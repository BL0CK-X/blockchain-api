from theblockchainapi import SolanaAPIResource, SolanaCurrencyUnit, SolanaWallet, DerivationPath

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

    # Create a wallet
    secret_recovery_phrase = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    wallet = SolanaWallet(
        secret_recovery_phrase=secret_recovery_phrase,
        derivation_path=DerivationPath.CLI_PATH,
        passphrase=str(),
        private_key=None,  # OR You can supply this instead. e.g, [11, 234, ... 99, 24]
        b58_private_key=None  # OR You can supply this instead. e.g, x12x0120jd ... 192j0eds
    )
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(wallet=wallet)
    print(f"Public Key: {public_key}")
    print(f"Secret Recovery Phrase: {secret_recovery_phrase}")

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
        wallet=wallet,
        name="The Blockchain API",
        symbol="BLOCKX",
        image_url="https://pbs.twimg.com/profile_images/1441903262509142018/_8mjWhho_400x400.jpg"
    )
    print("NFT: ", nft)
    print(f"You can view the NFT here: {nft['explorer_url']}")

    # *** >>> TRANSFER THE NFT
    # You can put your address in the `transfer_to` and receive the NFT on the devnet.
    # You can view it in your Phantom wallet by going to Settings > Change Network > Devnet and then viewing
    # your collectibles.
    transfer_to = "8UmhEzc1CGkYazNQcGHvAAgTw9vy8mfBb5z4huyeftxc"
    transaction_signature = BLOCKCHAIN_API_RESOURCE.transfer(
        wallet=wallet,
        recipient_address=transfer_to,
        token_address=nft['mint'],
        # fee_payer_wallet=SolanaWallet(
        #     b58_private_key='INSERT FEE PAYER PRIVATE KEY',
        #     private_key='',  # Or one of these other options
        #     secret_recovery_phrase=''  # Or one of these other options
        # )
    )
    print("Transferred!")
    print(f"You can view the transaction here: https://explorer.solana.com/tx/{transaction_signature}?cluster=devnet")

    get_balance()


if __name__ == '__main__':
    example()
