from theblockchainapi import TheBlockchainAPIResource

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
    secret_key = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    print(secret_key)
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(secret_key)
    print(public_key)
    result = BLOCKCHAIN_API_RESOURCE.get_balance(public_key)
    print(result)


if __name__ == '__main__':
    example()
