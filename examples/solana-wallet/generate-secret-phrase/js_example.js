import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'gyvYjO1vP8UD481';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = '9gwcWht8U0rg5Jv';

let apiInstance = new theblockchainapi.SolanaWalletApi();

const new_seed_phrase = await apiInstance.solanaGenerateSecretRecoveryPhrase().then((data) => {
  console.log('API called successfully.');
  return data['secret_recovery_phrase'];
}, (error) => {
  console.error(error);
  return null;
});

console.log(new_seed_phrase);
