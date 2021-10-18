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

    mint_fee_response = BLOCKCHAIN_API_RESOURCE.get_nft_mint_fee()
    print("Lamport Fee:", mint_fee_response['nft_mint_fee_estimate_lamports'])
    print("Fee Description:", mint_fee_response['description'])


if __name__ == '__main__':
    example()
