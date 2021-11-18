import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaCandyMachineApi();

// First get the candy machine details. That will have the configuration address in it.

const candy_details_request = new theblockchainapi.GetCandyDetailsRequest(); // GetCandyDetailsRequest | 
candy_details_request.candy_machine_id = "9htmDvW58pjCMQdjFbovo8cGBZviDfeP3j7DKnikHEy5"; // The Goat Society
candy_details_request.network = "mainnet-beta";

let candy_opts = {
  'getCandyDetailsRequest': candy_details_request
};

const candy_machine_info_result = await apiInstance.solanaGetCandyMachineDetails(candy_opts).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return error;
});

console.log("Candy Machine Details: ", candy_machine_info_result);

// Retrieve the configuration address of the candy machine.

const config_address = candy_machine_info_result['config_address'];

// Get the configuration details. 
// The candy machine configuration will have other information not contained in the candy machine details function.

let config_address_request = new theblockchainapi.GetConfigInfoRequest(); // GetConfigInfoRequest | 
config_address_request.config_address = config_address;
config_address_request.network = 'mainnet-beta';

let config_opts = {
  'getConfigInfoRequest': config_address_request
};

const config_info_result = await apiInstance.solanaGetCandyMachineConfigurationDetails(config_opts).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

console.log("Config Info: ", config_info_result);
