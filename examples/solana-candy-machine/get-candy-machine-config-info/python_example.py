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

    the_goat_society_candy_machine_id = "9htmDvW58pjCMQdjFbovo8cGBZviDfeP3j7DKnikHEy5"

    # First, get the candy machine config public key
    candy_machine_data = BLOCKCHAIN_API_RESOURCE.get_candy_machine_info(
        candy_machine_id=the_goat_society_candy_machine_id,
        network=SolanaNetwork.MAINNET_BETA
    )
    print(f"Candy Machine Info: {candy_machine_data}")

    config_address = candy_machine_data['config_address']
    print(f"Config Address: {config_address}")

    candy_machine_data = BLOCKCHAIN_API_RESOURCE.get_config_details(
        config_address=config_address,
        network=SolanaNetwork.MAINNET_BETA
    )
    print(f"Candy Machine Configuration: {candy_machine_data}")


if __name__ == '__main__':
    example()
