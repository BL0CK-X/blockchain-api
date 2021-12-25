import requests
import json
import time


# Create one here: https://dashboard.theblockchainapi.com/#api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None
HEADERS = {
    'APIKeyId': MY_API_KEY_ID,
    'APISecretKey': MY_API_SECRET_KEY
}

if __name__ == '__main__':

    if HEADERS['APIKeyId'] is None or HEADERS['APISecretKey'] is None:
        raise Exception("Fill in your API keys.")

    response = requests.get(
        url='https://api.theblockchainapi.com/v1/solana/nft/candy_machine/list',
        headers=HEADERS
    )

    if response.status_code == 401:
        raise Exception("Invalid API keys.")
    elif response.status_code != 200:
        raise Exception(f"Unknown error. {response.status_code}")

    result = response.json()

    print("The list of all candy machine configuration addresses on Solana mainnet-beta: ")
    print(json.dumps(result, indent=4, sort_keys=True))

    last_updated = result['last_updated']
    current_time = int(time.time())
    print(f"Last updated approx. {(current_time - last_updated) // 60} minutes ago.")
    print(f"There are a total of {len(result['config_addresses_v1'])} V1 candy machines.")
    print(f"There are a total of {len(result['config_addresses_v2'])} V2 candy machines.")
    print(f"There are a total of {len(result['config_addresses_magic-eden-v1'])} Magic Eden candy machines.")
