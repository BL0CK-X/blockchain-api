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


// ---- Uncomment this to use `Solana`
let blockchain = 'solana';
let unit = 'sol';
let network = 'devnet';

// ---- Uncomment this to use `Ethereum`
//let blockchain = 'ethereum';
//let unit = 'ether';
//let network = 'ropsten';

const token_blockchain_identifier = null;
const return_compiled_transaction = false; // If you return the compiled transaction, you don't have to provide a wallet address.
let sender_blockchain_identifier = null;
let new_seed_phrase = null;
let new_blockchain_identifier = null;
let getBalance = async () => {};

// Let's create a new wallet with a balance of 0.

// First, generate a new seed phrase.

if (!return_compiled_transaction) {

    new_seed_phrase = await apiInstance.generateSeedPhrase(blockchain).then((data) => {
        return data['secret_recovery_phrase'];
    }, (error) => {
        console.error(error);
        return null;
    });
    console.log("Seed Phrase: ", new_seed_phrase);

    // Then, derive a public key owned by the seed phrase.

    let getWalletIdentifierRequest = new theblockchainapi.SupplyWalletRequest();
    getWalletIdentifierRequest.wallet = {
      secret_recovery_phrase: new_seed_phrase
    };

    new_blockchain_identifier = await apiInstance.deriveWalletIdentifier(blockchain, getWalletIdentifierRequest).then((data) => {
      console.log('API called successfully.');
      if (blockchain == 'solana') {
        return data['public_key'];
      } else {
        return data['hex_public_address'];
      }
    }, (error) => {
      console.error(error);
      return null;
    });

    console.log("Wallet Address: ", new_blockchain_identifier);

    // Finally, get the balance of that public key on the devnet, measured in SOL (not LAMPORT, 1e9 LAMPORT in 1 SOL)

    const balance_request = new theblockchainapi.GeneralBalanceRequest(); // BalanceRequest |
    balance_request.blockchain_identifier = new_blockchain_identifier;
    balance_request.network = network;
    balance_request.unit = unit;

    let opts = {
      'generalBalanceRequest': balance_request
    };

    getBalance = async () => {
        const balance_result = await apiInstance.getBalance(
            blockchain,
            opts
        ).then((data) => {
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
    airdrop_request.recipient_blockchain_identifier = new_blockchain_identifier;

    let n_airdrops;
    if (blockchain == 'solana') {
        n_airdrops = 1;
    } else {
        n_airdrops = 3;
    }

    for (let i = 0; i < n_airdrops; i++) {
        const airdrop_tx_sig = await apiInstance.getAirdrop(
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
        });

        if (blockchain == 'solana') {
            console.log("You can view the transfer transaction here: https://explorer.solana.com/tx/" + airdrop_tx_sig + "?cluster=" + network);
        } else {
            if (network == 'ropsten') {
                console.log("You can view the transfer transaction here: https://ropsten.etherscan.io/tx/" + airdrop_tx_sig);
            } else {
                console.log("You can view the transfer transaction here: https://etherscan.io/tx/" + airdrop_tx_sig);
            }
        }
    }

    // Get the balance after the airdrop
    await getBalance();

} else {

    if (blockchain == 'solana') {
        sender_blockchain_identifier = 'DbjWJmYbn4dA4atBJsMKpwM9R72z18HLJc8ws8ekDhmY';
    } else {
        sender_blockchain_identifier = '0x8C77020c1fe8353c6b72198293E5A217aCF7463E';
    }

}


// Transfer that airdrop!

const transfer_request = new theblockchainapi.GeneralTransferRequest();

if (blockchain == 'solana') {
    transfer_request.recipient_blockchain_identifier = '31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj'; // Feel free to change to your public key address!
} else {
    transfer_request.recipient_blockchain_identifier = '0x80013Bd2C223437f5D46a01aFB28EfE624f2f8C0'; // Feel free to change to your address!
}

if (!return_compiled_transaction) {
    transfer_request.wallet = {
      secret_recovery_phrase: new_seed_phrase
    };
}

transfer_request.network = network;
transfer_request.amount = '0.014'; // The airdrop was 0.015, but we need to send a little less to pay for the transaction.

if (blockchain == 'solana') {
    transfer_request.amount = '0.014'; // The airdrop was 0.015, but we need to send a little less to pay for the transaction.
} else {
    transfer_request.amount = '0.0005'; // The airdrop was 0.001, but we need to send a little less to pay for the transaction.
}
transfer_request.return_compiled_transaction = return_compiled_transaction; // Instead
transfer_request.token_blockchain_identifier = null; // Transfer a token such as USDC or an NFT
transfer_request.sender_blockchain_identifier = sender_blockchain_identifier;

const transfer_response = await apiInstance.transfer(
        blockchain,
        {
            'generalTransferRequest': transfer_request
        }
    ).then((data) => {
    console.log('API called successfully.');
    if (return_compiled_transaction) {
        return data;
    }
    return data['transaction_blockchain_identifier'];
}, (error) => {
    console.error(error);
    return null;
});

if (return_compiled_transaction) {
    console.log("Instructions (You can submit this via Metamask, Phantom, etc.): ", transfer_response);
} else {
    if (blockchain == 'solana') {
        console.log("You can view the transfer transaction here: https://explorer.solana.com/tx/" + transfer_response + "?cluster=" + network);
    } else {
        if (network == 'ropsten') {
            console.log("You can view the transfer transaction here: https://ropsten.etherscan.io/tx/" + transfer_response);
        } else {
            console.log("You can view the transfer transaction here: https://etherscan.io/tx/" + transfer_response);
        }
    }
}


// Get the balance after the airdrop

await getBalance();