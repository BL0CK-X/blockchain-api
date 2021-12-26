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

    nft_mint_address = None

    # Yes, minted with a V1 candy machine.
    try:
        nft_mint_address = "4YmE6xzXAQ1HccBbzMgJh6NLn643ySrt1iXShUibrAsB"
        result = BLOCKCHAIN_API_RESOURCE.get_candy_machine_id_from_nft(
            mint_address=nft_mint_address,
            network=SolanaNetwork.MAINNET_BETA
        )
        print("Candy Machine ID:", result['candy_machine_id'])
        print("Candy Machine Version:", result['candy_machine_contract_version'])
    except Exception as e:
        print(str(e))

    # Yes, minted with a V2 candy machine.
    try:
        nft_mint_address = "63k8TCFNfQigyCfR4hvZg5moHZQ2uJYnfsuoDnrjHyeb"
        result = BLOCKCHAIN_API_RESOURCE.get_candy_machine_id_from_nft(
            mint_address=nft_mint_address,
            network=SolanaNetwork.MAINNET_BETA
        )
        print("Candy Machine ID:", result['candy_machine_id'])
        print("Candy Machine Version:", result['candy_machine_contract_version'])
    except Exception as e:
        print(str(e))

    # No, not minted with a candy machine ID.
    try:
        nft_mint_address = "GoxY1RhbuVwvQAWJ9DMT2PZWNJR6peQCy8cuKJHvb44e"
        result = BLOCKCHAIN_API_RESOURCE.get_candy_machine_id_from_nft(
            mint_address=nft_mint_address,
            network=SolanaNetwork.MAINNET_BETA
        )
        print("Candy Machine ID:", result['candy_machine_id'])
        print("Candy Machine Version:", result['candy_machine_contract_version'])
    except Exception as e:
        print(f"Error Retrieving Candy Machine ID for {nft_mint_address}:", str(e))


if __name__ == '__main__':
    example()
