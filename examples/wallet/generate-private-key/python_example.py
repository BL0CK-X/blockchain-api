from theblockchainapi import BlockchainAPIResource, Blockchain, BlockchainNetwork, Wallet, AvalancheChain
import json

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None

# ------ If using Solana..
BLOCKCHAIN = Blockchain.SOLANA

NETWORK = BlockchainNetwork.SolanaNetwork.MAINNET_BETA
# NETWORK = BlockchainNetwork.SolanaNetwork.DEVNET

DERIVATION_PATH = 'm/44/501/0/0'  # Used for Phantom, Sollet
# You can increment it for the next wallet in Phantom (e.g., what happens when you create a new wallet)
# DERIVATION_PATH = 'm/44/501/1/0'
# DERIVATION_PATH = None  # Defaults to 'm/44/501/0/0'
# DERIVATION_PATH = ""  # Use this if you created the wallet via the CLI

# ------ If using Ethereum..
# BLOCKCHAIN = Blockchain.ETHEREUM

# NETWORK = BlockchainNetwork.EthereumNetwork.MAINNET
# NETWORK = BlockchainNetwork.EthereumNetwork.ROPSTEN

# DERIVATION_PATH = None  # Use `None` for Metamask, the default

# ------ OR....
# BLOCKCHAIN = Blockchain.NEAR
# NETWORK = BlockchainNetwork.NearNetwork.MAINNET
#
# BLOCKCHAIN = Blockchain.BINANCE
# NETWORK = BlockchainNetwork.BinanceNetwork.MAINNET
#
# BLOCKCHAIN = Blockchain.AVALANCHE
# AVALANCHE_CHAIN = AvalancheChain.X
# NETWORK = BlockchainNetwork.AvalancheNetwork.MAINNET


BLOCKCHAIN_API_RESOURCE = BlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY,
    blockchain=BLOCKCHAIN,
    network=NETWORK,
    # avalanche_chain=AVALANCHE_CHAIN
)


def example():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    private_key = BLOCKCHAIN_API_RESOURCE.generate_private_key()

    if BLOCKCHAIN.value == Blockchain.SOLANA.value:
        b58_private_key = private_key['b58_private_key']
        print("This is a base58-encoded private key. This is what Phantom shows when you click `Show Private Key`")
        print(b58_private_key)

        print("-" * 20)

        private_key = private_key['private_key']
        print("This is a standard private key array. This is what SolFlare shows when you click `Export Private Key`")
        print(private_key)

        # You can now initialize `Wallet`, which can be used to create an NFT, transfer SOL, etc.
        # See the other examples.
        _ = Wallet(b58_private_key=b58_private_key)
        _ = Wallet(private_key=private_key)

    else:
        hex_private_key = private_key['hex_private_key']
        print("This is a standard private key. You can import this into Metamask.")
        print(hex_private_key)

        # You can now initialize `Wallet`, which can be used to create an NFT, transfer SOL, etc.
        # See the other examples.
        _ = Wallet(hex_private_key=hex_private_key)


if __name__ == '__main__':
    example()
