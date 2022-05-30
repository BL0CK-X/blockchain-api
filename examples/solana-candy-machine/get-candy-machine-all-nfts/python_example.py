from theblockchainapi import SolanaAPIResource, SolanaNetwork

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None

BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
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

    # If you have an NFT and it was created by a candy machine, you can get the candy machine ID with this
    # endpoint: https://docs.theblockchainapi.com/#operation/solanaGetNFTsCandyMachineId

    candy_machine_id = "FmkrvXRenCGtwBHw3VtBcExp8eTdnau97upaewF4GUEX"

    print(f"Retrieving all NFTs from the V1 candy machine with ID {candy_machine_id}... "
          f"This API call can take around 45 seconds...")
    result = BLOCKCHAIN_API_RESOURCE.get_all_nfts_from_candy_machine(
        candy_machine_id=candy_machine_id,
        network=SolanaNetwork.MAINNET_BETA
    )
    minted_nfts = result['minted_nfts']
    unminted_nfts = result['unminted_nfts']
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
    print(f"Was the division of NFTs into minted and unminted accurate? {result['accurate']}")

    # NOTE: With v2 candy machines, more work is required... see below.
    candy_machine_id = "BdgRfRzzFEWTa7Ka5bzWEy1QidSc5qVvn8zq7vRBrDL3"
    print(f"Retrieving all NFTs from the V2 candy machine with ID {candy_machine_id}... "
          f"This API call can take around 45 seconds...")
    result = BLOCKCHAIN_API_RESOURCE.get_all_nfts_from_candy_machine(
        candy_machine_id=candy_machine_id,
        network=SolanaNetwork.MAINNET_BETA
    )
    minted_nfts = result['minted_nfts']
    unminted_nfts = result['unminted_nfts']
    all_nfts = result['all_nfts']
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
    print(f"Was the division of NFTs into minted and unminted accurate? {result['accurate']}")
    print(f"All NFTs: {len(all_nfts)}")
    print(f"Example: {all_nfts[0]}")


if __name__ == '__main__':
    example(verbose=False)
