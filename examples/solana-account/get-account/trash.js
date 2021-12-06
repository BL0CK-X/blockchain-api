import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys
//same
let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'Ra0o8AY8DqJaYbJ';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'Q9RwXmuU3zy5EOO';
//api
let apiInstance = new theblockchainapi.SolanaCandyMachineApi();

let request = new theblockchainapi.GetMintedNFTsRequest(); // GetMintedNFTsRequest |
request.candy_machine_id = "8k6K6oAw2GSfgCdJ7Dkb1z5dN7whj1MCw7EoJEwuJ5tW";
request.network = "mainnet-beta";

let opts = {
  'getMintedNFTsRequest': request
};

const result = await apiInstance.solanaGetNFTsMintedFromCandyMachine(opts).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

console.log(result);
let nft_metadata = new Array();
for (let i = 0; i < result.length; i++) {
 nft_metadata.push(result[i]['nft_metadata']['mint'])
}


//Part2
let apiInstance2= new theblockchainapi.SolanaNFTApi();

let network = 'mainnet-beta'; // String | The network ID (devnet, mainnet-beta)
for(let i=0;i<4;i++){
let mintAddress = result[i]['nft_metadata']['mint']; // String | The mint address of the NFT

let view_nft_url = "https://explorer.solana.com/address/" + mintAddress + "?cluster=" + network;
console.log("View the NFT: " + view_nft_url);

const result2 = await apiInstance2.solanaGetNFTOwner(network, mintAddress).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

const nft_owner = result2['nft_owner'];

console.log("Retrieved the NFT Owner: " + nft_owner)
console.log("See the owner's token holdings: https://explorer.solana.com/address/" + nft_owner +  "/tokens?cluster=" + network)
console.log("You should see " + mintAddress + " in their token holdings.")
}
//api 3

let apiInstance3 = new theblockchainapi.SolanaWalletApi();
let network2 = 'mainnet-beta'; // String | The network ID (devnet, mainnet-beta)
for(let i=0;i<result.length;i++){
let publicKey = result[i]["pub_key_hash"]; // String | The public key of the account whose list of owned NFTs you want to get
//let publicKey='8WRsGBaDcs1X7bHWr4Ad5Nx3bW29BkcmEbyavrLXDC4i'
//console.log(publicKey)
const result3 = await apiInstance3.solanaGetNFTsBelongingToWallet(network2, publicKey).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return error;
});

console.log("NFTs: ", result3);

}