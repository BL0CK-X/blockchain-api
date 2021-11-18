import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaWalletApi();

// Let's create a new wallet with a balance of 0.

// First, generate a new seed phrase.

const new_seed_phrase = await apiInstance.solanaGenerateSecretRecoveryPhrase().then((data) => {
    return data['secret_recovery_phrase'];
}, (error) => {
    console.error(error);
    return null;
});
console.log("Seed Phrase: ", new_seed_phrase);

// Then, derive a public key owned by the seed phrase.

let getPublicKeyRequest = new theblockchainapi.GetPublicKeyRequest(); // GetPublicKeyRequest | 
getPublicKeyRequest.secret_recovery_phrase = new_seed_phrase;

const public_key = await apiInstance.solanaDerivePublicKey(getPublicKeyRequest).then((data) => {
  console.log('API called successfully.');
  return data['public_key'];
}, (error) => {
  console.error(error);
  return null;
});

console.log("Public Key: ", public_key);

// Finally, get the balance of that public key on the devnet, measured in SOL (not LAMPORT, 1e9 LAMPORT in 1 SOL)

const balance_request = new theblockchainapi.BalanceRequest(); // BalanceRequest | 
balance_request.public_key = public_key;
balance_request.network = 'devnet';
balance_request.unit = 'sol';

let opts = {
  'balanceRequest': balance_request
};

async function getBalance() {
    const balance_result = await apiInstance.solanaGetBalance(opts).then((data) => {
        console.log('API called successfully.');
        return data;
    }, (error) => {
        console.error(error);
        return error;
    });
    
    console.log("Balance Retrieved: ", balance_result);
}

// Get the balance before the airdrop
await getBalance();

// Now get an airdrop
const airdrop_request = new theblockchainapi.AirdropRequest();
airdrop_request.recipient_address = public_key;

const airdrop_tx_sig = await apiInstance.solanaGetAirdrop({
    'airdropRequest': airdrop_request
  }).then((data) => {
  console.log('API called successfully.');
  return data['transaction_signature'];
}, (error) => {
  console.error(error);
  return null;
});
console.log("You can view the Airdrop transaction here: https://explorer.solana.com/tx/" + airdrop_tx_sig + "?cluster=devnet");

console.log(airdrop_request);

// Get the balance after the airdrop
await getBalance();


// Transfer that airdrop!

const transfer_request = new theblockchainapi.TransferRequest(); // TransferRequest | 
transfer_request.recipient_address = '31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj'; // Feel free to change to your public key address!
transfer_request.secret_recovery_phrase = new_seed_phrase;
// transfer_request.derivation_path = ''; // We're using the defaults.
// transfer_request.passphrase = ''; // We're using the defaults.
// transfer_request.token_address = ...; // Don't provide when transferring SOL.
transfer_request.network = 'devnet';
transfer_request.amount = '0.014'; // The airdrop was 0.015, but we need to send a little less to pay for the transaction.

const tx_sig = await apiInstance.solanaTransfer({
        'transferRequest': transfer_request
    }).then((data) => {
    console.log('API called successfully.');
    return data['transaction_signature'];
}, (error) => {
    console.error(error);
    return null;
});
console.log("You can view the transfer transaction here: https://explorer.solana.com/tx/" + tx_sig + "?cluster=devnet");


// Get the balance after the airdrop

await getBalance();