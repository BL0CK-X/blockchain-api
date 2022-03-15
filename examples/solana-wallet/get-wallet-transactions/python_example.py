from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork

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

    public_key = '2VxSwAFYDx82gbKZTXsa5dieg3V9ZxbcZtnrUuv8WJ6g'
    print(f"Transactions for {public_key}")
    transactions = BLOCKCHAIN_API_RESOURCE.get_wallet_transactions(
        public_key,
        network=SolanaNetwork.MAINNET_BETA
    )
    for transaction in transactions:
        print(f"Transaction Signature: {transaction}")

    public_key = '2VxSwAFYDx82gbKZTXsa5dieg3V9ZxbcZtnrUuv8WJ6g'
    print(f"Holdings for {public_key}")
    transactions = BLOCKCHAIN_API_RESOURCE.get_wallet_transactions(
        public_key,
        network=SolanaNetwork.MAINNET_BETA
    )
    for transaction in transactions:
        print(f"Transaction Signature: {transaction}")
        # You can get more advanced details about every transaction with this function.
        # Be careful uncommenting this in the `for` loop as you might accidentally use a lot of credits.
        # transaction = BLOCKCHAIN_API_RESOURCE.get_solana_transaction(
        #     tx_signature=transaction,
        #     network=SolanaNetwork.MAINNET_BETA
        # )
        # import json
        # print(json.dumps(transaction, indent=4))


if __name__ == '__main__':
    example()
