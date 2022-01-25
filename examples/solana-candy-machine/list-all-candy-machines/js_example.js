import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.blockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

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
