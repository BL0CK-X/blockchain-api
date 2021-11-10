from theblockchainapi import TheBlockchainAPIResource, SolanaCurrencyUnit, SolanaNetwork

# Get an API key pair for free here: https://dashboard.theblockchainapi.com/
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
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
    secret_key = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(
        secret_recovery_phrase=secret_key
    )
    print(f"Public Key: {public_key}")
    print(f"Secret Key: {secret_key}")

    # Get an airdrop on the devnet in order to be able to transfer SOL
    BLOCKCHAIN_API_RESOURCE.get_airdrop(public_key)

    # We need to make sure this has time to process before transferring SOL
    import time
    time.sleep(25)

    def get_balance():
        balance_result = BLOCKCHAIN_API_RESOURCE.get_balance(
            public_key,
            unit=SolanaCurrencyUnit.SOL,
            network=SolanaNetwork.DEVNET
        )
        print(f"Balance: {balance_result['balance']}")

    # Get the balance after the airdrop
    get_balance()

    # *** >>> TRANSFER THE SOL AIRDROP
    # You can put your address in the `transfer_to` and receive the SOL on the devnet.
    # You can view it in your Phantom wallet by going to Settings > Change Network > Devnet and then viewing
    # your SOL balance.

    # This is the amount we received in SOL from the Airdrop
    airdrop_amount = 0.015
    transfer_fee = 0.000005

    # We cannot send `airdrop_amount` because we need to pay for the transaction, and so we wouldn't have enough to
    # pay for the transaction because our balance would be `0` after sending `airdrop_amount` yet we still need to cover
    # the transaction.
    amount_to_send = str(airdrop_amount - transfer_fee)

    # Transfer to this address
    transfer_to = "31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj"

    # Call the transfer endpoint
    transaction_signature = BLOCKCHAIN_API_RESOURCE.transfer(
        secret_recovery_phrase=secret_key,
        recipient_address=transfer_to,
        amount=amount_to_send,
        network=SolanaNetwork.DEVNET
    )
    print(transaction_signature)

    # The output of this `get_balance()` call should be `airdrop_amount` less
    # than the previous output of `get_balance()`
    get_balance()


if __name__ == '__main__':
    """
    Example Output:
    
    Public Key: 8vTgbAEVnh2RAP85njYmcSUAjYCBqbkZ638VsgJYbCve
    Secret Key: tattoo step foot essence amused marble slim access fiction lamp dawn talent
    Balance: 0.015
    5pWrB5SKoSAAfFqVFvvhyoUnxJGdY9gBQtuEbevVRgEHWybKGjBb7HfJXJVMM8xSijJ56EdoSohDGtmxzjuQpW46
    Balance: 0.0
    """
    example()
