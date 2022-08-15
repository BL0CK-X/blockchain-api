import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;
let APIKeyID = defaultClient.authentications['APIKeyID'];
let APISecretKey = defaultClient.authentications['APISecretKey'];

// BEGIN: -----------------------------------------------------------------------------------------------
// TODO:- Fill in with your own API Keys
// Get a free API Key Pair: https://dashboard.blockchainapi.com/api-keys
APIKeyID.apiKey = 'API-KEY-ID';
APISecretKey.apiKey = 'API-SECRET-KEY';
// END:   -----------------------------------------------------------------------------------------------

let apiInstance = new theblockchainapi.SolanaNFTApi();

let network = 'mainnet-beta'; // String | The network ID (devnet, mainnet-beta)
let mintAddress = '2pQPtnFm2mgXZrVWyNdcf5Qf2TWBGkTAeKZJhPjsc7Jn'; // String | The mint address of the NFT

let view_nft_url = "https://explorer.solana.com/address/" + mintAddress + "?cluster=" + network;
console.log("View the NFT: " + view_nft_url);

const result = await apiInstance.solanaGetNFTOwnerAdvanced(network, mintAddress).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

console.log("Retrieved the NFT Owner result: " + JSON.stringify(result));
