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

let apiInstance = new theblockchainapi.SolanaCandyMachineApi();
const result = await apiInstance.solanaListAllCandyMachines().then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return error;
});

console.log(result);
console.log("Keys of Result:", Object.keys(result));
console.log("# of V1 Candy Machines", result['config_addresses_v1'].length);
console.log("# of V2 Candy Machines", result['config_addresses_v2'].length);
console.log("# of Magic Eden Candy Machines", result['config_addresses_magic-eden-v1'].length);
