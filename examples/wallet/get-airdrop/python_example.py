from theblockchainapi import BlockchainAPIResource, Blockchain, BlockchainNetwork, Wallet, AvalancheChain, CurrencyUnit
import json

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None

# ------ If using Solana..
# BLOCKCHAIN = Blockchain.SOLANA
#
# NETWORK = BlockchainNetwork.SolanaNetwork.MAINNET_BETA
# UNIT = CurrencyUnit.SolanaCurrencyUnit.SOL
# # NETWORK = BlockchainNetwork.SolanaNetwork.DEVNET
#
# DERIVATION_PATH = 'm/44/501/0/0'  # Used for Phantom, Sollet
# You can increment it for the next wallet in Phantom (e.g., what happens when you create a new wallet)
# DERIVATION_PATH = 'm/44/501/1/0'
# DERIVATION_PATH = None  # Defaults to 'm/44/501/0/0'
# DERIVATION_PATH = ""  # Use this if you created the wallet via the CLI

# ------ If using Ethereum..
BLOCKCHAIN = Blockchain.ETHEREUM
UNIT = CurrencyUnit.EthereumCurrencyUnit.ETH

# NETWORK = BlockchainNetwork.EthereumNetwork.MAINNET
NETWORK = BlockchainNetwork.EthereumNetwork.ROPSTEN

# DERIVATION_PATH = None  # Use `None` for Metamask, the default

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

    # Create a wallet
    secret_phrase = BLOCKCHAIN_API_RESOURCE.generate_seed_phrase()

    wallet = Wallet(
        secret_recovery_phrase=secret_phrase
    )

    blockchain_identifier = BLOCKCHAIN_API_RESOURCE.derive_blockchain_identifier(wallet=wallet)
    print(f"Wallet Identifier: {blockchain_identifier}")
    print(f"Secret Phrase: {secret_phrase}")

    # Check the balance before
    balance_result = BLOCKCHAIN_API_RESOURCE.get_balance(blockchain_identifier, unit=UNIT)
    print(f"Balance Before Airdrop: {balance_result['balance']}")

    # Get an airdrop on the devnet in order to be able to mint an NFT
    result = BLOCKCHAIN_API_RESOURCE.get_airdrop(blockchain_identifier)
    print(f"Transaction Signature: {result}")
    if BLOCKCHAIN.value == Blockchain.SOLANA.value:
        print(f"View Transaction: https://explorer.solana.com/tx/{result}?cluster=devnet")
    else:
        print(f"View Transaction: https://ropsten.etherscan.io/tx/{result}")

    # Check the balance after
    balance_result = BLOCKCHAIN_API_RESOURCE.get_balance(blockchain_identifier, unit=UNIT)
    print(f"Balance After Airdrop: {balance_result['balance']}")


if __name__ == '__main__':
    example()
