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

    my_secret_phrase = 'sadness swap zebra path panda power finger robot yellow game list enemy'

    # An NFT on mainnet-beta
    # https://explorer.solana.com/address/7EWJNaNYfPYMaqzdAAa4ps5kpqW95B7VHsjhW1kr18sj
    nft_address = '7EWJNaNYfPYMaqzdAAa4ps5kpqW95B7VHsjhW1kr18sj'
    associated_token_address = BLOCKCHAIN_API_RESOURCE.derive_associated_token_account_address(
        token_address=nft_address,
        secret_recovery_phrase=my_secret_phrase,
        network=SolanaNetwork.MAINNET_BETA
    )
    print(associated_token_address)

    # An NFT on devnet
    # https://explorer.solana.com/address/FmKrVEUKqnpQwGX5kbxR4HB5GZuZaGFdwKkhAKUKC5zA?cluster=devnet
    nft_address = 'FmKrVEUKqnpQwGX5kbxR4HB5GZuZaGFdwKkhAKUKC5zA'
    associated_token_address = BLOCKCHAIN_API_RESOURCE.derive_associated_token_account_address(
        token_address=nft_address,
        secret_recovery_phrase=my_secret_phrase,
        network=SolanaNetwork.DEVNET
    )
    print(associated_token_address)

    # You can also use this for non-NFTs, such as any other token.
    # Take Serum for example: https://explorer.solana.com/address/SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt
    serum_token_address = "SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt"
    associated_token_address = BLOCKCHAIN_API_RESOURCE.derive_associated_token_account_address(
        token_address=serum_token_address,
        secret_recovery_phrase=my_secret_phrase,
        network=SolanaNetwork.MAINNET_BETA
    )
    print(associated_token_address)


if __name__ == '__main__':
    example()
