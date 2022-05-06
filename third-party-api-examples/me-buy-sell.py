from solana.rpc.api import Client
from solana.transaction import Transaction as SolanaTransaction
from solana.message import Message
from solana.publickey import PublicKey
from solana.keypair import Keypair
from typing import List, Union
from solana.rpc.types import TxOpts
from solana.rpc.core import RPCException, RPCNoResultException
import requests
import json


# ------------------------------------------------------------
#                  SEE INSTRUCTIONS BELOW
# ------------------------------------------------------------


class Error:

    def __init__(self, error_message, error_code=400):
        self.__error_message = error_message
        self.__error_code = error_code

    def get_error(self):
        return self.__error_message

    def get_error_code(self):
        return self.__error_code


def send_transaction(
        tx: SolanaTransaction,
        network_url: str,
        secret_keys: List[bytes],
        skip_preflight: bool = False,
        max_retries: int = 3
) -> Union[str, Error]:
    client = Client(network_url, timeout=30)

    solana_congestion_error = Error(
        "Unknown error. Exceeded max retries. Solana might be congested. "
        "Please note the time of this and report this to us."
    )

    for attempt in range(max_retries):

        signers = [
            Keypair.from_seed(bytes(PublicKey(s))) for s in secret_keys
        ]

        try:
            # noinspection PyTypeChecker
            result = client.send_transaction(
                tx,
                *signers,
                opts=TxOpts(
                    preflight_commitment='processed',
                    skip_confirmation=True,
                    skip_preflight=skip_preflight
                )
            )
        except RPCException as e:
            if attempt == max_retries - 1:
                return Error(str(e))
            continue
        except RPCNoResultException as e:
            if attempt == max_retries - 1:
                return Error(str(e))
            continue
        except Exception as e:
            if attempt == max_retries - 1:
                return Error("Unknown error... Please report this to us ASAP!\n\n" + str(e))
            continue

        transaction_signature = result.get('result', None)
        if transaction_signature is None and attempt == max_retries - 1:
            return Error("Unknown error. Result is NONE. Please report this to us.")

        return transaction_signature

    return solana_congestion_error


def submit_transaction_from_instructions(
        wallet: Keypair,
        instructions: List[int]
):
    instructions = bytearray(instructions)
    message = Message.deserialize(instructions)

    tx = SolanaTransaction(fee_payer=wallet.public_key)
    tx = tx.populate(message, signatures=[])

    secret_keys = [
        wallet.secret_key
    ]

    return send_transaction(
        tx=tx,
        network_url='https://api.mainnet-beta.solana.com/',
        secret_keys=secret_keys,
        skip_preflight=False,
        max_retries=3
    )


def get_instructions():

    # You might need to install requests: `pip install requests`
    # You can get an API key pair here: https://dashboard.blockchainapi.com?2d9UPbepdAmCwqJ5cExy#api-keys"

    # Read more here:
    # e.g., https://docs.blockchainapi.com/third-party-apis/2d9UPbepdAmCwqJ5cExy#operation/getBuyInstruction
    # e.g., https://docs.blockchainapi.com/third-party-apis/2d9UPbepdAmCwqJ5cExy#operation/getSellInstruction

    response = requests.post(
        url="https://api.blockchainapi.com/third-party-apis/2d9UPbepdAmCwqJ5cExy/v0.0.1/utility/getBuyInstruction",
        data=json.dumps(
            {
                "seller": "EwjUytd8yZvp6kQme6yeYp7NT4FwpJCF64rpNHW1URdb",
                "price": 1.9,
                "buyer": "DJHXvX9uatdjnitZgWCaSi5TYGiMhNP8tLWkdZLKwvDX",
                "mint_address": "5VtKwrFuLv3LCKMnDtCpHaj978sF1zdjTkihovRLuj6m"
            }
        ),
        headers={
            "APIKeyId": "INSERT-YOUR-API-KEY-ID",
            "APISecretKey": "INSERT-YOUR-API-SECRET-KEY"
        }
    )

    if response.status_code == 200:
        instructions = response.json()['instruction']
        if isinstance(instructions, list):
            return instructions
        elif isinstance(instructions, str):
            return json.loads(instructions)
        else:
            raise NotImplementedError
    else:
        raise Exception(f"Response Error: {response.text}")


def main():

    # Ensure packages are installed: `pip install solana`

    # Step (1): Initialize your wallet
    wallet = Keypair()

    print("Save this wallet information. ")
    print("Public Key: ", wallet.public_key)
    print("Private Key: ", wallet.secret_key)

    # You can reinitialize a saved wallet like this:
    wallet = Keypair.from_secret_key(wallet.secret_key)
    # Then send SOL to `wallet.public_key` and use the wallet as you please.

    # ==================================== BEGIN: IMPORTANT NOTE ====================================
    # Do not sign transaction instructions you do not know or trust.
    # Always use a burner wallet when testing new instructions.
    # NEVER use your personal wallet.
    # Always store in the burner wallet what you're willing to lose.
    # ==================================== END:   IMPORTANT NOTE ====================================

    # Step (2) Pull the instructions for a transaction via an API.
    # Here are two examples:
    # e.g., https://docs.blockchainapi.com/third-party-apis/2d9UPbepdAmCwqJ5cExy#operation/getBuyInstruction
    # e.g., https://docs.blockchainapi.com/third-party-apis/2d9UPbepdAmCwqJ5cExy#operation/getSellInstruction
    instructions = get_instructions()
    if isinstance(instructions, Error):
        return Error(instructions.get_error(), instructions.get_error_code())

    # Step (3) Sign and send the transaction
    submit_transaction_from_instructions(
        wallet=wallet,
        instructions=instructions
    )


if __name__ == '__main__':
    main()
