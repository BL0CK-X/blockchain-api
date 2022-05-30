from theblockchainapi import SolanaAPIResource, SolanaNetwork

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

    public_key = 'DJHXvX9uatdjnitZgWCaSi5TYGiMhNP8tLWkdZLKwvDX'
    nfts = BLOCKCHAIN_API_RESOURCE.get_nfts_belonging_to_address(
        public_key,
        network=SolanaNetwork.MAINNET_BETA
    )
    for nft in nfts:
        print("-" * 20)
        print(f"NFT: {nft}")

    print(f"This person owns {len(nfts)} NFTs.")


if __name__ == '__main__':
    example()
