from theblockchainapi import BlockchainAPIResource, Blockchain, BlockchainNetwork
import json

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None


SOLANA_BLOCKCHAIN_API_RESOURCE = BlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY,
    blockchain=Blockchain.SOLANA,
    network=BlockchainNetwork.SolanaNetwork.MAINNET_BETA
)

ETHEREUM_BLOCKCHAIN_API_RESOURCE = BlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY,
    blockchain=Blockchain.ETHEREUM,
    network=BlockchainNetwork.EthereumNetwork.MAINNET
)


def example():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    usdc_on_solana = SOLANA_BLOCKCHAIN_API_RESOURCE.get_token_metadata(
        token_blockchain_identifier="EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
    )

    usdt_on_ethereum = ETHEREUM_BLOCKCHAIN_API_RESOURCE.get_token_metadata(
        token_blockchain_identifier="0xdAC17F958D2ee523a2206206994597C13D831ec7"
    )

    print(f"Here's USDC on Solana: ", json.dumps(usdc_on_solana, indent=4, sort_keys=True))
    print("-" * 20)
    print(f"Here's USDT on Ethereum: ", json.dumps(usdt_on_ethereum, indent=4, sort_keys=True))


if __name__ == '__main__':
    example()
