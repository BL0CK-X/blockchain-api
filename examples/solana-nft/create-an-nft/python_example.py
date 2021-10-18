from theblockchainapi import TheBlockchainAPIResource, SolanaCurrencyUnit

# Get an API key pair for free here: https://dashboard.theblockchainapi.com/
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)


def example():
    """
    This example creates a new wallet, gets an airdrop to mint an NFT, and then mints an NFT.
    """
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    # Create a wallet
    secret_key = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(
        secret_recovery_phrase=secret_key
    )
    print(f"Public Key: {public_key}")
    print(f"Secret Key: {secret_key}")

    # Get an airdrop on the devnet in order to be able to mint an NFT
    BLOCKCHAIN_API_RESOURCE.get_airdrop(public_key)

    # We need to make sure this has time to process before minting the NFT!
    import time
    time.sleep(25)

    def get_balance():
        balance_result = BLOCKCHAIN_API_RESOURCE.get_balance(public_key, unit=SolanaCurrencyUnit.SOL)
        print(f"Balance: {balance_result['balance']}")
    get_balance()

    # Mint an NFT
    nft = BLOCKCHAIN_API_RESOURCE.create_nft(
        secret_recovery_phrase=secret_key,
        nft_name="The Blockchain API",
        nft_symbol="BLOCKX",
        nft_url="https://pbs.twimg.com/profile_images/1441903262509142018/_8mjWhho_400x400.jpg"
    )
    print("NFT: ", nft)
    print(f"You can view the NFT here: {nft['explorer_url']}")


if __name__ == '__main__':
    example()
