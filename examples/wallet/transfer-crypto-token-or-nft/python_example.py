from theblockchainapi import BlockchainAPIResource, Blockchain, BlockchainNetwork, Wallet, CurrencyUnit
import time

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None

BLOCKCHAIN = Blockchain.SOLANA
NETWORK = BlockchainNetwork.SolanaNetwork.DEVNET
# NETWORK = BlockchainNetwork.SolanaNetwork.MAINNET_BETA

# BLOCKCHAIN = Blockchain.ETHEREUM
# NETWORK = BlockchainNetwork.EthereumNetwork.MAINNET
# NETWORK = BlockchainNetwork.EthereumNetwork.ROPSTEN

# ------ If using Solana..
DERIVATION_PATH = 'm/44/501/0/0'  # Used for Phantom, Sollet
# You can increment it for the next wallet in Phantom (e.g., what happens when you create a new wallet)
# DERIVATION_PATH = 'm/44/501/1/0'
# DERIVATION_PATH = None  # Defaults to 'm/44/501/0/0'
# DERIVATION_PATH = ""  # Use this if you created the wallet via the CLI

UNIT = CurrencyUnit.SolanaCurrencyUnit.SOL

# ------ If using Ethereum..
DERIVATION_PATH = None  # Use `None` for Metamask, the default

UNIT = CurrencyUnit.EthereumCurrencyUnit.ETH

BLOCKCHAIN_API_RESOURCE = BlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY,
    blockchain=BLOCKCHAIN,
    network=NETWORK
)


def example():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    # Create a wallet
    secret_recovery_phrase = BLOCKCHAIN_API_RESOURCE.generate_seed_phrase()
    wallet = Wallet(
        secret_recovery_phrase=secret_recovery_phrase,
        derivation_path=DERIVATION_PATH,
        passphrase=str(),
        private_key=None,  # OR You can supply this instead. e.g, [11, 234, ... 99, 24]
        b58_private_key=None  # OR You can supply this instead. e.g, x12x0120jd ... 192j0eds
    )
    blockchain_identifier = BLOCKCHAIN_API_RESOURCE.derive_blockchain_identifier(wallet=wallet)
    print(f"Blockchain Identifier: {blockchain_identifier}")
    print(f"Secret Recovery Phrase: {secret_recovery_phrase}")

    if BLOCKCHAIN.value == Blockchain.SOLANA.value:
        n_airdrops = 1
    else:
        n_airdrops = 3

    for _ in range(n_airdrops):
        # Get an airdrop on the devnet in order to be able to transfer SOL
        result = BLOCKCHAIN_API_RESOURCE.get_airdrop(blockchain_identifier)
        print(result)
        # We need to make sure this has time to process before transferring
        time.sleep(45)

    def get_balance():
        balance_result = BLOCKCHAIN_API_RESOURCE.get_balance(
            blockchain_identifier,
            unit=UNIT
        )
        print(f"Balance: {balance_result['balance']}")

    # Get the balance after the airdrop
    get_balance()

    # *** >>> TRANSFER THE SOL AIRDROP
    # You can put your address in the `transfer_to` and receive the SOL on the devnet.
    # You can view it in your Phantom wallet by going to Settings > Change Network > Devnet and then viewing
    # your SOL balance.

    # This is the amount we received in SOL from the Airdrop
    airdrop_amount = 0.015
    transfer_fee = 0.000005

    # We cannot send `airdrop_amount` because we need to pay for the transaction, and so we wouldn't have enough to
    # pay for the transaction because our balance would be `0` after sending `airdrop_amount` yet we still need to cover
    # the transaction.
    amount_to_send = str(airdrop_amount - transfer_fee)

    # Transfer to this address
    transfer_to = "8UmhEzc1CGkYazNQcGHvAAgTw9vy8mfBb5z4huyeftxc"

    # Call the transfer endpoint
    response = BLOCKCHAIN_API_RESOURCE.transfer(

        wallet=wallet,

        recipient_blockchain_identifier=transfer_to,
        amount=amount_to_send,

        token_blockchain_identifier=None

        # Set the fee payer if you want someone else to pay the fee.
        # fee_payer_wallet=SolanaWallet(b58_private_key='INSERT FEE PAYER PRIVATE KEY'),

        # If you don't want to send private keys, define the `sender_public_key` and set `return_compiled_transaction`
        # to `True`. This will return instructions that you can sign and then send as a transaction.
        # sender_blockchain_identifier=blockchain_identifier,
        # return_compiled_transaction=True  # default is False
        # If return_compiled_transaction==True, then set `wallet=None`
    )
    result = response['transaction_blockchain_identifier']

    print("Transferred!")
    if BLOCKCHAIN.value == Blockchain.SOLANA.value:
        print(f"View Transaction: https://explorer.solana.com/tx/{result}?cluster=devnet")
    else:
        print(f"View Transaction: https://ropsten.etherscan.io/tx/{result}")

    # The output of this `get_balance()` call should be `airdrop_amount` less
    # than the previous output of `get_balance()`
    get_balance()


if __name__ == '__main__':
    """
    Example Output:
    
    Public Key: 8vTgbAEVnh2RAP85njYmcSUAjYCBqbkZ638VsgJYbCve
    Secret Key: tattoo step foot essence amused marble slim access fiction lamp dawn talent
    Balance: 0.015
    5pWrB5SKoSAAfFqVFvvhyoUnxJGdY9gBQtuEbevVRgEHWybKGjBb7HfJXJVMM8xSijJ56EdoSohDGtmxzjuQpW46
    Balance: 0.0
    """
    example()
