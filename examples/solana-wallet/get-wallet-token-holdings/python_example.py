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

    public_key = 'BNedxPqVzNAYDfJsdCeMqegTGTTG4qbjci9WkwsXBGsx'
    nfts = BLOCKCHAIN_API_RESOURCE.get_nfts_belonging_to_address(
        public_key,
        network=SolanaNetwork.MAINNET_BETA
    )
    for nft in nfts:
        print(f"Mint Address: {nft}")


if __name__ == '__main__':
    example()
