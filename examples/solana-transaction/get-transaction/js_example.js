import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'gyvYjO1vP8UD481';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = '9gwcWht8U0rg5Jv';

let apiInstance = new theblockchainapi.SolanaTransactionApi();

let network = 'mainnet-beta'; // String | The network ID (devnet, mainnet-beta)
let txSignature = '5wHu1qwD7q5ifaN5nwdcDqNFo53GJqa7nLp2BeeEpcHCusb4GzARz4GjgzsEHMkBMgCJMGa6GSQ1VG96Exv8kt2W'; // String | The transaction signature of the transaction

const result = await apiInstance.solanaGetTransaction(network, txSignature).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

console.log("Transaction: ", result);