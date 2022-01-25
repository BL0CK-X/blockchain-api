import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.blockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaNFTApi();

const search_nfts = async (request, title) =>  {
    let result = await apiInstance.solanaSearchNFTs(
        {
          'nFTSearchRequest': request
        }
    ).then((data) => {
      console.log('API called successfully.');
      return data;
    }, (error) => {
      console.error(error);
      return null;
    });
    console.log(title);
    if (result.length > 0) {
        console.log("Found a total of ", result.length, " NFTs.");
        console.log("Here's the first NFT of the list of search result: ", result[0]);
    } else {
        console.log("Didn't find any...");
    }
    console.log("----------------------------------");
};

let request = new theblockchainapi.NFTSearchRequest();
request.name = 'Bobby';
request.name_search_method = 'begins_with';
request.network = 'devnet';
await search_nfts(request, "Searching NFTs with a name that begins with `Bobby` on `devnet`.");


request = new theblockchainapi.NFTSearchRequest();
request.uri = 'https://arweave.net/hI0';
request.uri_search_method = 'begins_with';
request.network = 'devnet';
await search_nfts(request, "Searching NFTs with a uri that begins with `https://arweave.net/hI0` on `devnet`.");


request = new theblockchainapi.NFTSearchRequest();
request.symbol = 'GOAT';
request.symbol_search_method = 'exact_match';
request.network = 'devnet';
await search_nfts(request, "Searching NFTs with a symbol of `GOAT` on `devnet`.");


request = new theblockchainapi.NFTSearchRequest();
request.mint_address = '4DXvvS6PpKEpz3UrQG4VcAj9HPYiZ72gvZSw1Qjrhud9';
request.network = 'mainnet-beta';
await search_nfts(request, "Searching NFTs with a mint address of `4DXvvS6PpKEpz3UrQG4VcAj9HPYiZ72gvZSw1Qjrhud9` on `mainnet-beta`.");


request = new theblockchainapi.NFTSearchRequest();
request.update_authority = 'BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX';
request.network = 'mainnet-beta';
await search_nfts(request, "Searching NFTs with an update authority of `BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX` on `mainnet-beta`.");


request = new theblockchainapi.NFTSearchRequest();
request.update_authority = 'BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX';
request.name = 'Musk';
request.name_search_method = 'begins_with';
request.network = 'mainnet-beta';
await search_nfts(request, "Searching NFTs with an update authority of `BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX` on `mainnet-beta`.");

