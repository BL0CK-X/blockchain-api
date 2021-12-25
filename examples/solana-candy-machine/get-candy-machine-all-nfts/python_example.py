from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork

# Get an API key pair for free here: https://dashboard.theblockchainapi.com/
MY_API_KEY_ID = 'API-KEY-ID'
MY_API_SECRET_KEY = 'API-SECRET-KEY'
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)


def example(verbose=False):
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    # If you already know the candy machine ID, just enter it here.
    # NOTE: With v1 candy machines, we can sort MINTED and UNMINTED.
    # NOTE: With v2 candy machines, more work is required... see below.
    the_god_particle_candy_machine_id = "FmkrvXRenCGtwBHw3VtBcExp8eTdnau97upaewF4GUEX"
    print(f"Retrieving all NFTs from the candy machine with ID {the_god_particle_candy_machine_id}... "
          f"This API call can take around 45 seconds...")
    all_nfts = BLOCKCHAIN_API_RESOURCE.get_all_nfts_from_candy_machine(
        candy_machine_id=the_god_particle_candy_machine_id,
        network=SolanaNetwork.MAINNET_BETA
    )
    minted_nfts = all_nfts['minted_nfts']
    unminted_nfts = all_nfts['unminted_nfts']
    for nft in minted_nfts:
        if verbose:
            print(f"Minted: {nft}")
    for nft in unminted_nfts:
        if verbose:
            print(f"Unminted: {nft}")
    print(f"Minted NFTs: {len(minted_nfts)}")
    print(f"Example: {minted_nfts[0]}")
    print(f"Unminted NFTs: {len(unminted_nfts)}")
    print(f"Example: {unminted_nfts[0]}")

    # NOTE: With v2 candy machines, more work is required... see below.
    the_god_particle_candy_machine_id = "FmkrvXRenCGtwBHw3VtBcExp8eTdnau97upaewF4GUEX"
    print(f"Retrieving all NFTs from the candy machine with ID {the_god_particle_candy_machine_id}... "
          f"This API call can take around 45 seconds...")
    all_nfts = BLOCKCHAIN_API_RESOURCE.get_all_nfts_from_candy_machine(
        candy_machine_id=the_god_particle_candy_machine_id,
        network=SolanaNetwork.MAINNET_BETA
    )
    minted_nfts = all_nfts['minted_nfts']
    unminted_nfts = all_nfts['unminted_nfts']
    all_nfts = all_nfts['all_nfts']
    print("See.. these lists `minted_nfts` and `unminted_nfts` are empty because this endpoint does not distinguish"
          " between the two for v2 candy machines.")
    print(f"Minted NFTs: {len(minted_nfts)}")
    print(f"Unminted NFTs: {len(unminted_nfts)}")
    print(f"All NFTs: {len(all_nfts)}")
    print(f"Example: {all_nfts[0]}")


if __name__ == '__main__':
    example(verbose=True)
