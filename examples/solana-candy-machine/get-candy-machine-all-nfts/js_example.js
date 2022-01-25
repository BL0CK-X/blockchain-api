import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.blockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaCandyMachineApi();

let network = "mainnet-beta"; // String | The network ID (devnet, mainnet-beta)
let candyMachineId = "FmkrvXRenCGtwBHw3VtBcExp8eTdnau97upaewF4GUEX"; // String | The ID of the candy machine

console.log("This takes about 45 seconds... Starting the API call...")

let result = await apiInstance.solanaGetAllNFTsFromCandyMachine(network, candyMachineId).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

console.log(result);

candyMachineId = "BdgRfRzzFEWTa7Ka5bzWEy1QidSc5qVvn8zq7vRBrDL3"; // String | The ID of the candy machine
// We don't have to specify whether the candy is v1 or v2 this time. It auto-detects it.

console.log("This takes about 45 seconds... Starting the API call...");
console.log(
    "Retrieving all NFTs from a V2 candy machines... This API call can take around 45 seconds..."
)

result = await apiInstance.solanaGetAllNFTsFromCandyMachine(network, candyMachineId).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

console.log(result);