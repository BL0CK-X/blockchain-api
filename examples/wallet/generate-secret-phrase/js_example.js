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

// ---- Generates 12 words by default
//const blockchain = 'solana';
const blockchain = 'ethereum';
//const blockchain = 'near';
//const blockchain = 'binance_smart_chain';

// ---- Generates 24 words by default
//const blockchain = 'avalanche';

let apiInstance = new theblockchainapi.WalletApi();

let request = new theblockchainapi.GenerateSeedPhraseRequest();

// Optional. Can be 12, 15, 18, 21, or 24.
// request.n_words = 12;

let opts = {
  'generateSeedPhraseRequest': request
};

const new_seed_phrase = await apiInstance.generateSeedPhrase(blockchain, opts).then((data) => {
  console.log('API called successfully.');
  return data['secret_recovery_phrase'];
}, (error) => {
  console.error(error);
  return null;
});

console.log(new_seed_phrase);
