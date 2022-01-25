from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork, \
    SolanaCandyMachineContractVersion, SearchMethod
import json

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

    def print_output(candies: list, title: str):
        print("-" * 20)
        print(title)
        for candy in candies:
            print(candy)
        print("-" * 20)

    update_authority = "31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj"
    result = BLOCKCHAIN_API_RESOURCE.search_candy_machines(
        update_authority=update_authority,
        network=SolanaNetwork.MAINNET_BETA,
        candy_machine_contract_version=SolanaCandyMachineContractVersion.V1
    )
    print_output(result, title=f"Finding candy machines which have the update authority, `{update_authority}`.")

    symbol = "SOL"
    result = BLOCKCHAIN_API_RESOURCE.search_candy_machines(
        symbol=symbol,
        symbol_search_method=SearchMethod.BEGINS_WITH,
        network=SolanaNetwork.MAINNET_BETA,
        candy_machine_contract_version=SolanaCandyMachineContractVersion.V2
    )
    print_output(result, title=f"Finding candy machines which start with the symbol, `{symbol}`.")
    if len(result) > 0:
        metadata = BLOCKCHAIN_API_RESOURCE.get_candy_machine_metadata(
            candy_machine_id=result[0],
            network=SolanaNetwork.MAINNET_BETA,
            candy_machine_contract_version=SolanaCandyMachineContractVersion.V2
        )
        print(json.dumps(metadata, indent=4, sort_keys=True))

    symbol = "SOL"
    result = BLOCKCHAIN_API_RESOURCE.search_candy_machines(
        symbol=symbol,
        symbol_search_method=SearchMethod.EXACT_MATCH,
        network=SolanaNetwork.MAINNET_BETA,
        candy_machine_contract_version=SolanaCandyMachineContractVersion.V2
    )
    if len(result) > 0:
        print_output(result, title=f"Finding candy machines which have the symbol, `{symbol}`.")
    else:
        print("-" * 20)
        print("Didn't find any!")
        print("-" * 20)

    nft_name = "Genesis"
    nft_name_index = 0
    nft_name_search_method = SearchMethod.BEGINS_WITH
    result = BLOCKCHAIN_API_RESOURCE.search_candy_machines(
        nft_name=nft_name,
        nft_name_index=nft_name_index,
        nft_name_search_method=nft_name_search_method,
        network=SolanaNetwork.MAINNET_BETA,
        candy_machine_contract_version=SolanaCandyMachineContractVersion.V2
    )
    print_output(result, title=f"Finding candy machines where the NFT stored at index `{nft_name_index}`"
                               f" begins with the name `{nft_name}`.")

    uuid = '3qt9aB'
    result = BLOCKCHAIN_API_RESOURCE.search_candy_machines(
        uuid=uuid,
        network=SolanaNetwork.MAINNET_BETA,
        candy_machine_contract_version=SolanaCandyMachineContractVersion.V2
    )
    print_output(result, title=f"Finding candy machines with a uuid `{uuid}`. There should only be one.")


if __name__ == '__main__':
    example()

    """
    EXAMPLE OUTPUT: 
    
    --------------------
    Finding candy machines which have the update authority, `31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj`.
    BmmfHiKHzzaV9HUUT4ym1mSNa3hE2gkDkq3HwWQPKFm9
    --------------------
    --------------------
    Finding candy machines which start with the symbol, `SOL`.
    8WgcyTVPhyC9KYJV7rMgvJMpgiHVqpCUcNpxXPbJLduv
    C8iaVaN5c4pMG147fbhNDjt7EUBWqhdG6iJ8h7mMSRCp
    3qt9aBBmTSMxyzFEcwzZnFeV4tCZzPkTYVqPP7Bw5zUh
    Fdq8LfR12mm3yxwimywjofam6SSA3QQ1mZ6gR3LhZErT
    --------------------
    {
        "authority": "DeBtJy88jrnheD8F3HEAqiQztykXksgMyvmcByHC5RGv",
        "candy_machine_id": "8WgcyTVPhyC9KYJV7rMgvJMpgiHVqpCUcNpxXPbJLduv",
        "config_address": "8WgcyTVPhyC9KYJV7rMgvJMpgiHVqpCUcNpxXPbJLduv",
        "creators": [
            "DeBtJy88jrnheD8F3HEAqiQztykXksgMyvmcByHC5RGv",
            12.0,
            "53W4KTivh2Gm6XS15yWbPPpyC8wAmzf2Tih9yQhPxg3x",
            44.0,
            "H7MxF9YpK9542Aab9pQHikwGVyj6kJArko8uEZ9kVsVr",
            44.0
        ],
        "end_settings": {
            "end_on_x_date": null,
            "end_when_x_sold": null
        },
        "gatekeeper": {
            "expire_on_use": null,
            "gatekeeper_network": null
        },
        "go_live_date": 1640041200.0,
        "hidden_settings": null,
        "is_mutable": true,
        "items_available": 3333.0,
        "items_redeemed": 0.0,
        "key": "8WgcyTVPhyC9KYJV7rMgvJMpgiHVqpCUcNpxXPbJLduv",
        "max_supply": 0.0,
        "partial_info": false,
        "price": 1000000000.0,
        "retain_authority": true,
        "seller_fee_basis_points": 600.0,
        "share": [],
        "symbol": "SOLFLOWERS",
        "token_mint": null,
        "uuid": "8WgcyT",
        "wallet": "G4xavVeK4XEXsaa1YfAx526BDh4Ahdq6SN71jbUA3Wxx",
        "whitelist": {
            "discounted_price": 500000000.0,
            "mint": "7nE1GmnMmDKiycFkpHF7mKtxt356FQzVonZqBWsTWZNf",
            "mode": {
                "burnEveryTime": {}
            },
            "presale": true
        }
    }
    --------------------
    Didn't find any!
    --------------------
    --------------------
    Finding candy machines where the NFT stored at index `0` begins with the name `Genesis`.
    BdgRfRzzFEWTa7Ka5bzWEy1QidSc5qVvn8zq7vRBrDL3
    --------------------
    --------------------
    Finding candy machines with a uuid `3qt9aB`. There should only be one.
    3qt9aBBmTSMxyzFEcwzZnFeV4tCZzPkTYVqPP7Bw5zUh
    --------------------
    """
