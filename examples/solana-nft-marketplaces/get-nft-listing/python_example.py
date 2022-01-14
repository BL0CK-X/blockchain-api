from theblockchainapi import TheBlockchainAPIResource, \
    SolanaNetwork, SolanaCurrencyUnit, SolanaWallet
import json

# Get an API key pair for free here: https://dashboard.blockchainapi.com/
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

    network = SolanaNetwork.DEVNET

    # Create a new wallet
    wallet = SolanaWallet(
        # (1) SUPPLY Seed phrase
        # secret_recovery_phrase=BLOCKCHAIN_API_RESOURCE.generate_secret_key(),
        # derivation_path=DerivationPath.CLI_PATH,
        # passphrase=str(),
        # (2) OR You can supply this instead. e.g, [11, 234, ... 99, 24]
        # private_key=None,
        # (3) OR You can supply this instead. e.g, x12x0120jd ... 192j0eds
        b58_private_key=BLOCKCHAIN_API_RESOURCE.generate_private_key()['b58_private_key']
    )

    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(wallet=wallet)
    print(f"We just created a wallet with public key address: {public_key}")

    for _ in range(3):
        # Get an airdrop of 0.045 (0.015 * 3) to be able to pay for the creation of the candy machine
        BLOCKCHAIN_API_RESOURCE.get_airdrop(recipient_address=public_key)

    print(BLOCKCHAIN_API_RESOURCE.get_balance(public_key, SolanaCurrencyUnit.SOL, SolanaNetwork.DEVNET))

    new_nft = BLOCKCHAIN_API_RESOURCE.create_nft(
        wallet=wallet,
        network=network,
        nft_name="Rich Coin",
        nft_symbol="WAGMI"
    )
    mint_address = new_nft['mint']
    print(f"Minted a new NFT with mint address, `{mint_address}`.")

    print("The NFT isn't listed, but let's retrieve the listing to see what happens.")

    try:
        nft_listing = BLOCKCHAIN_API_RESOURCE.get_nft_listing(mint_address, network)
        print(json.dumps(nft_listing, indent=4))
    except Exception as e:
        print(f"EXCEPTION: {str(e)}")

    nft_price = 69  # lamports

    listing_tx = BLOCKCHAIN_API_RESOURCE.list_nft_on_solsea(
        mint_address=mint_address,
        wallet=wallet,
        network=network,
        nft_price=nft_price
    )
    print(f"Listed NFT with tx signature: `{listing_tx}`.")

    nft_listing = BLOCKCHAIN_API_RESOURCE.get_nft_listing(mint_address, network)
    print(json.dumps(nft_listing, indent=4))

    print(
        f"We can now delist it to get it back, buy it,"
        f" and interact with other listed NFTs using other Blockchain API functions."
    )


if __name__ == '__main__':
    example()
