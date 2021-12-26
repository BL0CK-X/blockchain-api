from theblockchainapi import TheBlockchainAPIResource, \
    SolanaNetwork, SolanaCurrencyUnit, SolanaCandyMachineContractVersion
import time

# Get an API key pair for free here: https://dashboard.theblockchainapi.com/
MY_API_KEY_ID = 'gRs2aqZqmrdohVX'
MY_API_SECRET_KEY = 'KKwqHenqSiqulDh'

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

    # Creates a test candy machine with 5 available to mint
    # NOTE: This endpoint is unstable. It is only meant for testing purposes.
    candy_machine_id = BLOCKCHAIN_API_RESOURCE.create_test_candy_machine(
        secret_recovery_phrase=secret_recovery_phrase,
        derivation_path=derivation_path,
        passphrase=pass_phrase,
        network=SolanaNetwork.DEVNET,
        # include_gatekeeper=True,  # including gatekeeper will cause the tx to NOT succeed
        candy_machine_contract_version=SolanaCandyMachineContractVersion.V2
    )

    print("candy_machine_id", candy_machine_id)
    url_to_view = f"https://explorer.solana.com/address/{candy_machine_id}?cluster={network.value}"
    print("View candy machine here:", url_to_view)

    # Now get the config_address of the candy machine
    candy_details = BLOCKCHAIN_API_RESOURCE.get_candy_machine_metadata(
        candy_machine_id=candy_machine_id,
        network=SolanaNetwork.DEVNET,
        candy_machine_contract_version=SolanaCandyMachineContractVersion.V2
    )
    print(candy_details)
    print("Candy Machine Metadata: ", candy_details)
    config_address = candy_details['config_address']
    print("Config Address: ", config_address)

    # Now mint an NFT from the candy machine
    transaction_signature = BLOCKCHAIN_API_RESOURCE.mint_from_candy_machine(
        config_address=config_address,
        secret_recovery_phrase=secret_recovery_phrase,
        derivation_path=derivation_path,
        passphrase=pass_phrase,
        network=SolanaNetwork.DEVNET,
        candy_machine_contract_version=SolanaCandyMachineContractVersion.V2
    )

    # We get a task ID. Now we have to wait for this task to complete.
    print("transaction_signature", transaction_signature)

    # The transaction takes about 30-60 seconds to confirm...
    print("Sleeping for 30 seconds while the transaction is confirmed.")
    time.sleep(30)

    transaction_info = BLOCKCHAIN_API_RESOURCE.get_solana_transaction(
        tx_signature=transaction_signature,
        network=SolanaNetwork.DEVNET
    )
    did_succeed = transaction_info['result']['meta']['err'] is None
    print(f"Did the tx succeed? {did_succeed}")

    url_to_view = f"https://explorer.solana.com/tx/{transaction_signature}?cluster={network.value}"
    print(f"You can view the transaction here: {url_to_view}")


def minting_bot():
    # An NFT minting bot
    import threading

    def to_thread():
        start_ = int(time.time())
        task_id = BLOCKCHAIN_API_RESOURCE.mint_from_candy_machine(
            secret_recovery_phrase="secret_recovery_phrase",
            derivation_path="derivation_path",
            passphrase="pass_phrase",
            network=SolanaNetwork.DEVNET,
            config_address="config_address",
            candy_machine_contract_version=SolanaCandyMachineContractVersion.V2
        )
        print(task_id)
        end_ = int(time.time())
        print(f"{task_id}: {end_ - start_}")

    start = int(time.time())
    threads = list()
    for _ in range(50):
        x = threading.Thread(target=to_thread)
        x.start()

    for thread in threads:
        thread.join()

    end = int(time.time())
    print(f"Final: {end - start}")


if __name__ == '__main__':
    # minting_bot()
    example()
