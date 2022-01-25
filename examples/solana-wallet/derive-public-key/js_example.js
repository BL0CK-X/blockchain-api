import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.blockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaWalletApi();

let getPublicKeyRequest = new theblockchainapi.GetPublicKeyRequest(); // GetPublicKeyRequest | 
getPublicKeyRequest.wallet = {
  secret_recovery_phrase: 'sadness swap zebra path panda power finger robot yellow game list enemy',
  derivation_path: 'm/44/501/0/0',
  passphrase: ''
}

const result = await apiInstance.solanaDerivePublicKey(getPublicKeyRequest).then((data) => {
  console.log('API called successfully.');
  return data['public_key'];
}, (error) => {
  console.error(error);
  return null;
});

console.log("Public Key: ", result);
