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

    # If you already know the candy machine ID, just enter it here.
    the_god_particle_candy_machine_id = "FmkrvXRenCGtwBHw3VtBcExp8eTdnau97upaewF4GUEX"
    print("Retrieving all NFTs from the given candy machine... This API call can take around 45 seconds...")
    all_nfts = BLOCKCHAIN_API_RESOURCE.get_all_nfts_from_candy_machine(
        candy_machine_id=the_god_particle_candy_machine_id,
        network=SolanaNetwork.MAINNET_BETA
    )
    minted_nfts = all_nfts['minted_nfts']
    unminted_nfts = all_nfts['unminted_nfts']
    for nft in minted_nfts:
        print(f"Minted: {nft}")
    for nft in unminted_nfts:
        print(f"Unminted: {nft}")
    print(f"Minted NFTs: {len(minted_nfts)}")
    print(f"Unminted NFTs: {len(unminted_nfts)}")


if __name__ == '__main__':
    example()
