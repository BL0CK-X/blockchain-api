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

    nfts = BLOCKCHAIN_API_RESOURCE.get_nfts_minted_from_candy_machine(
        candy_machine_id="9htmDvW58pjCMQdjFbovo8cGBZviDfeP3j7DKnikHEy5",
        network=SolanaNetwork.MAINNET_BETA
    )
    nft_hashes = list()
    for nft in nfts:
        nft_hashes.append(nft['pub_key_hash'])

    for pub_key_hash in nft_hashes:
        print(pub_key_hash)


if __name__ == '__main__':
    example()
