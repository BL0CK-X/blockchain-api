from theblockchainapi import TheBlockchainAPIResource, SolanaMintAddresses, SolanaNetwork

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
    secret_key = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    print(secret_key)
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(secret_key)
    print(public_key)
    result = BLOCKCHAIN_API_RESOURCE.get_balance(public_key)
    print(result)

    # This is the public key of a wallet on Solana: GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ
    # We know this public key has some amount of USDC in it already
    public_key = 'GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ'
    result = BLOCKCHAIN_API_RESOURCE.get_balance(
        public_key=public_key,
        mint_address=SolanaMintAddresses.USDC_MAINNET_BETA,
        network=SolanaNetwork.MAINNET_BETA
    )
    print("-" * 20)
    print(f"Balance of {public_key}")
    print(result)


if __name__ == '__main__':
    example()
