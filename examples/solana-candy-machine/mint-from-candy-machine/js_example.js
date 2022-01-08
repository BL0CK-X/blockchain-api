import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

const network = 'devnet';

//// First, we create a wallet, get an airdrop three times, use that airdrop to create a test candy machine, and then mint from the candy machine.

// Let's create a new wallet with a balance of 0.

// First, generate a new seed phrase.

let apiInstance = new theblockchainapi.SolanaWalletApi();

const new_seed_phrase = await apiInstance.solanaGenerateSecretRecoveryPhrase().then((data) => {
    return data['secret_recovery_phrase'];
}, (error) => {
    console.error(error);
    return null;
});
console.log("New Seed Phrase: ", new_seed_phrase);

// Then, derive a public key owned by the seed phrase.

let getPublicKeyRequest = new theblockchainapi.GetPublicKeyRequest(); // GetPublicKeyRequest | 
getPublicKeyRequest.wallet = {
  secret_recovery_phrase: new_seed_phrase
};

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
balance_request.network = network;
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
for (let i = 0; i < 3; i++) {
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
}

// Get the balance after the airdrop
await getBalance();

// Now mint the NFT
// We need to make sure the airdrops have time to process before creating the candy machine
await new Promise(r => setTimeout(r, 30000));

const candy_request = new theblockchainapi.CreateTestCandyMachineRequest(); // CreateTestCandyMachineRequest |
candy_request.wallet = {
  secret_recovery_phrase: new_seed_phrase
};
candy_request.candy_machine_contract_version = 'v2';
candy_request.network = network;

let candyApiInstance = new theblockchainapi.SolanaCandyMachineApi();
opts = {
  'createTestCandyMachineRequest': candy_request
};

const candy_machine_id = await candyApiInstance.solanaCreateTestCandyMachine(opts).then((data) => {
  console.log('API called successfully.');
  return data['candy_machine_id']
}, (error) => {
  console.error(error);
  return null;
});

if (candy_machine_id !== null) {
  console.log("Here is the candy machine ID.", candy_machine_id, "Now let's mint from it.")

  // We now need to get the configuration address to be able to send the mint API call

  const candy_details_request = new theblockchainapi.GetCandyMetadataRequest(); // GetCandyMetadataRequest |
  candy_details_request.candy_machine_id = candy_machine_id;
  candy_details_request.network = network;
  candy_details_request.candy_machine_contract_version = 'v2';

  opts = {
    'getCandyMetadataRequest': candy_details_request
  };

  const candy_machine_details = await candyApiInstance.solanaGetCandyMachineMetadata(opts).then((data) => {
    console.log('API called successfully.');
    return data;
  }, (error) => {
    console.error(error);
    return error;
  });

  const candy_machine_config_address = candy_machine_details['config_address'];

  console.log("Retrieved the Config Address:", candy_machine_config_address);

  let candyMachineApi = new theblockchainapi.SolanaCandyMachineApi();
  const request = new theblockchainapi.MintNFTRequest(); // MintNFTRequest |

  request.wallet = {
    secret_recovery_phrase: new_seed_phrase
  };
  request.config_address = candy_machine_config_address;
  request.candy_machine_contract_version = 'v2';
  request.network = network;

  opts = {
    'mintNFTRequest': request
  };

  const transactionSignature = await candyMachineApi.solanaMintFromCandyMachine(opts).then((data) => {
    console.log('API called successfully.');
    return data['transaction_signature'];
  }, (error) => {
    console.error(error);
    return null;
  });

  console.log("Transaction Signature: ", transactionSignature)

  console.log("Sleeping for 30 secs...")
  // Wait for the transaction to be confirmed... about 30 secs
  await new Promise(r => setTimeout(r, 30000));

  // Check TX success

  let txApiInstance = new theblockchainapi.SolanaTransactionApi();
  const txResult = await txApiInstance.solanaGetTransaction(network, transactionSignature).then((data) => {
    console.log('API called successfully.');
    return data;
  }, (error) => {
    console.error(error);
    return null;
  });

  console.log(txResult);
  const didSucceed = txResult['result']['meta']['err'] === null;
  console.log(txResult['result']['meta']['err']);
  console.log("Did the tx succeed? ", didSucceed);

  const url_to_view = "https://explorer.solana.com/tx/" + transactionSignature + "?cluster=" + network;
  console.log("You can view the transaction here: ", url_to_view)
} else {
  console.log("ERROR. Please try again.")
}
