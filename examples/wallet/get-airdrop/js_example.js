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
let transactionApiInstance = new theblockchainapi.TransactionApi();

// ---- Generates 12 words by default
//const blockchain = 'solana';
const blockchain = 'ethereum';

let network;
if (blockchain == 'solana') {
    // solana
    network = 'devnet';
} else {
    // ethereum
    network = 'ropsten';
}

// Let's create a new wallet with a balance of 0.

// First, generate a new seed phrase.

const new_seed_phrase = await apiInstance.generateSeedPhrase(blockchain).then((data) => {
    return data['secret_recovery_phrase'];
}, (error) => {
    console.error(error);
    return null;
});
console.log("Seed Phrase: ", new_seed_phrase);

// Then, derive a public key owned by the seed phrase.

let supplyWalletRequest = new theblockchainapi.SupplyWalletRequest();
supplyWalletRequest.wallet = {
    secret_recovery_phrase: new_seed_phrase
};

let wallet_identifier;

if (blockchain == 'solana') {
    wallet_identifier = await apiInstance.deriveWalletIdentifier(blockchain, supplyWalletRequest).then((data) => {
      console.log('API called successfully.');
      return data['public_key'];
    }, (error) => {
      console.error(error);
      return null;
    });
    console.log("Wallet Identifier (public key): ", wallet_identifier);
} else {
    wallet_identifier = await apiInstance.deriveWalletIdentifier(blockchain, supplyWalletRequest).then((data) => {
      console.log('API called successfully.');
      return data['hex_public_address'];
    }, (error) => {
      console.error(error);
      return null;
    });
    console.log("Wallet Identifier (hex public address): ", wallet_identifier);
}

// Finally, get the balance of that public key on the devnet, measured in SOL (not LAMPORT, 1e9 LAMPORT in 1 SOL)

async function getBalance() {

    const balance_request = new theblockchainapi.GeneralBalanceRequest(); // BalanceRequest |

    balance_request.blockchain_identifier = wallet_identifier;
    balance_request.network = network;

    if (blockchain == 'solana') {
        // solana
        balance_request.unit = 'sol';
    } else {
        // ethereum
        balance_request.unit = 'ether';
    }

    let opts = {
      'generalBalanceRequest': balance_request
    };

    console.log(balance_request);

    const balance_result = await apiInstance.getBalance(blockchain, opts).then((data) => {
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
const airdrop_request = new theblockchainapi.GeneralAirdropRequest();

airdrop_request.recipient_blockchain_identifier = wallet_identifier;
airdrop_request.network = network;

const tx_id = await apiInstance.getAirdrop(
    blockchain,
    {
        'generalAirdropRequest': airdrop_request
    }
    ).then((data) => {
        console.log('API called successfully.');
        return data['transaction_blockchain_identifier'];
    }, (error) => {
        console.error(error);
        return null;
    }
);


const max_attempts = 10;

for (let i = 0; i < max_attempts; i++) {
    const tx = await transactionApiInstance.getTransaction(blockchain, network, tx_id).then((data) => {
      return data;
    }, (error) => {
      console.error(error);
      return null;
    });
    if (tx == null) {
        console.log("Waiting for transaction to become final.... Attempt #" + string(i) + " of " + max_attempts);
        await new Promise(r => setTimeout(r, 90000));
    } else {
        console.log(data);
        break;
    }
}


if (blockchain == 'solana') {
    // solana
    console.log("You can view the Airdrop transaction here: https://explorer.solana.com/tx/" + tx_id + "?cluster=devnet");
} else {
    // solana
    console.log("You can view the Airdrop transaction here: https://ropsten.etherscan.io/tx/" + tx_id);
}

console.log(airdrop_request);

// Get the balance after the airdrop
await getBalance();