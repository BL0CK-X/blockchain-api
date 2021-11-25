import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaWalletApi();

// ------- EXAMPLE #1: GET SOL BALANCE

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

// Then get an airdrop so that we have a nonzero balance
const airdrop_request = new theblockchainapi.AirdropRequest();
airdrop_request.recipient_address = public_key;

const tx_sig = await apiInstance.solanaGetAirdrop({
    'airdropRequest': airdrop_request
  }).then((data) => {
  console.log('API called successfully.');
  return data['transaction_signature'];
}, (error) => {
  console.error(error);
  return null;
});
console.log("You can view the Airdrop transaction here: https://explorer.solana.com/tx/" + tx_sig + "?cluster=devnet");

console.log(airdrop_request);

// Finally, get the balance of that public key on the devnet, measured in SOL (not LAMPORT, 1e9 LAMPORT in 1 SOL)

const balance_request = new theblockchainapi.BalanceRequest(); // BalanceRequest | 
balance_request.public_key = public_key;
balance_request.network = 'devnet';
balance_request.unit = 'sol';

let opts = {
  'balanceRequest': balance_request
};

const balance_result = await apiInstance.solanaGetBalance(opts).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return error;
});

console.log("SOL Balance Retrieved: ", balance_result);

// ------- EXAMPLE #2: GET USDC BALANCE
// We know that the public key GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ has some USDC belonging to it.
// We have also retrieved the USDC mint address, EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
// You can see some popular ones here:
// https://raw.githubusercontent.com/solana-labs/token-list/main/src/tokens/solana.tokenlist.json

const balance_request_two = new theblockchainapi.BalanceRequest(); // BalanceRequest |
balance_request_two.public_key = 'GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ';
balance_request_two.mint_address = 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v';
balance_request_two.network = 'mainnet-beta';

opts = {
  'balanceRequest': balance_request_two
};

const balance_result_two = await apiInstance.solanaGetBalance(opts).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return error;
});

console.log("USDC Balance Retrieved: ", balance_result_two);
