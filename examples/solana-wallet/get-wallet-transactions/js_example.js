import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.blockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaWalletApi();
let network = 'mainnet-beta'; // String | The network ID (devnet, mainnet-beta)
let publicKey = 'GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ'; // String | The public key of the account whose list of owned NFTs you want to get


let result = await apiInstance.solanaGetWalletTransactions(network, publicKey).then((data) => {
 console.log('API called successfully.');
 return data;
}, (error) => {
 console.error(error);
 return error;
});

console.log("Wallet Transactions: ", result);

publicKey = 'BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX';

result = await apiInstance.solanaGetWalletTransactions(network, publicKey).then((data) => {
   console.log('API called successfully.');
   return data;
}, (error) => {
   console.error(error);
   return error;
});
console.log("Wallet Transactions: ", result);


// You can get more info based on the transaction signature like this:
let txApiInstance = new theblockchainapi.SolanaTransactionApi();
let txSignature = '5wHu1qwD7q5ifaN5nwdcDqNFo53GJqa7nLp2BeeEpcHCusb4GzARz4GjgzsEHMkBMgCJMGa6GSQ1VG96Exv8kt2W'; // String | The transaction signature of the transaction

result = await txApiInstance.solanaGetTransaction(network, txSignature).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

console.log("Transaction Details", result);

