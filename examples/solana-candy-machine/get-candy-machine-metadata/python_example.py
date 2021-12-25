from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork, SolanaCandyMachineContractVersion
import json

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

    candy_machine_id_v1 = "9htmDvW58pjCMQdjFbovo8cGBZviDfeP3j7DKnikHEy5"
    metadata = BLOCKCHAIN_API_RESOURCE.get_candy_machine_metadata(
        candy_machine_id=candy_machine_id_v1,
        network=SolanaNetwork.MAINNET_BETA
    )
    print(f"Metadata of a v1 Candy Machine")
    print(json.dumps(metadata, indent=4, sort_keys=True))
    print("-" * 20)

    candy_machine_id_v2 = "4m1NuyoW87ZRHByQQ4frWaApbNARNLXjebf59fTcGAv1"
    metadata = BLOCKCHAIN_API_RESOURCE.get_candy_machine_metadata(
        candy_machine_id=candy_machine_id_v2,
        network=SolanaNetwork.MAINNET_BETA,
        candy_machine_contract_version=SolanaCandyMachineContractVersion.V2
    )
    print(f"Metadata of a v2 Candy Machine")
    print(json.dumps(metadata, indent=4, sort_keys=True))
    print("-" * 20)


if __name__ == '__main__':
    example()

    """
    EXAMPLE OUTPUT:
    
    Metadata of a v1 Candy Machine
    {
        "authority": "B13yYLdTb3reTZmoyZtGGxCCqEpTzLR2PTzgTomTYuK4",
        "bump": 255.0,
        "candy_machine_id": "9htmDvW58pjCMQdjFbovo8cGBZviDfeP3j7DKnikHEy5",
        "config_address": "FVbP4uormTqtmR8uQS2YrfKEfoVoQfGEzznCMPTQMZoQ",
        "creators": [
            {
                "address": "9C5Tg7bKV2m2H79sJ8WzrRYUyC7qQe5foxZvGCR8BZ5A",
                "share": 30.0
            },
            {
                "address": "EEs4thyqw4dCgFXZDzSaX5eXM9XtF4XscSEQWjb7jZqV",
                "share": 30.0
            },
            {
                "address": "B13yYLdTb3reTZmoyZtGGxCCqEpTzLR2PTzgTomTYuK4",
                "share": 40.0
            }
        ],
        "go_live_date": 1635883384.0,
        "is_mutable": true,
        "items_available": 8888.0,
        "items_redeemed": 8888.0,
        "max_number_of_lines": 8888.0,
        "max_supply": 0.0,
        "partial_info": false,
        "price": 1000.0,
        "retain_authority": true,
        "seller_fee_basis_points": 1000.0,
        "symbol": "GOAT",
        "token_mint": null,
        "uuid": "FVbP4u",
        "wallet": "B13yYLdTb3reTZmoyZtGGxCCqEpTzLR2PTzgTomTYuK4"
    }
    --------------------
    Metadata of a v2 Candy Machine
    {
        "authority": "D9Ysnx4sNgkKsUSkRr5Dt8iTDMWraRDhjVkPX2hgx7Rj",
        "candy_machine_id": "4m1NuyoW87ZRHByQQ4frWaApbNARNLXjebf59fTcGAv1",
        "config_address": "4m1NuyoW87ZRHByQQ4frWaApbNARNLXjebf59fTcGAv1",
        "creators": [
            "4griW5rKwn7ecT99ECbNJ9nqFWVxSWGity5PxVuDHMeh",
            100.0
        ],
        "end_settings": {
            "end_on_x_date": null,
            "end_when_x_sold": null
        },
        "gatekeeper": {
            "expire_on_use": null,
            "gatekeeper_network": null
        },
        "go_live_date": 1640118060.0,
        "hidden_settings": null,
        "is_mutable": true,
        "items_available": 4444.0,
        "items_redeemed": 840.0,
        "key": "4m1NuyoW87ZRHByQQ4frWaApbNARNLXjebf59fTcGAv1",
        "max_supply": 0.0,
        "partial_info": false,
        "price": 550000000.0,
        "retain_authority": true,
        "seller_fee_basis_points": 600.0,
        "share": [],
        "symbol": "TROLEX",
        "token_mint": null,
        "uuid": "4m1Nuy",
        "wallet": "4griW5rKwn7ecT99ECbNJ9nqFWVxSWGity5PxVuDHMeh",
        "whitelist": {
            "discounted_price": 450000000.0,
            "mint": "nNK9tzMQNmuftMHKaHHc635ubsvpWvsbd2Ut5nZ5GUT",
            "mode": {
                "burnEveryTime": {}
            },
            "presale": true
        }
    }
    --------------------
    """
