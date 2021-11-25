from theblockchainapi import TheBlockchainAPIResource, SolanaMintAddresses, SolanaNetwork

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

    # (1) Test get SOL balance
    # Create a new wallet, get an airdrop, and then get its balance
    secret_key = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    print(secret_key)
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(secret_key)
    print(public_key)
    airdrop_tx_signature = BLOCKCHAIN_API_RESOURCE.get_airdrop(public_key)
    print(airdrop_tx_signature)
    result = BLOCKCHAIN_API_RESOURCE.get_balance(public_key)
    print(f"SOL Balance of {public_key}")
    print(result)

    # (2) Test get USDC balance (or any other SPL token)
    # This is the public key of a wallet on Solana: GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ
    # We know this public key has some amount of USDC in it already
    public_key = 'GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ'
    result = BLOCKCHAIN_API_RESOURCE.get_balance(
        public_key=public_key,
        mint_address=SolanaMintAddresses.USDC_MAINNET_BETA,  # or replace your own mint address
        network=SolanaNetwork.MAINNET_BETA
    )
    print("-" * 20)
    print(f"USDC Balance of {public_key}")
    print(result)


if __name__ == '__main__':
    example()
