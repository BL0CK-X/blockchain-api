from theblockchainapi import TheBlockchainAPIResource, SolanaCurrencyUnit

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

    # *** >>> TRANSFER THE NFT
    # You can put your address in the `transfer_to` and receive the NFT on the devnet.
    # You can view it in your Phantom wallet by going to Settings > Change Network > Devnet and then viewing
    # your collectibles.
    transfer_to = "31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj"
    transaction_signature = BLOCKCHAIN_API_RESOURCE.transfer(
        secret_recovery_phrase=secret_key,
        recipient_address=transfer_to,
        token_address=nft['mint']
    )
    print(transaction_signature)

    get_balance()


if __name__ == '__main__':
    example()
