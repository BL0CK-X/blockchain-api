from theblockchainapi import BlockchainAPIResource, Blockchain, BlockchainNetwork
import json

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None

# This function is only supported for Ethereum at the moment...
BLOCKCHAIN = Blockchain.ETHEREUM
NETWORK = BlockchainNetwork.EthereumNetwork.MAINNET
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

    blockchain_identifier = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'

    name = BLOCKCHAIN_API_RESOURCE.get_name_from_blockchain_identifier(blockchain_identifier)

    print(f"The ENS of `{blockchain_identifier}` is {name}.")


if __name__ == '__main__':
    example()
