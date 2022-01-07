from theblockchainapi import TheBlockchainAPIResource, SolanaWallet

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

    private_key = BLOCKCHAIN_API_RESOURCE.generate_private_key()

    b58_private_key = private_key['b58_private_key']
    print("This is a base58-encoded private key. This is what Phantom shows when you click `Show Private Key`")
    print(b58_private_key)

    print("-" * 20)

    private_key = private_key['private_key']
    print("This is a standard private key array. This is what SolFlare shows when you click `Export Private Key`")
    print(private_key)

    # You can now initialize `SolanaWallet`, which can be used to create an NFT, transfer SOL, etc.
    # See the other examples.
    _ = SolanaWallet(b58_private_key=b58_private_key)
    _ = SolanaWallet(private_key=private_key)


if __name__ == '__main__':
    example()
