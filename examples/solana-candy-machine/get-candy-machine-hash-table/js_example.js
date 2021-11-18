import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaCandyMachineApi();

let request = new theblockchainapi.GetMintedNFTsRequest(); // GetMintedNFTsRequest | 
request.candy_machine_id = "9htmDvW58pjCMQdjFbovo8cGBZviDfeP3j7DKnikHEy5";
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

let pub_key_hashes = new Array();

for (let i = 0; i < result.length; i++) {
    pub_key_hashes.push(result[i]['pub_key_hash'])
}

console.log(pub_key_hashes);