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

let apiInstance = new theblockchainapi.NameServiceApi();

let blockchain = "ethereum"; // String | The blockchain you want to use
let network = "mainnet"; // or ropsten // String | The network of the blockchain you selected  - Solana: `devnet`, `mainnet-beta` - Ethereum: `ropsten`, `mainnet`  Defaults when not provided (not applicable to path parameters): - Solana: `devnet` - Ethereum: `ropsten`

let request =  new theblockchainapi.InputBlockchainIdentifier(); // InputName |
request.blockchain_identifier = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045';

let opts = {
  'inputBlockchainIdentifier': request
};

const name = await apiInstance.getNameForBlockchainIdentifier(
    blockchain, network, opts
).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

console.log("Name: ", name);
