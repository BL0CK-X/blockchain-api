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

let apiInstance = new theblockchainapi.WalletApi();

let getPublicKeyRequest = new theblockchainapi.SupplyWalletRequest();

//const blockchain = 'solana';
const blockchain = 'ethereum';
//const blockchain = 'avalanche';
//const blockchain = 'near';
//const blockchain = 'binance_smart_chain';

const avalanche_chain = 'P'; // can be `X`, `C`, `P`

const seed_phrase = 'sadness swap zebra path panda power finger robot yellow game list enemy';

if (blockchain == 'solana') {
    getPublicKeyRequest.wallet = {
      secret_recovery_phrase: seed_phrase,
      derivation_path: 'm/44/501/0/0',
      passphrase: ''
    }

    const result = await apiInstance.deriveWalletIdentifier(blockchain, getPublicKeyRequest).then((data) => {
      console.log('API called successfully.');
      return data['public_key'];
    }, (error) => {
      console.error(error);
      return null;
    });

    console.log("Public Key: ", result);
} else {

    getPublicKeyRequest.wallet = {
      secret_recovery_phrase: seed_phrase,
      derivation_path: null,
      passphrase: null,
      avalanche_chain: avalanche_chain
    }
    const result = await apiInstance.deriveWalletIdentifier(blockchain, getPublicKeyRequest).then((data) => {
      return data;
    }, (error) => {
      console.error(error);
      return null;
    });

    console.log('API called successfully.');

    if (blockchain == 'ethereum' || blockchain == 'binance_smart_chain' || (blockchain == 'avalanche' && avalanche_chain == 'C')) {
        console.log(result['hex_public_address']);
    } else if (blockchain == 'avalanche') {
        console.log(result['bech_public_address']);
    } else if (blockchain == 'near') {
        console.log(result['hex_public_key']);
    }
}

