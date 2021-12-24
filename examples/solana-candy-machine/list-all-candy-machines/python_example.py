# Coming soon to the Python wrapper `theblockchainapi`. For now, we use the `requests` package.
# pip install requests

import requests
import json
import time


HEADERS = {
    'APIKeyId': None,
    'APISecretKey': None
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
        print(f"There are a total of {len(result['config_addresses'])} candy machines.")
