from theblockchainapi import SolanaAPIResource, SolanaNetwork

# Get an API key pair for free here: https://dashboard.theblockchainapi.com/api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None

BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)


def example():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    public_key = 'GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ'
    print(f"Holdings for {public_key}")
    token_holdings = BLOCKCHAIN_API_RESOURCE.get_wallet_token_holdings(
        public_key,
        include_nfts=False,
        include_zero_balance_holdings=False,
        network=SolanaNetwork.MAINNET_BETA
    )
    for token_holding in token_holdings:
        print(f"Token Holding: {token_holding}")

    # As you can see here... https://explorer.solana.com/address/BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX/tokens
    # ... public key owns 2 NFTs, but used to also own 2 others. Set `include_zero_balance_holdings` to `True` and
    # `include_nfts` to `True` to see all 4 NFTs.. See that the balance is `0` for two of the NFTs and `1` for the other
    # two NFTs.
    public_key = 'BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX'
    print(f"Holdings for {public_key}")
    token_holdings = BLOCKCHAIN_API_RESOURCE.get_wallet_token_holdings(
        public_key,
        include_nfts=True,
        include_zero_balance_holdings=True,
        network=SolanaNetwork.MAINNET_BETA
    )
    for token_holding in token_holdings:
        print(f"Token Holding: {token_holding}")


if __name__ == '__main__':
    example()
