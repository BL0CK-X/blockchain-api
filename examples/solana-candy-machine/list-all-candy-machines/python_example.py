from theblockchainapi import TheBlockchainAPIResource
import time

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

    current_time = int(time.time())
    result = BLOCKCHAIN_API_RESOURCE.list_all_candy_machines()
    print(result.keys())
    print(f"Last updated approx. {(current_time - result['last_updated']) // 60} minutes ago.")
    print(f"There are a total of {len(result['config_addresses_v1'])} V1 candy machines.")
    print(f"There are a total of {len(result['config_addresses_v2'])} V2 candy machines.")
    print(f"There are a total of {len(result['config_addresses_magic-eden-v1'])} Magic Eden candy machines.")


if __name__ == '__main__':
    example()
