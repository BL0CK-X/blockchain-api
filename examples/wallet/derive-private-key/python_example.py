from theblockchainapi import BlockchainAPIResource, Blockchain, BlockchainNetwork, Wallet, AvalancheChain

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

    # Shows how to get the second phantom wallet by changing the derivation path.
    wallet = Wallet(
        secret_recovery_phrase='sadness swap zebra path panda power finger robot yellow game list enemy',
        derivation_path=DERIVATION_PATH,
        passphrase=str(),
        private_key=None,  # OR You can supply this instead. e.g, [11, 234, ... 99, 24]
        b58_private_key=None  # OR You can supply this instead. e.g, x12x0120jd ... 192j0eds
    )
    public_key = BLOCKCHAIN_API_RESOURCE.derive_private_key(wallet=wallet)
    print(public_key)

    if BLOCKCHAIN.value == Blockchain.SOLANA.value:
        private_key = [14.0, 89.0, 130.0, 180.0, 6.0, 188.0, 214.0, 232.0, 110.0, 111.0, 168.0, 233.0, 193.0, 156.0, 80.0, 174.0, 53.0, 166.0, 203.0, 194.0, 233.0, 63.0, 104.0, 148.0, 169.0, 117.0, 86.0, 39.0, 114.0, 231.0, 78.0, 178.0, 255.0, 33.0, 247.0, 222.0, 140.0, 123.0, 73.0, 174.0, 232.0, 10.0, 198.0, 129.0, 106.0, 166.0, 124.0, 191.0, 75.0, 85.0, 221.0, 82.0, 145.0, 147.0, 51.0, 93.0, 171.0, 201.0, 203.0, 209.0, 18.0, 27.0, 35.0, 98.0]
        wallet = Wallet(
            private_key=private_key
        )
        public_key = BLOCKCHAIN_API_RESOURCE.derive_private_key(wallet=wallet)
        print(public_key)

        b58_private_key = 'He7kXDX1wXWvK5CppMmop3pwjE3k6pLdtbBnZbKCLU1CHLeXXxEoPLe8kjqbh54zWgGSstj1e9XtsE57WZLcQrd'
        wallet = Wallet(
            b58_private_key=b58_private_key
        )
        public_key = BLOCKCHAIN_API_RESOURCE.derive_private_key(wallet=wallet)
        print(public_key)
    else:
        pass


if __name__ == '__main__':
    example()
