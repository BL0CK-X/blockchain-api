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

let apiInstance = new theblockchainapi.TransactionApi();

let blockchain = 'ethereum';
let network = 'mainnet'; // String | The network ID (devnet, mainnet-beta)
let transactionBlockchainIdentifier = '0x1e1b56c517d56df2f41fd6fe37aa8446657ec05ab368ce8141919a8a9a79b5d4';

//let blockchain = 'solana';
//let network = 'mainnet-beta'; // String | The network ID (devnet, mainnet-beta)
//let transactionBlockchainIdentifier = '5wHu1qwD7q5ifaN5nwdcDqNFo53GJqa7nLp2BeeEpcHCusb4GzARz4GjgzsEHMkBMgCJMGa6GSQ1VG96Exv8kt2W'; // String | The transaction signature of the transaction

const result = await apiInstance.getTransaction(blockchain, network, transactionBlockchainIdentifier).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

console.log("Transaction: ", result);