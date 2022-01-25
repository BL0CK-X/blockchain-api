from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork

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

    def get_spl_token(pub_key, title, network):
        # noinspection PyBroadException
        print(title)
        try:
            response = BLOCKCHAIN_API_RESOURCE.get_spl_token(
                public_key=pub_key,
                network=network
            )
            print(response)
        except Exception as e:
            print("Did not find.", str(e))
        print("-" * 40)

    # Get an NFT -- actually an SPL token behind the scenes!
    get_spl_token("EEr5yQpNXf7Bru6Rt5podx56HGW9CEehXqgRGh2wa71w", "NFT Account", SolanaNetwork.MAINNET_BETA)

    # Get an SPL Token
    get_spl_token("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", "USDC Token", SolanaNetwork.MAINNET_BETA)

    # Get an SPL Token
    get_spl_token("MangoCzJ36AjZyKwVj3VnYU4GTonjfVEnJmvvWaxLac", "Mango Token", SolanaNetwork.MAINNET_BETA)

    # Get an SPL Token
    get_spl_token("SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt", "Serum Token", SolanaNetwork.MAINNET_BETA)

    # Get smart contract
    get_spl_token("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", "Smart Contract", SolanaNetwork.MAINNET_BETA)

    # Get candy machine account, v1
    get_spl_token(
        "9htmDvW58pjCMQdjFbovo8cGBZviDfeP3j7DKnikHEy5", "Candy Machine Account: v1", SolanaNetwork.MAINNET_BETA
    )

    # Get candy machine account, v2
    get_spl_token(
        "C3gQisQbf2tHdiwTJPXjV3AoYkZg6vsmKvtCkhxM9oP4", "Candy Machine Account: v2", SolanaNetwork.MAINNET_BETA
    )

    # Get candy machine account, magic-eden
    get_spl_token(
        "8eF9sgCopyfMo5JBLCLxCdwBvU1WvKG2y56hcgdJ43Fc", "Candy Machine Account: Magic Eden v1", SolanaNetwork.MAINNET_BETA
    )

    # Get a system program (wallet account, such as the public key to your wallet)
    get_spl_token("31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj", "System Program", SolanaNetwork.MAINNET_BETA)


if __name__ == '__main__':
    example()
