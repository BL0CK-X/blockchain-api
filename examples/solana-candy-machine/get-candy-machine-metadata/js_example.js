import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

const request = new theblockchainapi.GetCandyDetailsRequest(); // GetCandyDetailsRequest | 
request.candy_machine_id = "9htmDvW58pjCMQdjFbovo8cGBZviDfeP3j7DKnikHEy5";
request.network = "mainnet-beta";

let apiInstance = new theblockchainapi.SolanaCandyMachineApi();
let opts = {
  'getCandyDetailsRequest': request
};

const result = await apiInstance.solanaGetCandyMachineDetails(opts).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return error;
});

console.log(result);