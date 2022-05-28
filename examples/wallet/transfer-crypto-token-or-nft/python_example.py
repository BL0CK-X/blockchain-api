from theblockchainapi import TheBlockchainAPIResource, SolanaCurrencyUnit, SolanaNetwork, SolanaWallet, DerivationPath

# Get an API key pair for free here: https://dashboard.blockchainapi.com/
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
    secret_recovery_phrase = BLOCKCHAIN_API_RESOURCE.generate_secret_key()
    wallet = SolanaWallet(
        secret_recovery_phrase=secret_recovery_phrase,
        derivation_path=DerivationPath.CLI_PATH,
        passphrase=str(),
        private_key=None,  # OR You can supply this instead. e.g, [11, 234, ... 99, 24]
        b58_private_key=None  # OR You can supply this instead. e.g, x12x0120jd ... 192j0eds
    )
    public_key = BLOCKCHAIN_API_RESOURCE.derive_public_key(wallet=wallet)
    print(f"Public Key: {public_key}")
    print(f"Secret Recovery Phrase: {secret_recovery_phrase}")

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
    transfer_to = "8UmhEzc1CGkYazNQcGHvAAgTw9vy8mfBb5z4huyeftxc"

    # Call the transfer endpoint
    transaction_signature = BLOCKCHAIN_API_RESOURCE.transfer(
        wallet=wallet,
        recipient_address=transfer_to,
        amount=amount_to_send,
        network=SolanaNetwork.DEVNET,

        # Set the fee payer if you want someone else to pay the fee.
        # fee_payer_wallet=SolanaWallet(b58_private_key='INSERT FEE PAYER PRIVATE KEY'),

        # If you don't want to send private keys, define the `sender_public_key` and set `return_compiled_transaction`
        # to `True`. This will return instructions that you can sign and then send as a transaction.
        # sender_public_key='insert public key',
        # return_compiled_transaction=True  # default is False
    )

    print("Transferred!")
    print(f"You can view the transaction here: https://explorer.solana.com/tx/{transaction_signature}?cluster=devnet")

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
