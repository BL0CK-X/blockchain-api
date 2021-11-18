import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaWalletApi();

// https://explorer.solana.com/address/7EWJNaNYfPYMaqzdAAa4ps5kpqW95B7VHsjhW1kr18sj
const nft_on_mainnet_beta_address = '7EWJNaNYfPYMaqzdAAa4ps5kpqW95B7VHsjhW1kr18sj';

// https://explorer.solana.com/address/FmKrVEUKqnpQwGX5kbxR4HB5GZuZaGFdwKkhAKUKC5zA?cluster=devnet
const nft_on_devnet_address = 'FmKrVEUKqnpQwGX5kbxR4HB5GZuZaGFdwKkhAKUKC5zA';

// https://explorer.solana.com/address/SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt
const serum_token_address = "SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt";

const request = new theblockchainapi.ATARequest(); // ATARequest | 

request.secret_recovery_phrase = 'sadness swap zebra path panda power finger robot yellow game list enemy';
request.derivation_path = 'm/44/501/0/0';
request.passphrase = '';

// (1) ... Associated token address for an NFT on mainnet-beta
request.token_address = nft_on_mainnet_beta_address;
request.network = 'mainnet-beta';

let opts = {
  'aTARequest': request
};

let result = await apiInstance.solanaDeriveAssociatedTokenAccountAddress(opts).then((data) => {
  return data;
}, (error) => {
  console.error(error);
  return null;
});
console.log('Associated Token Account Address for NFT on mainnet-beta: ', result['associated_token_address'])


// (2) ... Associated token address for an NFT on devnet
request.token_address = nft_on_devnet_address;
request.network = 'devnet';

opts = {
  'aTARequest': request
};

result = await apiInstance.solanaDeriveAssociatedTokenAccountAddress(opts).then((data) => {
  return data;
}, (error) => {
  console.error(error);
  return null;
});
console.log('Associated Token Account Address for NFT on devnet: ', result['associated_token_address'])


// (3) ... Associated token address for a Serum token
request.token_address = serum_token_address;
request.network = 'mainnet-beta';

opts = {
  'aTARequest': request
};

result = await apiInstance.solanaDeriveAssociatedTokenAccountAddress(opts).then((data) => {
  return data;
}, (error) => {
  console.error(error);
  return null;
});
console.log('Associated Token Account Address for Serum on mainnet-beta: ', result['associated_token_address'])