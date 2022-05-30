from theblockchainapi import SolanaAPIResource, SolanaWallet

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
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

    my_secret_phrase = 'sadness swap zebra path panda power finger robot yellow game list enemy'

    wallet = SolanaWallet(
        derivation_path="m/44/501/0/0",
        secret_recovery_phrase=my_secret_phrase,
        passphrase=str()
    )

    # You can replace this with your public key here. Then you won't have to provide a seed phrase.
    my_public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(wallet=wallet)

    # An NFT on mainnet-beta
    # https://explorer.solana.com/address/7EWJNaNYfPYMaqzdAAa4ps5kpqW95B7VHsjhW1kr18sj
    nft_address = '7EWJNaNYfPYMaqzdAAa4ps5kpqW95B7VHsjhW1kr18sj'
    associated_token_address = BLOCKCHAIN_API_RESOURCE.get_associated_token_account_address(
        mint_address=nft_address,
        public_key=my_public_key
    )
    print(associated_token_address)

    # An NFT on devnet
    # https://explorer.solana.com/address/FmKrVEUKqnpQwGX5kbxR4HB5GZuZaGFdwKkhAKUKC5zA?cluster=devnet
    nft_address = 'FmKrVEUKqnpQwGX5kbxR4HB5GZuZaGFdwKkhAKUKC5zA'
    associated_token_address = BLOCKCHAIN_API_RESOURCE.get_associated_token_account_address(
        mint_address=nft_address,
        public_key=my_public_key
    )
    print(associated_token_address)

    # You can also use this for non-NFTs, such as any other token.
    # Take Serum for example: https://explorer.solana.com/address/SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt
    serum_token_address = "SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt"
    associated_token_address = BLOCKCHAIN_API_RESOURCE.get_associated_token_account_address(
        mint_address=serum_token_address,
        public_key=my_public_key
    )
    print(associated_token_address)


if __name__ == '__main__':
    example()
