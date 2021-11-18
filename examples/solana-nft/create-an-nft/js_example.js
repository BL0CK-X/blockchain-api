import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

///// Here, we create a new wallet, get an airdrop, and then use the airdrop to mint an NFT.

// Let's create a new wallet with a balance of 0.

// First, generate a new seed phrase.

let apiInstance = new theblockchainapi.SolanaWalletApi();

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

// Get the balance after the airdrop
await getBalance();

// Now mint the NFT
// We need to make sure the airdrops have time to process before minting the NFT!
await new Promise(r => setTimeout(r, 30000));

let nftApiInstance = new theblockchainapi.SolanaNFTApi();

const nftMintRequest = new theblockchainapi.NFTMintRequest(); // NFTMintRequest

// https://github.com/BL0CK-X/theblockchainapi-wrappers/blob/b951a8300869f97d8e2336156d1af85ebb705c02/go/model_nft_mint_request.go#L19
nftMintRequest.secret_recovery_phrase = new_seed_phrase;
nftMintRequest.nft_name = 'Blockchain API NFT'
nftMintRequest.nft_symbol = 'BLOCKX'

opts = {
  'nFTMintRequest': nftMintRequest // NFTMintRequest | 
};

const nft_result = await nftApiInstance.solanaCreateNFT(opts).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

// Display the NFT details

console.log(nft_result);


