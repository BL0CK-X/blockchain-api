import theblockchainapi
from theblockchainapi import TheBlockchainAPIResource

# Get an API key pair for free here: https://dashboard.theblockchainapi.com/
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)


def example():
    secret_key = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    print(secret_key)


if __name__ == '__main__':
    example()
