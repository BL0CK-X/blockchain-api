import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.blockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'INSERT-API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'INSERT-API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaNFTMarketplacesApi();
const result = await apiInstance.solanaGetNFTMarketplaceMarketShare().then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return error;
});

// Values given in Lamports
console.log(result);
