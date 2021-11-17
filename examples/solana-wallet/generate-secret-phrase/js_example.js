import TheBlockchainApi from 'the-blockchain-api';

let defaultClient = TheBlockchainApi.ApiClient.instance;

// Get a pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'Cq9ZAF48Cnnabsf';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'JbarbHL84eOGkSF';

let apiInstance = new TheBlockchainApi.SolanaWalletApi();
const req = apiInstance.solanaWalletSecretRecoveryPhrasePost(
    (error, data, response) => {
        if (error) {
            console.error(error);
            return null;
        } else {
            console.log('API called successfully. Returned data: ' + JSON.stringify(data));
            return data["secret_recovery_phrase"]
        }
    }
);

// asfunction getProjectParameterValue() {
//     return apiInstance.solanaWalletSecretRecoveryPhrasePost(
//         (error, data, response) => {
//             if (error) {
//                 console.error(error);
//                 resolve(null);
//             } else {
//                 console.log('API 22222 called successfully. Returned data: ' + JSON.stringify(data));
//                 // resolve(data["secret_recovery_phrase"])
//                 return data["secret_recovery_phrase"]
//             }
//         }
//     );
// }
// const result = getProjectParameterValue();
console.log("result", req);
// console.log( req);
// req.then((v)= );
// console.log(secret_phrase);