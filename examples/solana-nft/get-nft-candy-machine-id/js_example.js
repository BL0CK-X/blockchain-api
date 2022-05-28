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

let apiInstance = new theblockchainapi.SolanaNFTApi();

let getCandyMachineIdRequest = new theblockchainapi.GetCandyMachineIDRequest();
getCandyMachineIdRequest.network = 'mainnet-beta';
getCandyMachineIdRequest.mint_address = 'EEr5yQpNXf7Bru6Rt5podx56HGW9CEehXqgRGh2wa71w';

let opts = {
  'getCandyMachineIDRequest': getCandyMachineIdRequest
};

// Yes, minted with a V1 candy machine.
let result = await apiInstance.solanaGetNFTsCandyMachineId(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
  return data;
}, (error) => {
  console.error(error);
  return null;
});
console.log("Candy Machine Id:", result);

// Yes, minted with a V2 candy machine.
getCandyMachineIdRequest.mint_address = '63k8TCFNfQigyCfR4hvZg5moHZQ2uJYnfsuoDnrjHyeb';
result = await apiInstance.solanaGetNFTsCandyMachineId(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
  return data;
}, (error) => {
  console.error(error);
  return null;
});
console.log("Candy Machine Id:", result);

// No, not minted with a candy machine ID.
getCandyMachineIdRequest.mint_address = 'GoxY1RhbuVwvQAWJ9DMT2PZWNJR6peQCy8cuKJHvb44e';
result = await apiInstance.solanaGetNFTsCandyMachineId(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
  return data;
}, (error) => {
  console.error(error['body']['error_message']);
  return null;
});
console.log("Candy Machine Id:", result);
