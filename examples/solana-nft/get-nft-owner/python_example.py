from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork

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

    nft_address = '2pQPtnFm2mgXZrVWyNdcf5Qf2TWBGkTAeKZJhPjsc7Jn'
    url_to_view = f"https://explorer.solana.com/address/{nft_address}?cluster=devnet"
    print(url_to_view)
    nft_metadata = BLOCKCHAIN_API_RESOURCE.get_nft_metadata(
        mint_address=nft_address,
        network=SolanaNetwork.MAINNET_BETA
    )
    print(nft_metadata)


if __name__ == '__main__':
    example()
