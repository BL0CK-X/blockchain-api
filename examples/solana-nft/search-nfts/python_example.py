from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork, SearchMethod

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

    name_to_search = "Bobby"
    nfts = BLOCKCHAIN_API_RESOURCE.search_nfts(
        nft_name=name_to_search,
        nft_name_search_method=SearchMethod.BEGINS_WITH,
        network=SolanaNetwork.DEVNET
    )
    print("-" * 50)
    print(f"Found {len(nfts)} NFTs beginning with the name `{name_to_search}`. Here are some samples: ")
    only_print_five = 5
    count = 0
    for nft in nfts:
        count += 1
        if count > only_print_five:
            break
        print(nft)

    print("-" * 50)
    uri_to_search = "https://arweave.net/hI0"
    nfts = BLOCKCHAIN_API_RESOURCE.search_nfts(
        nft_uri_search_method=SearchMethod.BEGINS_WITH,
        nft_uri=uri_to_search,
        network=SolanaNetwork.DEVNET
    )
    print(f"Found {len(nfts)} NFTs with a URI beginning with `{uri_to_search}`.")

    symbol = "GOAT"
    nfts = BLOCKCHAIN_API_RESOURCE.search_nfts(
        symbol_search_method=SearchMethod.EXACT_MATCH,
        symbol=symbol,
        network=SolanaNetwork.DEVNET
    )
    print(f"Found {len(nfts)} NFTs with a symbol matching `{symbol}`.")

    mint_address = '4DXvvS6PpKEpz3UrQG4VcAj9HPYiZ72gvZSw1Qjrhud9'
    nfts = BLOCKCHAIN_API_RESOURCE.search_nfts(
        mint_address=mint_address,
        network=SolanaNetwork.MAINNET_BETA
    )
    print(f"Found {len(nfts)} NFT with a `mint_address` of `{mint_address}`.")

    update_authority = 'BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX'
    nfts = BLOCKCHAIN_API_RESOURCE.search_nfts(
        update_authority=update_authority,
        network=SolanaNetwork.MAINNET_BETA
    )
    print("-" * 50)
    print(f"Found {len(nfts)} NFTs with an `update_authority` of `{update_authority}`.")
    for nft in nfts:
        print(nft)
    print("-" * 50)

    update_authority = 'BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX'
    name = "Musk"
    nfts = BLOCKCHAIN_API_RESOURCE.search_nfts(
        update_authority=update_authority,
        nft_name=name,
        nft_name_search_method=SearchMethod.BEGINS_WITH,
        network=SolanaNetwork.MAINNET_BETA
    )
    print("-" * 50)
    print(f"Found {len(nfts)} NFTs with an `update_authority` of `{update_authority}` and a name that begins "
          f"with `{name}`.")
    for nft in nfts:
        print(nft)
    print("-" * 50)


