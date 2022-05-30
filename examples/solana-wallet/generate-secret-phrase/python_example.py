from theblockchainapi import SolanaAPIResource, SolanaWallet

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None


BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)


def example():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")
    secret_recovery_phrase = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    print(secret_recovery_phrase)

    # You can now initialize `SolanaWallet`, which can be used to create an NFT, transfer SOL, etc.
    # See the other examples.
    _ = SolanaWallet(secret_recovery_phrase=secret_recovery_phrase)


if __name__ == '__main__':
    example()
