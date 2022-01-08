import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaWalletApi();

const private_key = await apiInstance.solanaGeneratePrivateKey().then((data) => {
  return data;
}, (error) => {
  console.error(error);
  return null;
});

const b58_private_key = private_key['b58_private_key'];
console.log("This is a base58-encoded private key. This is what Phantom shows when you click `Show Private Key`");
console.log(b58_private_key);

console.log("------------------------");

const private_key_arr = private_key['private_key'];
console.log("This is a standard private key array. This is what SolFlare shows when you click `Export Private Key`");
console.log(private_key_arr);
