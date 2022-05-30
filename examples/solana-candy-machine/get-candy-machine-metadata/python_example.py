from theblockchainapi import SolanaAPIResource, SolanaNetwork
import json

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

    candy_machine_id_v2 = "BdgRfRzzFEWTa7Ka5bzWEy1QidSc5qVvn8zq7vRBrDL3"
    metadata = BLOCKCHAIN_API_RESOURCE.get_candy_machine_metadata(
        candy_machine_id=candy_machine_id_v2,
        network=SolanaNetwork.MAINNET_BETA
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
        "go_live_date": 1635883384.0,
        "items_available": 8888.0,
        "items_redeemed": 8888.0,
        "partial_info": true,
        "price": 1000.0,
        "token_mint": null,
        "uuid": "FVbP4u",
        "wallet": "B13yYLdTb3reTZmoyZtGGxCCqEpTzLR2PTzgTomTYuK4"
    }
    --------------------
    Metadata of a v2 Candy Machine
    {
        "authority": "EDshWM3jBy2YUszMiFLAFLx3WkbtqR9An7JZzvg22R1P",
        "candy_machine_id": "BdgRfRzzFEWTa7Ka5bzWEy1QidSc5qVvn8zq7vRBrDL3",
        "config_address": "BdgRfRzzFEWTa7Ka5bzWEy1QidSc5qVvn8zq7vRBrDL3",
        "creators": [
            "5LAfBvHiJBKaEqqXd7TmPZgbmRPRbqRBMbQLPeyqE46p",
            85.0,
            "HCRc9R6iEmmSz7m9LvHtPt3o1WvyoSj6yWtvXRESEFSF",
            5.0,
            "G2Z8DTdcnhLg9ydosi9o9g5PfQQre1LpdGDLoTN6tYBe",
            10.0
        ],
        "end_settings": {
            "end_on_x_date": null,
            "end_when_x_sold": null
        },
        "gatekeeper": {
            "expire_on_use": true,
            "gatekeeper_network": "ignREusXmGrscGNUesoU9mxfds9AiYTezUKex2PsZV6"
        },
        "go_live_date": 1639249200.0,
        "hidden_settings": null,
        "is_mutable": true,
        "items_available": 777.0,
        "items_redeemed": 702.0,
        "key": "BdgRfRzzFEWTa7Ka5bzWEy1QidSc5qVvn8zq7vRBrDL3",
        "max_supply": 0.0,
        "partial_info": false,
        "price": 1.0,
        "retain_authority": true,
        "seller_fee_basis_points": 500.0,
        "share": [],
        "symbol": "LJGEN2",
        "token_mint": "4bvi1vSLJn4z5iDDYfUcroJJYAMfViNW8TRQDhxNKY95",
        "uuid": "BdgRfR",
        "wallet": "5zuTfpJcR87nRvykbDzVwXkzwnq38QewqbT3hHGFGMiv",
        "whitelist": {
            "discounted_price": null,
            "mint": null,
            "mode": null,
            "presale": null
        }
    }
    --------------------
    """
