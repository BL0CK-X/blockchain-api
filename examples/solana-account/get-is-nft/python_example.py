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

    def get_is_nft(pub_key, title, network):
        response = BLOCKCHAIN_API_RESOURCE.get_is_nft(
            public_key=pub_key,
            network=network
        )
        print(title)
        print(response)
        print("-" * 40)

    # Get an NFT
    get_is_nft("EEr5yQpNXf7Bru6Rt5podx56HGW9CEehXqgRGh2wa71w", "NFT Account", SolanaNetwork.MAINNET_BETA)

    # Get an SPL Token
    get_is_nft("SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt", "SPL Token", SolanaNetwork.MAINNET_BETA)

    # Get smart contract
    get_is_nft("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", "Smart Contract", SolanaNetwork.MAINNET_BETA)

    # Get an associated token account
    get_is_nft("3CdXPzAgY72HnaReerSXhfaJa5WiBj6ftgsTB9sv6RKJ", "Associated Token Account", SolanaNetwork.MAINNET_BETA)

    # Get candy machine account
    get_is_nft("9htmDvW58pjCMQdjFbovo8cGBZviDfeP3j7DKnikHEy5", "Candy Machine Account", SolanaNetwork.MAINNET_BETA)

    # Get a system program (wallet account, such as the public key to your wallet)
    get_is_nft("31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj", "System Program", SolanaNetwork.MAINNET_BETA)


if __name__ == '__main__':
    example()
