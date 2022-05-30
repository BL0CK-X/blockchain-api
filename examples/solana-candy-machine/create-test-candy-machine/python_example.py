from theblockchainapi import SolanaAPIResource, SolanaNetwork, \
    SolanaCurrencyUnit, SolanaWallet, DerivationPath

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None

BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
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

    print(BLOCKCHAIN_API_RESOURCE.get_balance(public_key, SolanaCurrencyUnit.SOL, SolanaNetwork.DEVNET))

    # Creates a test candy machine with 5 available to mint
    # NOTE: This endpoint is not available for v1 mints.
    # NOTE: It is only meant for testing purposes.
    candy_machine_id = BLOCKCHAIN_API_RESOURCE.create_test_candy_machine(
        wallet=wallet,
        # include_gatekeeper=False,  # You can set this to True to include a gatekeeper. Only applies to v2
        # candy machines. When gatekeeper is ON, our mint endpoint doesn't work.
        network=SolanaNetwork.DEVNET
    )

    print(candy_machine_id)
    url_to_view = f"https://explorer.solana.com/address/{candy_machine_id}?cluster={network.value}"
    print(url_to_view)


if __name__ == '__main__':
    example()
