import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaNFTApi();

let network = 'mainnet-beta'; // String | The network ID (devnet, mainnet-beta)
let mintAddress = '2pQPtnFm2mgXZrVWyNdcf5Qf2TWBGkTAeKZJhPjsc7Jn'; // String | The mint address of the NFT

let view_nft_url = "https://explorer.solana.com/address/" + mintAddress + "?cluster=" + network;
console.log("View the NFT: " + view_nft_url);

const result = await apiInstance.solanaGetNFTOwner(network, mintAddress).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

const nft_owner = result['nft_owner'];

console.log("Retrieved the NFT Owner: " + nft_owner)
console.log("See the owner's token holdings: https://explorer.solana.com/address/" + nft_owner +  "/tokens?cluster=" + network)
console.log("You should see " + mintAddress + " in their token holdings.")
