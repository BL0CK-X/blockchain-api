import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaWalletApi();

// Let's create a new wallet with a balance of 0.

// First, generate a new seed phrase.

const new_seed_phrase = await apiInstance.solanaGenerateSecretRecoveryPhrase().then((data) => {
    return data['secret_recovery_phrase'];
}, (error) => {
    console.error(error);
    return null;
});
console.log("Seed Phrase: ", new_seed_phrase);

// Then, derive a public key owned by the seed phrase.

let getPublicKeyRequest = new theblockchainapi.GetPublicKeyRequest(); // GetPublicKeyRequest | 
getPublicKeyRequest.secret_recovery_phrase = new_seed_phrase;

const public_key = await apiInstance.solanaDerivePublicKey(getPublicKeyRequest).then((data) => {
  console.log('API called successfully.');
  return data['public_key'];
}, (error) => {
  console.error(error);
  return null;
});

console.log("Public Key: ", public_key);

// Finally, get the balance of that public key on the devnet, measured in SOL (not LAMPORT, 1e9 LAMPORT in 1 SOL)

const balance_request = new theblockchainapi.BalanceRequest(); // BalanceRequest | 
balance_request.public_key = public_key;
balance_request.network = 'devnet';
balance_request.unit = 'sol';

let opts = {
  'balanceRequest': balance_request
};

const balance_result = await apiInstance.solanaGetBalance(opts).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return error;
});

console.log("Balance Retrieved: ", balance_result);