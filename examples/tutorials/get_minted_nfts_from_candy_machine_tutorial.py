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

    # (1) Get the CM ID. There are several ways to do this. One way is to get it from an NFT
    # that was minted from the CM.
    try:
        nft_mint_address = "63k8TCFNfQigyCfR4hvZg5moHZQ2uJYnfsuoDnrjHyeb"
        network = SolanaNetwork.MAINNET_BETA

        result = BLOCKCHAIN_API_RESOURCE.get_candy_machine_id_from_nft(
            mint_address=nft_mint_address,
            network=network
        )
        candy_machine_id = result['candy_machine_id']

        print("Candy Machine ID:", result['candy_machine_id'])
        print("Candy Machine Version:", result['candy_machine_contract_version'])

    except Exception as e:
        print(str(e))
        raise e

    # (2) Now get all of the NFTs minted with that candy machine.
    print(f"Retrieving all NFTs from the V2 candy machine with ID {candy_machine_id}... "
          f"This API call can take around 45 seconds...")

    result = BLOCKCHAIN_API_RESOURCE.get_all_nfts_from_candy_machine(
        candy_machine_id=candy_machine_id,
        network=network
    )
    minted_nfts = result['minted_nfts']
    unminted_nfts = result['unminted_nfts']
    print(f"Found Minted NFTs: {len(minted_nfts)}")
    print(f"Found Unminted NFTs: {len(unminted_nfts)}")
    print("Play with the code to loop through these NFTs...")


if __name__ == '__main__':
    example()
