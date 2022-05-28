from theblockchainapi import TheBlockchainAPIResource, SolanaMintAddresses, SolanaNetwork, SolanaWallet

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

    # (1) Test get SOL balance
    # Create a new wallet, get an airdrop, and then get its balance
    secret_phrase = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    print(secret_phrase)
    wallet = SolanaWallet(secret_recovery_phrase=secret_phrase)
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(wallet=wallet)
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

    # (3) Get the balance of an NFT
    # We have an NFT: 4zH3Rwm1QXdfTSUqsYmeUBY4QqQmQEXJVbv4ErSK736Q
    # We know that the public key GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ DOES NOT OWN this NFT.
    # We know that the public key 31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj OWNS this NFT.
    nft_address = '4zH3Rwm1QXdfTSUqsYmeUBY4QqQmQEXJVbv4ErSK736Q'

    public_key = 'GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ'
    result = BLOCKCHAIN_API_RESOURCE.get_balance(
        public_key=public_key,
        mint_address=nft_address,  # or replace your own mint address
        network=SolanaNetwork.MAINNET_BETA
    )
    print("-" * 20)
    print(f"Balance of {public_key} should be 0 because they do NOT own the NFT...")
    print(result)

    public_key = '31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj'
    result = BLOCKCHAIN_API_RESOURCE.get_balance(
        public_key=public_key,
        mint_address=nft_address,  # or replace your own mint address
        network=SolanaNetwork.MAINNET_BETA
    )
    print("-" * 20)
    print(f"Balance of {public_key} should be 1 because they do NOT own the NFT...")
    print(result)


if __name__ == '__main__':
    example()
