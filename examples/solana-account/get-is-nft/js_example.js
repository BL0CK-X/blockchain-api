import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaAccountApi();

let network = "mainnet-beta"; // String | The network ID (devnet, mainnet-beta)
let publicKey = "EEr5yQpNXf7Bru6Rt5podx56HGW9CEehXqgRGh2wa71w"; // String | The public key of the account

const account_info = await apiInstance.solanaGetAccount(network, publicKey).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

console.log("Account Info: ", account_info);
