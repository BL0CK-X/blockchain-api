from theblockchainapi import TheBlockchainAPIResource, SolanaCurrencyUnit, SolanaNFTUploadMethod, SolanaNetwork

# Get an API key pair for free here: https://dashboard.theblockchainapi.com/
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)


def example():
    """
    This example creates a new wallet, gets an airdrop to mint an NFT, and then mints an NFT.
    """
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    # Create a wallet
    secret_key = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    derivation_path = str()
    pass_phrase = str()
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(
        secret_recovery_phrase=secret_key,
        derivation_path=derivation_path,
        passphrase=derivation_path
    )
    print(f"Public Key: {public_key}")
    print(f"Secret Key: {secret_key}")

    # Get an airdrop on the devnet in order to be able to mint an NFT
    BLOCKCHAIN_API_RESOURCE.get_airdrop(public_key)

    # We need to make sure the airdrops have time to process before minting the NFT!
    import time
    time.sleep(30)

    def get_balance():
        balance_result = BLOCKCHAIN_API_RESOURCE.get_balance(
            public_key,
            unit=SolanaCurrencyUnit.SOL,
            network=SolanaNetwork.DEVNET
        )
        print(f"Balance: {balance_result['balance']}")
    get_balance()

    # Mint an NFT
    nft = BLOCKCHAIN_API_RESOURCE.create_nft(
        secret_recovery_phrase=secret_key,
        derivation_path=derivation_path,
        passphrase=pass_phrase,
        nft_name="The Blockchain API",
        nft_symbol="BLOCKX",
        nft_url="https://pbs.twimg.com/profile_images/1441903262509142018/_8mjWhho_400x400.jpg",
        nft_upload_method=SolanaNFTUploadMethod.S3,
        network=SolanaNetwork.DEVNET,
        nft_description="An NFT of the Blockchain API logo",
        creators=[
            public_key,
            "31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj",
            "G17UmNGnMJ851x3M1JXocgpft1afcYedjPuFpo1ohhCk"
        ],
        share=[10, 70, 20],
        seller_fee_basis_points=100,
        is_mutable=False,
        is_master_edition=True
    )
    print("NFT: ", nft)
    print(f"You can view the NFT here: {nft['explorer_url']}")


if __name__ == '__main__':
    example()
    """
    The output will look something like this:
    
    Public Key: 7fSX9LCMmA39N1Kfbwemxzw1nswnohuzhAJqa7ntr5jg
    Secret Key: vast consider vague machine economy crystal dose ivory autumn notice master furnace
    Balance: 0.015
    NFT:  {
            'update_authority': '7fSX9LCMmA39N1Kfbwemxzw1nswnohuzhAJqa7ntr5jg',
            'mint': '9FSVv9ey1bTKNfwAVVR4DDSMML5fhb1HVaMbf1dHYALf',
            'data': {
                'name': 'The Blockchain API',
                'symbol': 'BLOCKX',
                'uri': 'https://blockx-api-storage.s3.amazonaws.com/89360005839/data',
                'seller_fee_basis_points': 100.0, 
                'creators': [
                    '7fSX9LCMmA39N1Kfbwemxzw1nswnohuzhAJqa7ntr5jg', 
                    '31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj', 
                    'G17UmNGnMJ851x3M1JXocgpft1afcYedjPuFpo1ohhCk'
                ], 
                'verified': [1.0, 0.0, 0.0], 
                'share': [10.0, 70.0, 20.0]
            }, 
            'primary_sale_happened': False, 
            'is_mutable': False, 
            'explorer_url': 
                'https://explorer.solana.com/address/9FSVv9ey1bTKNfwAVVR4DDSMML5fhb1HVaMbf1dHYALf?cluster=devnet', 
            'mint_secret_recovery_phrase': 
            'have lawsuit slide discover round slot want quick sword false economy crumble'
        }
    You can view the NFT here: 
        https://explorer.solana.com/address/9FSVv9ey1bTKNfwAVVR4DDSMML5fhb1HVaMbf1dHYALf?cluster=devnet
    """
