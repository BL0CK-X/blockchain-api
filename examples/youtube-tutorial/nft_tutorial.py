import requests
import json

NFT_URI = "https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F6097d" \
          "7ee81957044af68d9ce%2FSNL%2F960x0.jpg%3Ffit%3Dscale"
NFT_NAME = "Wario Musk"
NFT_SYMBOL = "WARIO"
NFT_DESCRIPTION = "The ONLY Wario NFT!"
NFT_METADATA = {
    "cleverness": 100,
    "intelligence": 100,
    "musk": 99,
    "warioness": 98
}

KEY_ID = "eadJIWYqwP8EYYG"
SECRET_KEY = "o1nwup684SErtO6"
HEADERS = {
    "APIKeyID": KEY_ID,
    "APISecretKey": SECRET_KEY
}


SECRET_PHRASE_ENDPOINT = "https://api.theblockchainapi.com/v1/solana/wallet/secret_recovery_phrase"
PUBLIC_KEY_ENDPOINT = "https://api.theblockchainapi.com/v1/solana/wallet/public_key"
BALANCE_ENDPOINT = "https://api.theblockchainapi.com/v1/solana/wallet/balance"
NFT_MINT_FEE_ENDPOINT = "https://api.theblockchainapi.com/v1/solana/nft/mint/fee"
NFT_ENDPOINT = "https://api.theblockchainapi.com/v1/solana/nft"

SECRET_PHRASE = "critic summer impact weasel muscle couch into nuclear sibling clip dignity multiply"
DERIVATION_PATH = ""

PUBLIC_KEY = "DMjPKvEjRSA8rbCemvvojactQVuBPXwTVeifQad3h7yC"

EXAMPLE_MINT_NFT_RESPONSE = {
    'mint_address': 'HBJcGkVuZhaLhvMA8df4p7swdisCcNAQocNS7zfYKH7U',
    'mint_secret_recovery_phrase': 'ice arrive clown other soccer main orange calm aspect toward hammer modify',
    'name': 'Wario Musk',
    'symbol': 'WARIO',
    'update_authority_address': 'DMjPKvEjRSA8rbCemvvojactQVuBPXwTVeifQad3h7yC',
    'uri': 'https://blockx-api-storage.s3.amazonaws.com/67845517719/data.txt'
}


def get_secret_phrase():
    response = requests.post(
        SECRET_PHRASE_ENDPOINT,
        headers=HEADERS
    )
    print(response.json())


def derive_public_key():
    response = requests.post(
        PUBLIC_KEY_ENDPOINT,
        params={
            "derivation_path": DERIVATION_PATH,
            "secret_recovery_phrase": SECRET_PHRASE
        },
        headers=HEADERS
    )
    print(response.json())


def get_balance():
    response = requests.get(
        BALANCE_ENDPOINT,
        params={
            "public_key": PUBLIC_KEY
        },
        headers=HEADERS
    )
    print(response.json())


def get_nft_mint_fee():
    response = requests.get(
        NFT_MINT_FEE_ENDPOINT,
        headers=HEADERS
    )
    print(response.json())


if __name__ == '__main__':
    # Create the NFT!
    mint_nft_response = requests.post(
        NFT_ENDPOINT,
        params={
            "derivation_path": DERIVATION_PATH,
            "secret_recovery_phrase": SECRET_PHRASE,
            "nft_name": NFT_NAME,
            "nft_symbol": NFT_SYMBOL,
            "nft_description": NFT_DESCRIPTION,
            "nft_url": NFT_URI,
            "nft_metadata": json.dumps(NFT_METADATA),
            "network": "devnet",
            "nft_upload_method": "S3"
        },
        headers=HEADERS
    )
    print(mint_nft_response.json())