if __name__ == '__main__':
    example()

    """
    EXAMPLE OUTPUT: 
    
    --------------------------------------------------
    Found 7 NFTs beginning with the name `Bobby`. Here are some samples: 
    {'nft_metadata': {'data': {'creators': ['6cEzbSh93hcXFWm841wnnLXwsr6u6yfcVzQKGa5rRyh8', 'DuzXruy2ABcFnikLUY22Qb5E2qqyTF8T3kxmjpnr8rgj'], 'name': 'Bobby New Jersey', 'seller_fee_basis_points': 500.0, 'share': [0.0, 100.0], 'symbol': 'SWM', 'uri': 'https://arweave.net/uVqLnlGIG4P3mPAtPM_9ZPTHrJujjBOgX4BGM5ZzMQ8', 'verified': [1.0, 0.0]}, 'is_mutable': True, 'mint': 'J5R1RB8Epou354tN1zGsdCXx9H67S9jP8wGhRnUPttoa', 'primary_sale_happened': True, 'update_authority': 'DuzXruy2ABcFnikLUY22Qb5E2qqyTF8T3kxmjpnr8rgj'}, 'pub_key_hash': 'AjB5w3GSf8TSv47K3KGqJZBtDKH9ckvs2GS2mf7wVmpS'}
    {'nft_metadata': {'data': {'creators': ['2WU25UGcXDEvdRikgCDPrWtKmr6nwg4p7jKyeark3zps', 'D9Eda84T7bHPgAgKv35XtUSfM8bHGuyuBLuWMA8GNVsH', 'G1QroRHZs1Ec4V77ZCfVBKudzso6j4w9GjGY5nbDQ6hG'], 'name': 'Bobby Rabbits #0', 'seller_fee_basis_points': 1000.0, 'share': [0.0, 50.0, 50.0], 'symbol': 'BOBBY', 'uri': 'https://arweave.net/PHGt9me56CbVdLNSZbmJRMtP1FHDQioypWXtSXUaaPE', 'verified': [1.0, 0.0, 0.0]}, 'is_mutable': True, 'mint': '9cApJTNEGRzjLq47tEKaMM2y7hXAe8ih84Cb4x8AvzKi', 'primary_sale_happened': True, 'update_authority': '47qTyabfmQev3iqsDAhVCPvnYkxK8QXhBvUdi5SN5igd'}, 'pub_key_hash': 'ETRchuZiv6BSP3zTPBjqd6pgNh6RopDuJv1LH5wUhdks'}
    {'nft_metadata': {'data': {'creators': ['87ub2UsfrZwu5PbiqFsEXieKB8JYZLwoRSKXQC7wvGsj'], 'name': 'Bobby Brown Potatoes', 'seller_fee_basis_points': 0.0, 'share': [100.0], 'symbol': 'BBPOT', 'uri': 'https://arweave.net/Umi1tOw4hIPn8VkJtq_fjamMgT-YCOGa55g22t6sT6M?ext=jpg', 'verified': [1.0]}, 'is_mutable': True, 'mint': '7L1vJCnWh45YkWJ5Hrm4ZrqkZ5XTt71KkRCCCXXHFsNN', 'primary_sale_happened': False, 'update_authority': '87ub2UsfrZwu5PbiqFsEXieKB8JYZLwoRSKXQC7wvGsj'}, 'pub_key_hash': '4BuRXaoSs82iYGcp2JhKCRmMEqFUL3HPrcMg35wz1UpN'}
    {'nft_metadata': {'data': {'creators': ['6cEzbSh93hcXFWm841wnnLXwsr6u6yfcVzQKGa5rRyh8', 'DuzXruy2ABcFnikLUY22Qb5E2qqyTF8T3kxmjpnr8rgj'], 'name': 'Bobby New Jersey', 'seller_fee_basis_points': 500.0, 'share': [0.0, 100.0], 'symbol': 'SWM', 'uri': 'https://arweave.net/bLtHCRHxeyrnRdSjP8TITr2wXEDHmGI3ZYrkPGgplB4', 'verified': [1.0, 0.0]}, 'is_mutable': True, 'mint': '5XLK2wGRZ76aPYeH52CUBTiuX2bVnmGyhiAVf5aNjbjg', 'primary_sale_happened': True, 'update_authority': 'DuzXruy2ABcFnikLUY22Qb5E2qqyTF8T3kxmjpnr8rgj'}, 'pub_key_hash': '6SzgQX9LwcikN4ZHSjnfmQvcboA1Fr7ZGhritQQySLpu'}
    {'nft_metadata': {'data': {'creators': ['2WU25UGcXDEvdRikgCDPrWtKmr6nwg4p7jKyeark3zps', 'D9Eda84T7bHPgAgKv35XtUSfM8bHGuyuBLuWMA8GNVsH', 'G1QroRHZs1Ec4V77ZCfVBKudzso6j4w9GjGY5nbDQ6hG'], 'name': 'Bobby Rabbits #1', 'seller_fee_basis_points': 1000.0, 'share': [0.0, 50.0, 50.0], 'symbol': 'BOBBY', 'uri': 'https://arweave.net/bausU3PTAoY7M8DcOTe4yr7jttlioyNyVYFp_T5PasU', 'verified': [1.0, 0.0, 0.0]}, 'is_mutable': True, 'mint': 'eKHpkFT4dBvVPVK7MRtR5rSd4joyWFcMqaJdJAazhUs', 'primary_sale_happened': True, 'update_authority': '47qTyabfmQev3iqsDAhVCPvnYkxK8QXhBvUdi5SN5igd'}, 'pub_key_hash': 'CCt4xNJQ2LVi5DhGHJPTEZdFoyqzYA9MuJNJLhMDLZKc'}
    --------------------------------------------------
    Found 4 NFTs with a URI beginning with `https://arweave.net/hI0`.
    Found 60 NFTs with a symbol matching `GOAT`.
    Found 1 NFT with a `mint_address` of `4DXvvS6PpKEpz3UrQG4VcAj9HPYiZ72gvZSw1Qjrhud9`.
    --------------------------------------------------
    Found 3 NFTs with an `update_authority` of `BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX`.
    {'nft_metadata': {'data': {'creators': ['BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX'], 'name': 'Musk Coin', 'seller_fee_basis_points': 0.0, 'share': [100.0], 'symbol': 'MUSK', 'uri': 'https://www.vhv.rs/dpng/d/24-241018_elon-musk-meme-review-hd-png-download.png', 'verified': [1.0]}, 'is_mutable': True, 'mint': 'CB4G7UV3qzjQD7Gx9ZZLsmnTKk6f82pezdUBHaFhPxPw', 'primary_sale_happened': False, 'update_authority': 'BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX'}, 'pub_key_hash': '6tT9h8QCJbhx4TBfFjtz3RWimtQGeMshpDnXeDnxNneM'}
    {'nft_metadata': {'data': {'creators': ['BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX'], 'name': 'Josh Coin', 'seller_fee_basis_points': 0.0, 'share': [100.0], 'symbol': 'JOSH', 'uri': 'https://www.vhv.rs/dpng/d/24-241018_elon-musk-meme-review-hd-png-download.png', 'verified': [1.0]}, 'is_mutable': True, 'mint': 'F3dNuBNyLtLJyYH23vv51DzLFA5ChkxXYHoH1cHZtTqb', 'primary_sale_happened': False, 'update_authority': 'BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX'}, 'pub_key_hash': 'EscJ2ZXCkUWkgizYWkWQ9NAtyMYtAtVzVybhBwLS6noR'}
    {'nft_metadata': {'data': {'creators': ['BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX'], 'name': 'Musk Coin', 'seller_fee_basis_points': 0.0, 'share': [100.0], 'symbol': 'MUSK', 'uri': 'https://blockx-api-storage.s3.amazonaws.com/22574121018/data', 'verified': [1.0]}, 'is_mutable': True, 'mint': '7EWJNaNYfPYMaqzdAAa4ps5kpqW95B7VHsjhW1kr18sj', 'primary_sale_happened': False, 'update_authority': 'BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX'}, 'pub_key_hash': '78RjQhV9F5ePbeggmj8psKDaqwNobyY42sMZ7vfoMXsr'}
    --------------------------------------------------
    --------------------------------------------------
    Found 2 NFTs with an `update_authority` of `BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX` and a name that begins with `Musk`.
    {'nft_metadata': {'data': {'creators': ['BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX'], 'name': 'Musk Coin', 'seller_fee_basis_points': 0.0, 'share': [100.0], 'symbol': 'MUSK', 'uri': 'https://www.vhv.rs/dpng/d/24-241018_elon-musk-meme-review-hd-png-download.png', 'verified': [1.0]}, 'is_mutable': True, 'mint': 'CB4G7UV3qzjQD7Gx9ZZLsmnTKk6f82pezdUBHaFhPxPw', 'primary_sale_happened': False, 'update_authority': 'BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX'}, 'pub_key_hash': '6tT9h8QCJbhx4TBfFjtz3RWimtQGeMshpDnXeDnxNneM'}
    {'nft_metadata': {'data': {'creators': ['BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX'], 'name': 'Musk Coin', 'seller_fee_basis_points': 0.0, 'share': [100.0], 'symbol': 'MUSK', 'uri': 'https://blockx-api-storage.s3.amazonaws.com/22574121018/data', 'verified': [1.0]}, 'is_mutable': True, 'mint': '7EWJNaNYfPYMaqzdAAa4ps5kpqW95B7VHsjhW1kr18sj', 'primary_sale_happened': False, 'update_authority': 'BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX'}, 'pub_key_hash': '78RjQhV9F5ePbeggmj8psKDaqwNobyY42sMZ7vfoMXsr'}
    --------------------------------------------------
    """
