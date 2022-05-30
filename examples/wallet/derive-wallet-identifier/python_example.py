from theblockchainapi import BlockchainAPIResource, Blockchain, BlockchainNetwork, Wallet, AvalancheChain

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None

# ------ If using Solana..
BLOCKCHAIN = Blockchain.SOLANA

NETWORK = BlockchainNetwork.SolanaNetwork.MAINNET_BETA
# NETWORK = BlockchainNetwork.SolanaNetwork.DEVNET

# DERIVATION_PATH = 'm/44/501/0/0'  # Used for Phantom, Sollet
# You can increment it for the next wallet in Phantom (e.g., what happens when you create a new wallet)
# DERIVATION_PATH = 'm/44/501/1/0'
DERIVATION_PATH = None  # Defaults to 'm/44/501/0/0'
# DERIVATION_PATH = ""  # Use this if you created the wallet via the CLI

# ------ If using Ethereum..
BLOCKCHAIN = Blockchain.ETHEREUM

NETWORK = BlockchainNetwork.EthereumNetwork.MAINNET
# NETWORK = BlockchainNetwork.EthereumNetwork.ROPSTEN

# DERIVATION_PATH = None  # Use `None` for Metamask, the default

# ------ OR....
BLOCKCHAIN = Blockchain.NEAR
NETWORK = BlockchainNetwork.NearNetwork.MAINNET

# BLOCKCHAIN = Blockchain.BINANCE
# NETWORK = BlockchainNetwork.BinanceNetwork.MAINNET

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

    # Retrieve a public key from a seed phrase and the derivation path that the CLI uses.
    wallet = Wallet(
        secret_recovery_phrase='sadness swap zebra path panda power finger robot yellow game list enemy',
        derivation_path=DERIVATION_PATH,
        passphrase=str(),
        private_key=None,  # OR You can supply this instead. e.g, [11, 234, ... 99, 24]
        b58_private_key=None,  # OR You can supply this instead. e.g, x12x0120jd ... 192j0eds
        hex_private_key=None  # OR You can supply this instead. e.g., 0x2e89a59b6a2....0ef0513aa38b0d39b3a
    )
    blockchain_identifier = BLOCKCHAIN_API_RESOURCE.derive_blockchain_identifier(wallet=wallet)
    print(blockchain_identifier)


if __name__ == '__main__':
    example()
