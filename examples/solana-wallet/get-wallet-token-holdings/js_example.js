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

let apiInstance = new theblockchainapi.SolanaWalletApi();
let network = 'mainnet-beta'; // String | The network ID (devnet, mainnet-beta)
let publicKey = 'GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ'; // String | The public key of the account whose list of owned NFTs you want to get


let result = await apiInstance.solanaGetTokensBelongingToWallet(network, publicKey, {}).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return error;
});

console.log("Token Holdings: ", result);


// As you can see here... https://explorer.solana.com/address/BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX/tokens
// ... public key owns 2 NFTs, but used to also own 2 others. Set `include_zero_balance_holdings` to `True` and
// `include_nfts` to `True` to see all 4 NFTs.. See that the balance is `0` for two of the NFTs and `1` for the other
// two NFTs.
publicKey = 'BNEG1SxxPpcFHQszKshECqf9aRV5E2pmot7kLSnhzHrX';
let opts = {
  'includeNfts': true, // Boolean | Whether or not to include NFTs in the response
  'includeZeroBalanceHoldings': true // Boolean | Whether or not to include holdings that have zero balance. This indicates that the wallet held this token or NFT in the past, but no longer holds it.
};

result = await apiInstance.solanaGetTokensBelongingToWallet(network, publicKey, opts).then((data) => {
    console.log('API called successfully.');
    return data;
}, (error) => {
    console.error(error);
    return error;
});
console.log("Token Holdings: ", result);
