from theblockchainapi import TheBlockchainAPIResource
import json
import requests

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

    collection_data_url = \
        'https://raw.githubusercontent.com/BL0CK-X/solana-nft-collection-mint-addresses/main/collections.json'
    mint_addresses = requests.get(collection_data_url).json()['solana_money_boys']
    start_time = None  # Default start time is 1 day ago. Provide -1 to get full history (since we began recording it).
    end_time = None

    print(f"Retrieved {len(mint_addresses)} mint addresses.")

    analytics = BLOCKCHAIN_API_RESOURCE.get_nft_marketplace_analytics(
        mint_addresses=mint_addresses,
        start_time=start_time,
        end_time=end_time
    )

    print(f"NFT Transactions: {json.dumps(analytics, indent=4)}")
    print(f"Floor = {analytics['floor']}")
    print(f"Volume = {analytics['volume']}")


if __name__ == '__main__':
    example()

    """
    OUTPUT: 
    
    Floor = 13900000000.0
    Volume = 13000000000.0
    NFT Transactions: {
        "22oPvMQkpdMpJ6KJ3WPYH8CLBS3Qd62WTjw9ugqrfaAt": [
            {
                "block_time": 1644424948.0,
                "exchange": "magic-eden",
                "exchange_readable": "Magic Eden",
                "mint_address": "22oPvMQkpdMpJ6KJ3WPYH8CLBS3Qd62WTjw9ugqrfaAt",
                "operation": "list",
                "price": 12890000000.0,
                "seller": "4n1ZGL8QdnsjR6hK94CsmAm8y3VBVShScbqtps1fYUDq",
                "transaction_signature": "4a7ddfKezfUgWPxYLPJaYHpLNmSWA11ZshLnp7PEShoiY3teEQVD4YeAfbNuhqZRRAwCiNsY9mnEGBteeb4LkVrt"
            }
        ],
        "7tGEAXH2xWnqTDfKpQwMijFfpunAitkonLsFNPN51TsE": [
            {
                "block_time": 1644423545.0,
                "exchange": "magic-eden",
                "exchange_readable": "Magic Eden",
                "mint_address": "7tGEAXH2xWnqTDfKpQwMijFfpunAitkonLsFNPN51TsE",
                "operation": "list",
                "price": 13300000000.0,
                "seller": "5zHguARCXyjikKoPA4zoZXsoXB2jvUnHH54E82hPewj4",
                "transaction_signature": "v3f3ibPwjcyLJqDUKA3NpXFJEvqR6ugvpdaUvuw9R6vv3f1hKRB2hu5wx7Tqyk1W4c9CprE13zsfPbi9M9XHcpP"
            }
        ],
        "CD8awfGuU4fkFAwKTbb94zcMi41V7bmxdFiFRu1xTEZn": [
            {
                "block_time": 1644424903.0,
                "exchange": "magic-eden",
                "exchange_readable": "Magic Eden",
                "mint_address": "CD8awfGuU4fkFAwKTbb94zcMi41V7bmxdFiFRu1xTEZn",
                "operation": "list",
                "price": 13000000000.0,
                "seller": "EyWoDersP7ZZABUoFEAqLmiEYXofxoSSZuWy6WPHtrSY",
                "transaction_signature": "2FT6UEgtE3KeCKA7qPB3CYYvbTHBzSFVDm3Yt3MYQ2oGDk2J25jGQczNUwNhJkfkLfm7KXd6RxDWJcHLJAENwwX4"
            },
            {
                "block_time": 1644425012.0,
                "buyer": "Fs2vLonwL4KhmGsL9EeZr2dG5eHEXw6cPJHvAM2Ymmrk",
                "exchange": "magic-eden",
                "exchange_readable": "Magic Eden",
                "mint_address": "CD8awfGuU4fkFAwKTbb94zcMi41V7bmxdFiFRu1xTEZn",
                "operation": "buy",
                "price": 13000000000.0,
                "seller": "EyWoDersP7ZZABUoFEAqLmiEYXofxoSSZuWy6WPHtrSY",
                "transaction_signature": "3pgYbgZr9WS1u3zvkJQWVfyVG52GDtFavZ4gFWRLBDzZYbSpQkuGZNpttvg6hzr75fNcQG2WR6ZBrZDF5UWzSqz6"
            }
        ],
        "DjBRcfH83wPpZ5TQ9mJ1i7PzP4LbZ2gp7MhbDfdhJRng": [
            {
                "block_time": 1644381112.0,
                "exchange": "magic-eden",
                "exchange_readable": "Magic Eden",
                "mint_address": "DjBRcfH83wPpZ5TQ9mJ1i7PzP4LbZ2gp7MhbDfdhJRng",
                "operation": "list",
                "price": 14000000000.0,
                "seller": "H38kTeMY8aQSMN5sNhSuwHaur2Awj6XRi57CDwN2pUtG",
                "transaction_signature": "2TPn8C9qV1n6oCxgJjMkjwpZDp26g3KxQR8EKQDe4tUCGjp1aiekgJ93CywHzrKNRs1zmEkyhyEiezc2w6QKdB27"
            },
            {
                "block_time": 1644381618.0,
                "exchange": "magic-eden",
                "exchange_readable": "Magic Eden",
                "mint_address": "DjBRcfH83wPpZ5TQ9mJ1i7PzP4LbZ2gp7MhbDfdhJRng",
                "operation": "de_list",
                "seller": "H38kTeMY8aQSMN5sNhSuwHaur2Awj6XRi57CDwN2pUtG",
                "transaction_signature": "49zRGKohzCu2nr84QSfTidCsVJ6hyq87pxyMUc2xvtBSdfApWdJqLVrK6oZX8C6maiekoGEkwhiUKQ1GsmKoGgcd"
            },
            {
                "block_time": 1644381708.0,
                "exchange": "magic-eden",
                "exchange_readable": "Magic Eden",
                "mint_address": "DjBRcfH83wPpZ5TQ9mJ1i7PzP4LbZ2gp7MhbDfdhJRng",
                "operation": "list",
                "price": 13900000000.0,
                "seller": "H38kTeMY8aQSMN5sNhSuwHaur2Awj6XRi57CDwN2pUtG",
                "transaction_signature": "3F7SsJFATJAAXTh8h4McG7ndE5ovsW6nUhZjtdbV4tLe5HdDJf3L968NjhS7vKPUYt7VVWt8SNwFjUJ7RYF8PMSk"
            }
        ],
        "floor": 13900000000.0,
        "volume": 13000000000.0
    }
    """
