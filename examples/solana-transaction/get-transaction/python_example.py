from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork
import json

# Get an API key pair for free here: https://dashboard.theblockchainapi.com/
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)


def example():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    # This is the transaction signature for a transaction that lists an NFT on SolSea.
    tx_signature = "5wHu1qwD7q5ifaN5nwdcDqNFo53GJqa7nLp2BeeEpcHCusb4GzARz4GjgzsEHMkBMgCJMGa6GSQ1VG96Exv8kt2W"

    transaction_info = BLOCKCHAIN_API_RESOURCE.get_solana_transaction(
        tx_signature=tx_signature,
        network=SolanaNetwork.MAINNET_BETA
    )

    print(json.dumps(transaction_info, indent=4, sort_keys=True))


if __name__ == '__main__':
    example()
