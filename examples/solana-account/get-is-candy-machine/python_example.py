from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork

# Get an API key pair for free here: https://dashboard.theblockchainapi.com/
MY_API_KEY_ID = "0qiMmf8BEZYCN4E"
MY_API_SECRET_KEY = "99t1AuOhcZHxcRQ"
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

    def get_account(pub_key, title):
        response = BLOCKCHAIN_API_RESOURCE.get_account_info(
            public_key=pub_key,
            network=SolanaNetwork.MAINNET_BETA
        )
        print("-" * 40)
        print(title)
        print(response)
        print("\n\n\n")

    # Get an NFT
    get_account("EEr5yQpNXf7Bru6Rt5podx56HGW9CEehXqgRGh2wa71w", "NFT Account")

    # Get an SPL Token
    get_account("SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt", "SPL Token")

    # Get smart contract
    get_account("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", "Smart Contract")

    # Get an associated token account
    get_account("3CdXPzAgY72HnaReerSXhfaJa5WiBj6ftgsTB9sv6RKJ", "Associated Token Account")

    # Get candy machine account
    get_account("9htmDvW58pjCMQdjFbovo8cGBZviDfeP3j7DKnikHEy5", "Candy Machine Account")

    # Get a system program (wallet account, such as the public key to your wallet)
    get_account("31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj", "System Program")


if __name__ == '__main__':
    example()
