from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork, SolanaCurrencyUnit

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

    print(candy_machine_id)
    url_to_view = f"https://explorer.solana.com/address/{candy_machine_id}?cluster={network.value}"
    print(url_to_view)


if __name__ == '__main__':
    example()
