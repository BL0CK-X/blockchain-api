import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaCandyMachineApi();

let network = "mainnet-beta"; // String | The network ID (devnet, mainnet-beta)
let candyMachineId = "FmkrvXRenCGtwBHw3VtBcExp8eTdnau97upaewF4GUEX"; // String | The ID of the candy machine

console.log("This takes about 45 seconds... Starting the API call...")

const result = await apiInstance.solanaGetAllNFTsFromCandyMachine(network, candyMachineId).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});


console.log(result);