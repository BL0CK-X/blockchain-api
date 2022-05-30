from theblockchainapi import BlockchainAPIResource, Blockchain, BlockchainNetwork
import json

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None

BLOCKCHAIN = Blockchain.SOLANA
NETWORK = BlockchainNetwork.SolanaNetwork.MAINNET_BETA
# NETWORK = BlockchainNetwork.SolanaNetwork.DEVNET

# BLOCKCHAIN = Blockchain.ETHEREUM
# NETWORK = BlockchainNetwork.EthereumNetwork.MAINNET
# NETWORK = BlockchainNetwork.EthereumNetwork.ROPSTEN

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

    rpc_url = BLOCKCHAIN_API_RESOURCE.get_rpc_url()

    print(
        f"You can use this RPC URL for `{BLOCKCHAIN.value}`, `{NETWORK.value}`; "
        f"but make sure to include your API keys in the headers. \n\n {rpc_url}"
    )

    rpc_response = BLOCKCHAIN_API_RESOURCE.make_rpc_request(
        method='getBlockTime',
        params=[
            135659086
        ]
    )

    # In progress....
    print(rpc_response)
    print(json.dumps(rpc_response, indent=4))


if __name__ == '__main__':
    example()
