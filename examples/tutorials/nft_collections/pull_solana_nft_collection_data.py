from theblockchainapi import SolanaAPIResource, SolanaNetwork, SearchMethod, Blockchain, BlockchainNetwork
from collections import defaultdict
import json
from concurrent.futures import ThreadPoolExecutor

# Get an API key pair for free here: https://dashboard.blockchainapi.com/
MY_API_KEY_ID = 'AbSox7LJV3klHJe'
MY_API_SECRET_KEY = '6OwvgukfqH2GpXc'

BLOCKCHAIN_API_RESOURCE = SolanaAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)


def pull_mint_addresses():
    update_authorities = defaultdict(int)

    nfts = BLOCKCHAIN_API_RESOURCE.search_nfts(
        # update_authority="CvywfuSVev6da9LngjJkFd2y3utrU2W9zvHw8TAmfo9P",
        symbol="YC\x00",
        symbol_search_method=SearchMethod.EXACT_MATCH,
        nft_name="Solana Money Boy",
        nft_name_search_method=SearchMethod.BEGINS_WITH,
        network=SolanaNetwork.MAINNET_BETA
    )
    print(len(nfts))

    for nft in nfts:
        update_authorities[nft['nft_metadata']['update_authority']] += 1

    # We know there are only max 4 update authorities, because we know there are 4 candy machines.

    valid_update_authorities = set()
    min_associated_nfts_to_be_valid = 50

    for update_authority, n_associated_nfts in update_authorities.items():
        if n_associated_nfts > min_associated_nfts_to_be_valid:
            valid_update_authorities.add(update_authority)

    valid_nft_mint_addresses = set()

    for nft in nfts:
        update_authority = nft['nft_metadata']['update_authority']
        mint_address = nft['nft_metadata']['mint']

        if update_authority in valid_update_authorities:
            valid_nft_mint_addresses.add(mint_address)

    with open("0euvre_mint_addresses.json", "w+") as fp:
        fp.write(json.dumps(list(valid_nft_mint_addresses)))


def pull_mint_stats():

    owners = defaultdict(int)

    with open("the_founders.json", "rb+") as fp:

        # mint_addresses = json.loads(fp.read())

        nfts = json.loads(fp.read().decode())
        mint_addresses = list()
        for nft in nfts:
            mint_addresses.append(nft['nft_metadata']['mint'])

        print(len(mint_addresses))

    executor = ThreadPoolExecutor(max_workers=20)
    tasks = list()
    n_mints = len(mint_addresses)
    prices = list()
    exchange_listings = defaultdict(set)

    for i in range(n_mints):

        def get_data(index: int):
            mint_address = mint_addresses[index]

            # noinspection PyBroadException
            try:
                owner_ = BLOCKCHAIN_API_RESOURCE.get_nft_owner(mint_address, SolanaNetwork.MAINNET_BETA)

                # # noinspection PyBroadException
                # try:
                #     listing = BLOCKCHAIN_API_RESOURCE.get_nft_listing(mint_address, SolanaNetwork.MAINNET_BETA)
                #     if 'seller' in listing:
                #         owner_ = listing['seller']
                #     prices.append(listing['price'])
                #     exchange_listings[listing['exchange_readable']].add(mint_address)
                # except Exception as e:
                #     print(e, mint_address)

                owners[owner_] += 1
            except Exception as e:
                print("Error!", str(e))
                pass

            if index % 25 == 0:
                print(f"Done... {index} / {n_mints}")

        # Uncomment this to only pull a few NFTs for testing purposes.
        # if i > 1000:
        #     break

        a = executor.submit(get_data, i)
        tasks.append(a)

    for task in tasks:
        task.result()

    print("-" * 50)
    for owner, count in owners.items():
        print(owner, count)

    print("-" * 50)
    top_ten_owners = sorted(owners, key=owners.get, reverse=True)[:10]
    print(f"Number of Unique Owners: {len(set(owners.keys()))}")
    print("Top 10 Owners")
    # 1BWutmTvYPwDtmw9abTkS4Ssr8no61spGAvW1X6NDix
    for owner in top_ten_owners:
        print(f"{owner} owns {owners[owner]} Money Boys.")

    print("-" * 20)
    owners_with_more_than_x_money_boys = 5
    print(f"Printing Owners with More than {owners_with_more_than_x_money_boys} Money Boys")
    for owner, count in owners.items():
        if count > owners_with_more_than_x_money_boys:
            print(owner, count)
    print("-" * 20)

    lamports_in_a_sol = int(1e9)

    if len(exchange_listings) > 0:
        for exchange_listing_name, mints in exchange_listings.items():
            print(f"{len(mints)} Money Boys are listed on {exchange_listing_name}")

        print(f"Highest Price: {round(max(prices) / lamports_in_a_sol, 4)} SOL")
        print(f"Floor Price: {round(min(prices) / lamports_in_a_sol, 4)} SOL")
    else:
        print("No listings found for the entire collection!")


if __name__ == '__main__':

    pull_mint_stats()
    # pull_mint_addresses()
    # import time
    # start = int(time.time())
    # print("START:", start)
    # pull_mint_stats()
    # end = int(time.time())
    # print("END:", end)
    # print(f"TOOK {end - start} SECONDS")
