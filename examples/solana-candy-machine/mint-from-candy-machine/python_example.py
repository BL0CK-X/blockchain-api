from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork, SolanaCurrencyUnit
import time

# Get an API key pair for free here: https://dashboard.theblockchainapi.com/
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)
TASK_IN_PROGRESS_STATUS_CODE = 202


def example():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    # Create a new wallet
    network = SolanaNetwork.DEVNET
    secret_recovery_phrase = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    derivation_path = str()
    pass_phrase = str()
    print(secret_recovery_phrase)
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(
        secret_recovery_phrase=secret_recovery_phrase,
        derivation_path=derivation_path,
        passphrase=pass_phrase
    )
    print(public_key)

    for _ in range(3):
        # Get an airdrop of 0.045 (0.015 * 3) to be able to pay for the creation of the candy machine
        BLOCKCHAIN_API_RESOURCE.get_airdrop(recipient_address=public_key)

    print(BLOCKCHAIN_API_RESOURCE.get_balance(public_key, SolanaCurrencyUnit.SOL, SolanaNetwork.DEVNET))

    # Creates a test candy machine with 2 available to mint
    # NOTE: This endpoint is unstable. It is only meant for testing purposes.
    candy_machine_id = BLOCKCHAIN_API_RESOURCE.create_test_candy_machine(
        secret_recovery_phrase=secret_recovery_phrase,
        derivation_path=derivation_path,
        passphrase=pass_phrase,
        network=SolanaNetwork.DEVNET
    )

    print("candy_machine_id", candy_machine_id)
    url_to_view = f"https://explorer.solana.com/address/{candy_machine_id}?cluster={network.value}"
    print("View candy machine ID here:", url_to_view)

    # Now mint an NFT from the candy machine
    task_id = BLOCKCHAIN_API_RESOURCE.mint_from_candy_machine(
        secret_recovery_phrase=secret_recovery_phrase,
        derivation_path=derivation_path,
        passphrase=pass_phrase,
        network=SolanaNetwork.DEVNET,
        candy_machine_id=candy_machine_id
    )

    # We get a task ID. Now we have to wait for this task to complete.
    print("task_id", task_id)

    time_slept = 0
    time_to_sleep = 30

    while True:
        response = BLOCKCHAIN_API_RESOURCE.get_task(task_id)

        if response['status_code'] == TASK_IN_PROGRESS_STATUS_CODE:
            # 202 = In Progress
            # This task might take 180 seconds to show as completed. It might take as long as 300 seconds.
            print(f"Sleeping for {time_to_sleep} seconds... Have already slept for {time_slept} seconds.")
            time.sleep(time_to_sleep)
            time_slept += time_to_sleep
            continue
        else:
            break

    # Parse the response
    print(response)
    transaction_signature = response['response']['transaction_signature']
    url_to_view = f"https://explorer.solana.com/tx/{transaction_signature}?cluster={network.value}"
    print(url_to_view)


if __name__ == '__main__':
    example()
