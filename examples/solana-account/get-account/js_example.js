import TheBlockchainApi from 'the-blockchain-api';

let defaultClient = TheBlockchainApi.ApiClient.instance;

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'latWiyo7TuuXnQx';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'i7VdMvuI5y74A6p';

let apiInstance = new TheBlockchainApi.SolanaAccountApi();

let network = "mainnet-beta"; // String | The network ID (devnet, mainnet-beta)
let publicKey = "EEr5yQpNXf7Bru6Rt5podx56HGW9CEehXqgRGh2wa71w"; // String | The public key of the account

apiInstance.solanaAccountNetworkPublicKeyGet(network, publicKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + JSON.stringify(data));
  }
});
