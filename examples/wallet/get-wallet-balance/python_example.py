from theblockchainapi import BlockchainAPIResource, Blockchain, BlockchainNetwork, Wallet

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None

# BLOCKCHAIN = Blockchain.SOLANA
# NETWORK = BlockchainNetwork.SolanaNetwork.MAINNET_BETA
# # NETWORK = BlockchainNetwork.SolanaNetwork.DEVNET
# UNIT = 'sol'
# TEST_BLOCKCHAIN_IDENTIFIER = 'DbjWJmYbn4dA4atBJsMKpwM9R72z18HLJc8ws8ekDhmY'
# USDC_TOKEN_BLOCKCHAIN_IDENTIFIER = 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v'
# NFT_TOKEN_BLOCKCHAIN_IDENTIFIER = '4zH3Rwm1QXdfTSUqsYmeUBY4QqQmQEXJVbv4ErSK736Q'

BLOCKCHAIN = Blockchain.ETHEREUM
NETWORK = BlockchainNetwork.EthereumNetwork.MAINNET
# NETWORK = BlockchainNetwork.EthereumNetwork.ROPSTEN
UNIT = 'ether'
TEST_BLOCKCHAIN_IDENTIFIER = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'
USDC_TOKEN_BLOCKCHAIN_IDENTIFIER = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
NFT_TOKEN_BLOCKCHAIN_IDENTIFIER = '0x1542B05412Dfecd80E734929F9087f8766934275'


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

    # (1) Test get SOL/ETH balance
    # Create a new wallet, get an airdrop, and then get its balance
    secret_phrase = BLOCKCHAIN_API_RESOURCE.generate_seed_phrase()
    print(secret_phrase)
    wallet = Wallet(secret_recovery_phrase=secret_phrase)
    blockchain_identifier = BLOCKCHAIN_API_RESOURCE.derive_blockchain_identifier(wallet=wallet)
    print(blockchain_identifier)

    airdrop_tx_signature = BLOCKCHAIN_API_RESOURCE.get_airdrop(blockchain_identifier)
    print(airdrop_tx_signature)

    result = BLOCKCHAIN_API_RESOURCE.get_balance(blockchain_identifier, unit=UNIT)
    print(f"Balance of {blockchain_identifier}")
    print(result)

    # (2) Test get USDC balance (or any other SPL token)
    # This is the public key of a wallet on Solana: GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ
    # We know this public key has some amount of USDC in it already
    if BLOCKCHAIN.value == Blockchain.SOLANA.value:
        blockchain_identifier = 'GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ'
    else:
        blockchain_identifier = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'
    result = BLOCKCHAIN_API_RESOURCE.get_balance(
        blockchain_identifier=blockchain_identifier,
        token_blockchain_identifier=USDC_TOKEN_BLOCKCHAIN_IDENTIFIER  # or replace your own token blockchain identifier
    )
    print("-" * 20)
    print(f"USDC Balance of {blockchain_identifier}")
    print(result)

    # (3) Get the balance of an NFT
    # We have an NFT: 4zH3Rwm1QXdfTSUqsYmeUBY4QqQmQEXJVbv4ErSK736Q
    # We know that the public key GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ DOES NOT OWN this NFT.
    # We know that the public key 31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj OWNS this NFT.

    if BLOCKCHAIN.value == Blockchain.SOLANA.value:
        blockchain_identifier = 'GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ'
    else:
        blockchain_identifier = '0xE3Ad30ee62126ee4f82894683c7Eb5a42264b536'
    result = BLOCKCHAIN_API_RESOURCE.get_balance(
        blockchain_identifier=blockchain_identifier,
        token_blockchain_identifier=NFT_TOKEN_BLOCKCHAIN_IDENTIFIER,  # or replace your own token blockchain address
    )
    print("-" * 20)
    print(f"Balance of {blockchain_identifier} should be 0 because they do NOT own the NFT...")
    print(result)

    if BLOCKCHAIN.value == Blockchain.SOLANA.value:
        blockchain_identifier = '31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj'
    else:
        blockchain_identifier = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045'
    result = BLOCKCHAIN_API_RESOURCE.get_balance(
        blockchain_identifier=blockchain_identifier,
        token_blockchain_identifier=NFT_TOKEN_BLOCKCHAIN_IDENTIFIER
    )
    print("-" * 20)
    print(f"Balance of {blockchain_identifier} should be 1 because they do NOT own the NFT...")
    print(result)


if __name__ == '__main__':
    example()
