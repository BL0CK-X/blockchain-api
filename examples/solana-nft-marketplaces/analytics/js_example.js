import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.blockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'INSERT-API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'INSERT-API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaNFTMarketplacesApi();
let candyMachineApiInstance = new theblockchainapi.SolanaCandyMachineApi();

let network = "mainnet-beta"; // String | The network ID (devnet, mainnet-beta)
let candyMachineId = "2umuuUfCTBpQZxdTUmnRSQ3LX74nBECncaPjMojbULkJ"; // String | The ID of the candy machine

console.log("First retrieving the list of mint addresses for a collection...")
console.log("This takes about 45 seconds... Starting the API call...")

let result = await candyMachineApiInstance.solanaGetAllNFTsFromCandyMachine(network, candyMachineId).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});


const minted_nfts = result['minted_nfts'];
const mint_addresses = [];

for (let i = 0; i < minted_nfts.length; i++ ) {
    mint_addresses.push(minted_nfts[i]['nft_metadata']['mint']);
}

console.log(mint_addresses);

let nFTAnalyticsRequest =  new theblockchainapi.NFTAnalyticsRequest(); // NFTAnalyticsRequest |
nFTAnalyticsRequest.mint_addresses = mint_addresses;

nFTAnalyticsRequest.start_time = 1644465399; // use -1 to get all
// nFTAnalyticsRequest.end_time = 1644982038;

let opts = {
  'nFTAnalyticsRequest': nFTAnalyticsRequest
};

const analytics_result = await apiInstance.solanaGetNFTMarketplaceAnalytics(opts).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return error;
});

console.log(analytics_result);

const transaction_history = analytics_result['transaction_history'];

console.log(transaction_history);
console.log('Floor', analytics_result['floor']);
console.log('Volume', analytics_result['volume']);
