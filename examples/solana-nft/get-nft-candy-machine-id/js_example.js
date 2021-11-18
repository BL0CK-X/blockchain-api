import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaNFTApi();

let getCandyMachineIdRequest = new theblockchainapi.GetCandyMachineIDRequest();
getCandyMachineIdRequest.network = 'mainnet-beta';
getCandyMachineIdRequest.mint_address = 'EEr5yQpNXf7Bru6Rt5podx56HGW9CEehXqgRGh2wa71w';

let opts = {
  'getCandyMachineIDRequest': getCandyMachineIdRequest
};

const result = await apiInstance.solanaGetNFTsCandyMachineId(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
  return data['candy_machine_id'];
}, (error) => {
  console.error(error);
  return null;
});

console.log("Candy Machine Id:", result);
