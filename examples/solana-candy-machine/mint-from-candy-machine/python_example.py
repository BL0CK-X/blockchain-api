from theblockchainapi import TheBlockchainAPIResource, \
    SolanaNetwork, SolanaCurrencyUnit, SolanaCandyMachineContractVersion, SolanaWallet, DerivationPath
import time

# Get an API key pair for free here: https://dashboard.blockchainapi.com/
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
    # network = SolanaNetwork.MAINNET_BETA
    wallet = SolanaWallet(
        secret_recovery_phrase=BLOCKCHAIN_API_RESOURCE.generate_secret_key(),
        derivation_path=DerivationPath.CLI_PATH,
        passphrase=str(),
        private_key=None,  # OR You can supply this instead. e.g, [11, 234, ... 99, 24]
        b58_private_key=None  # OR You can supply this instead. e.g, x12x0120jd ... 192j0eds
    )

    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(wallet=wallet)
    print(public_key)

    for _ in range(3):
        # Get an airdrop of 0.045 (0.015 * 3) to be able to pay for the creation of the candy machine
        BLOCKCHAIN_API_RESOURCE.get_airdrop(recipient_address=public_key)

    print(BLOCKCHAIN_API_RESOURCE.get_balance(public_key, SolanaCurrencyUnit.SOL, network))

    # Creates a test candy machine with 5 available to mint
    # NOTE: This endpoint is unstable. It is only meant for testing purposes.
    candy_machine_id = BLOCKCHAIN_API_RESOURCE.create_test_candy_machine(
        wallet=wallet,
        network=network,
        # include_gatekeeper=True,  # including gatekeeper will cause the tx to NOT succeed
        candy_machine_contract_version=SolanaCandyMachineContractVersion.V2
    )

    print("candy_machine_id", candy_machine_id)
    url_to_view = f"https://explorer.solana.com/address/{candy_machine_id}?cluster={network.value}"
    print("View candy machine here:", url_to_view)

    # Now get the config_address of the candy machine
    candy_details = BLOCKCHAIN_API_RESOURCE.get_candy_machine_metadata(
        candy_machine_id=candy_machine_id,
        network=network,
        candy_machine_contract_version=SolanaCandyMachineContractVersion.V2
    )
    print(candy_details)
    print("Candy Machine Metadata: ", candy_details)
    config_address = candy_details['config_address']
    print("Config Address: ", config_address)

    transaction_signatures = list()

    for _ in range(10):
        # Now mint an NFT from the candy machine
        transaction_signature = BLOCKCHAIN_API_RESOURCE.mint_from_candy_machine(
            config_address=config_address,
            wallet=wallet,
            network=network,
            candy_machine_contract_version=SolanaCandyMachineContractVersion.V2
        )
        transaction_signatures.append(transaction_signature)

    print(transaction_signatures)

    for transaction_signature in transaction_signatures:

        # We get a task ID. Now we have to wait for this task to complete.
        print("transaction_signature", transaction_signature)

        # The transaction takes about 30-60 seconds to confirm...
        # Check out this Gist for how to formally check confirmation status:
        # https://gist.github.com/joshwolff1/298e8251e43ff9b4815028683b1ca17d
        print("Sleeping for 30 seconds while the transaction is confirmed.")
        time.sleep(30)

        transaction_info = BLOCKCHAIN_API_RESOURCE.get_solana_transaction(
            tx_signature=transaction_signature,
            network=network
        )
        print(transaction_info)
        did_succeed = transaction_info['result']['meta']['err'] is None
        print(f"Did the tx succeed? {did_succeed}")

        url_to_view = f"https://explorer.solana.com/tx/{transaction_signature}?cluster={network.value}"
        print(f"You can view the transaction here: {url_to_view}")


def minting_bot():
    # An NFT minting bot
    import threading

    wallet = SolanaWallet(
        secret_recovery_phrase=BLOCKCHAIN_API_RESOURCE.generate_secret_key(),
        derivation_path=DerivationPath.CLI_PATH,
        passphrase=str(),
        private_key=None,  # OR You can supply this instead. e.g, [11, 234, ... 99, 24]
        b58_private_key=None  # OR You can supply this instead. e.g, x12x0120jd ... 192j0eds
    )

    def to_thread(my_wallet):
        start_ = int(time.time())

        task_id = BLOCKCHAIN_API_RESOURCE.mint_from_candy_machine(
            wallet=my_wallet,
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
        x = threading.Thread(target=to_thread, args=(wallet, ))
        x.start()

    for thread in threads:
        thread.join()

    end = int(time.time())
    print(f"Final: {end - start}")


if __name__ == '__main__':
    # minting_bot()
    example()
