from theblockchainapi import TheBlockchainAPIResource, SolanaWallet
from concurrent.futures import ThreadPoolExecutor
import time


# Get an API key pair here: https://dashboard.blockchainapi.com/#api-keys
RESOURCE = TheBlockchainAPIResource(
    api_key_id=None,
    api_secret_key=None
)
MAX_RATE_LIMIT = 25


if __name__ == '__main__':
    starting_with = 'api'

    # Not case sensitive
    import string
    loops_required = 1
    for my_character in starting_with:
        if my_character in string.ascii_uppercase or my_character in string.ascii_lowercase:
            loops_required *= 2 / (26 + 26 + 10)
        else:
            loops_required *= 1 / (26 + 26 + 10)
    loops_required = int(1 / loops_required)
    print(f"Expected Loops Required: {loops_required}")

    while True:

        start = int(time.time())
        futures = list()

        with ThreadPoolExecutor(max_workers=200) as executor:

            for _ in range(MAX_RATE_LIMIT):

                def generate():
                    # noinspection PyBroadException
                    try:
                        private_key = RESOURCE.generate_private_key()
                        public_key = RESOURCE.derive_public_key(
                            wallet=SolanaWallet(b58_private_key=private_key['b58_private_key'])
                        )
                        print(public_key)
                        if public_key[:len(starting_with)].lower() == starting_with.lower():
                            print(private_key)
                            return private_key
                        return None
                    except Exception:
                        return None

                future = executor.submit(generate)
                futures.append(future)

            should_break = False
            for future in futures:
                future_result = future.result()
                if future_result is not None:
                    print(future_result)
                    should_break = True
                    break

            if should_break:
                break

        end = int(time.time())
        expected_end = start + 60
        if expected_end - end > 0:
            time.sleep(expected_end - end)
