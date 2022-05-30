from theblockchainapi import BlockchainAPIResource, Blockchain, BlockchainNetwork
import json

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None

# This function is only supported for Solana at the moment...
BLOCKCHAIN = Blockchain.SOLANA
NETWORK = BlockchainNetwork.SolanaNetwork.MAINNET_BETA
# NETWORK = BlockchainNetwork.SolanaNetwork.DEVNET

BLOCKCHAIN_API_RESOURCE = BlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY,
    blockchain=BLOCKCHAIN,
    network=NETWORK
)


def example():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    all_tokens = BLOCKCHAIN_API_RESOURCE.get_all_tokens()

    print(f"There are {len(all_tokens)} tokens.")

    print(f"Here's one: ", json.dumps(all_tokens[0], indent=4, sort_keys=True))


if __name__ == '__main__':
    example()
