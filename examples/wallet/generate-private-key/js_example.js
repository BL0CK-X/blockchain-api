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

//const blockchain = 'solana';
const blockchain = 'ethereum';
//const blockchain = 'avalanche';
//const blockchain = 'near';
//const blockchain = 'binance_smart_chain';

const test = async (blockchain, seed_phrase, derivation_path, passphrase) => {
    console.log(" BEGIN ------------------------");

    console.log(seed_phrase);

    let getPublicKeyRequest = new theblockchainapi.SupplyWalletRequest(); // GetPublicKeyRequest |
    getPublicKeyRequest.wallet = {
        secret_recovery_phrase: seed_phrase,
        derivation_path: derivation_path,
        passphrase: passphrase
    }

    const private_key = await apiInstance.generatePrivateKey(blockchain, getPublicKeyRequest).then((data) => {
        console.log('API called successfully.');
        return data;
    }, (error) => {
        console.error(error);
        return null;
    });

    if (blockchain == 'solana') {
        const b58_private_key = private_key['b58_private_key'];
        console.log("This is a base58-encoded private key. This is what Phantom shows when you click `Show Private Key`");
        console.log(b58_private_key);

        console.log("------------------------");

        const private_key_arr = private_key['private_key'];
        console.log("This is a standard private key array. This is what SolFlare shows when you click `Export Private Key`");
        console.log(private_key_arr);
    } else if (blockchain == 'ethereum' || blockchain == 'binance_smart_chain') {
        const hex_private_key = private_key['hex_private_key'];
        console.log("This is a hex-encoded private key. You can import this into Metamask.");
        console.log(hex_private_key);
    } else if (blockchain == 'avalanche') {
        const hex_private_key = private_key['hex_private_key'];
        console.log("This is a hex-encoded private key. You can import this into wallet.avax.network/access/privatekey.");
        console.log(hex_private_key);
        console.log("However, to import it successfully, remove the `0x`.");
        console.log(hex_private_key.slice(2));
    } else if (blockchain == 'near') {
        const private_key_arr = private_key['private_key'];
        console.log(
            "This is a standard private key array. However, wallet.near.org currently only supports using a seed phrase."
        );
        console.log(private_key_arr);
    } else {
        console.log(JSON.stringify(private_key));
    }


    console.log(" END: ------------------------");

}

if (blockchain == 'solana') {
    await test(blockchain, 'sadness swap zebra path panda power finger robot yellow game list enemy', 'm/44/501/0/0', '');
    await test(blockchain, 'sadness swap zebra path panda power finger robot yellow game list enemy', 'm/44/501/1/0', '');
    await test(blockchain, 'sadness swap zebra path panda power finger robot yellow game list enemy', 'm/44/501/0/0', 'apple');
    await test(blockchain, 'fire owner display success half rescue pledge oval foam gossip window once', 'm/44/501/0/0', '');
} else {
    await test(blockchain, 'sadness swap zebra path panda power finger robot yellow game list enemy', null, null);
}