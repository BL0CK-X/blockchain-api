from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork

# Get an API key pair for free here: https://dashboard.theblockchainapi.com/
MY_API_KEY_ID = 'API-KEY-ID'
MY_API_SECRET_KEY = 'API-SECRET-KEY'
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

    nft_mint_address = '2pQPtnFm2mgXZrVWyNdcf5Qf2TWBGkTAeKZJhPjsc7Jn'
    network = SolanaNetwork.MAINNET_BETA

    url_to_view = f"https://explorer.solana.com/address/{nft_mint_address}?cluster={network.value}"
    print(f"View the NFT: {url_to_view}")

    nft_owner = BLOCKCHAIN_API_RESOURCE.get_nft_owner(
        mint_address=nft_mint_address,
        network=network
    )
    print(f"Retrieved the NFT Owner: {nft_owner}")
    print(f"See the owner's token holdings: "
          f"https://explorer.solana.com/address/{nft_owner}/tokens?cluster={network.value}")
    print(f"You should see {nft_mint_address} in their token holdings.")


if __name__ == '__main__':
    example()
