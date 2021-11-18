import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

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