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

const result = await apiInstance.solanaGetNFTMintFee().then((data) => {
  console.log('API called successfully.');
  return data
}, (error) => {
  console.error(error);
  return null;
});

console.log(result);