from theblockchainapi import SolanaAPIResource, SolanaCurrencyUnit, SolanaWallet

# Get an API key pair for free here: https://dashboard.blockchainapi.com/api-keys
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None

BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)


def example():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    # Create a wallet
    secret_phrase = BLOCKCHAIN_API_RESOURCE.generate_secret_key()

    wallet = SolanaWallet(
        secret_recovery_phrase=secret_phrase
    )

    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(wallet=wallet)
    print(f"Public Key: {public_key}")
    print(f"Secret Phrase: {secret_phrase}")

    # Check the balance before
    balance_result = BLOCKCHAIN_API_RESOURCE.get_balance(public_key, unit=SolanaCurrencyUnit.SOL)
    print(f"Balance Before Airdrop: {balance_result['balance']}")

    # Get an airdrop on the devnet in order to be able to mint an NFT
    result = BLOCKCHAIN_API_RESOURCE.get_airdrop(public_key)
    print(f"Transaction Signature: {result}")
    print(f"View Transaction: https://explorer.solana.com/tx/{result}?cluster=devnet")

    # Check the balance after
    balance_result = BLOCKCHAIN_API_RESOURCE.get_balance(public_key, unit=SolanaCurrencyUnit.SOL)
    print(f"Balance After Airdrop: {balance_result['balance']}")


if __name__ == '__main__':
    example()
