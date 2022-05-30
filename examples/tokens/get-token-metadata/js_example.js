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

let apiInstance = new theblockchainapi.TokenApi();

//let blockchain = "solana"; // only supported for Solana
//let network = 'mainnet-beta'; // String | The network of the blockchain you selected  - Solana: `devnet`, `mainnet-beta` - Ethereum: `ropsten`, `mainnet`  Defaults when not provided (not applicable to path parameters): - Solana: `devnet` - Ethereum: `ropsten`
//let tokenBlockchainIdentifier = 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v';

let blockchain = "ethereum"; // only supported for Solana
let network = 'mainnet'; // String | The network of the blockchain you selected  - Solana: `devnet`, `mainnet-beta` - Ethereum: `ropsten`, `mainnet`  Defaults when not provided (not applicable to path parameters): - Solana: `devnet` - Ethereum: `ropsten`
let tokenBlockchainIdentifier = '0xdAC17F958D2ee523a2206206994597C13D831ec7';

const token = await apiInstance.getTokenMetadata(blockchain, network, tokenBlockchainIdentifier).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
});

console.log(token);