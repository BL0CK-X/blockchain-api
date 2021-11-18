from theblockchainapi import TheBlockchainAPIResource

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
        
    # Default uses the Phantom Derivation path
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(
        secret_recovery_phrase='sadness swap zebra path panda power finger robot yellow game list enemy',
    )
    print(public_key)
    
    # Use an empty string to use the CLI derivation path 
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(
        secret_recovery_phrase='sadness swap zebra path panda power finger robot yellow game list enemy',
        derivation_path=''
    )
    print(public_key)


if __name__ == '__main__':
    example()
