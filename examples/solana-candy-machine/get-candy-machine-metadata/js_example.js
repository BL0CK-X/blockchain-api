import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaCandyMachineApi();
let request = new theblockchainapi.GetCandyMetadataRequest() // GetCandyMetadataRequest |

// V1 candy machine
request.candy_machine_id = "9htmDvW58pjCMQdjFbovo8cGBZviDfeP3j7DKnikHEy5";
request.network = "mainnet-beta";

let opts = {
  'getCandyMetadataRequest': request
};

let result = await apiInstance.solanaGetCandyMachineMetadata(opts).then((data) => {
    console.log('API called successfully.');
    return data;
}, (error) => {
    console.error(error);
    return null;
});

console.log("V1 CANDY MACHINE", result);


// V2 candy machine
request.candy_machine_id = "4m1NuyoW87ZRHByQQ4frWaApbNARNLXjebf59fTcGAv1";
request.network = "mainnet-beta";
request.candy_machine_contract_version = 'v2'; // You have to specify the version. You can find the version here: https://docs.theblockchainapi.com/#operation/solanaGetAccountIsCandyMachine

opts = {
  'getCandyMetadataRequest': request
};

result = await apiInstance.solanaGetCandyMachineMetadata(opts).then((data) => {
    console.log('API called successfully.');
    return data;
}, (error) => {
    console.error(error);
    return null;
});

console.log("V2 CANDY MACHINE", result);