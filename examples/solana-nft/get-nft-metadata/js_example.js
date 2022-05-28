import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;
let APIKeyID = defaultClient.authentications['APIKeyID'];
let APISecretKey = defaultClient.authentications['APISecretKey'];

// BEGIN: -----------------------------------------------------------------------------------------------
// TODO:- Fill in with your own API Keys
// Get a free API Key Pair: https://dashboard.blockchainapi.com/api-keys
APIKeyID.apiKey = 'API-KEY-ID';
APISecretKey.apiKey = 'API-SECRET-KEY';

APIKeyID.apiKey = 'gJfSVNAf21eVWwV';
APISecretKey.apiKey = 'ov8AMrIHMqZymQM';
// END:   -----------------------------------------------------------------------------------------------

let apiInstance = new theblockchainapi.SolanaNFTApi();

let network = 'mainnet-beta'; // String | The network ID (devnet, mainnet-beta)
let mintAddress = 'EEr5yQpNXf7Bru6Rt5podx56HGW9CEehXqgRGh2wa71w'; // String | The mint address of the NFT

const result = await apiInstance.solanaGetNFT(network, mintAddress).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

console.log(result);