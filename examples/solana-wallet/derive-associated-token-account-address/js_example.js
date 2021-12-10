import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaWalletApi();

// https://explorer.solana.com/address/7EWJNaNYfPYMaqzdAAa4ps5kpqW95B7VHsjhW1kr18sj
const nft_on_mainnet_beta_address = '7EWJNaNYfPYMaqzdAAa4ps5kpqW95B7VHsjhW1kr18sj';

// https://explorer.solana.com/address/FmKrVEUKqnpQwGX5kbxR4HB5GZuZaGFdwKkhAKUKC5zA?cluster=devnet
const nft_on_devnet_address = 'FmKrVEUKqnpQwGX5kbxR4HB5GZuZaGFdwKkhAKUKC5zA';

// https://explorer.solana.com/address/SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt
const serum_token_address = "SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt";

const request = new theblockchainapi.GetPublicKeyRequest(); // ATARequest |

request.secret_recovery_phrase = 'sadness swap zebra path panda power finger robot yellow game list enemy';
request.derivation_path = 'm/44/501/0/0';
request.passphrase = '';

// First, derive your public key.
// You can replace this with your public key here. This way, you won't have to provide a seed phrase.
let getPublicKeyRequest = new theblockchainapi.GetPublicKeyRequest(); // GetPublicKeyRequest |
getPublicKeyRequest.secret_recovery_phrase = 'sadness swap zebra path panda power finger robot yellow game list enemy';
getPublicKeyRequest.derivation_path = 'm/44/501/0/0';
getPublicKeyRequest.passphrase = '';

const public_key = await apiInstance.solanaDerivePublicKey(getPublicKeyRequest).then((data) => {
  console.log('API called successfully.');
  return data['public_key'];
}, (error) => {
  console.error(error);
  return null;
});

console.log("Public Key: ", public_key);


const get_ata = async (public_key, mint_address) => {
    return await apiInstance.solanaDeriveAssociatedTokenAccountAddress(public_key, mint_address).then((data) => {
      console.log('API called successfully.');
      return data['associated_token_address'];
    }, (error) => {
      console.error(error);
      return null;
    });
}

// (1) ... Associated token address for an NFT on mainnet-beta
let ata = await get_ata(public_key, nft_on_mainnet_beta_address);
console.log('Associated Token Account Address for NFT on mainnet-beta: ', ata);


// (2) ... Associated token address for an NFT on devnet
ata = await get_ata(public_key, nft_on_devnet_address);
console.log('Associated Token Account Address for NFT on devnet: ', ata)


// (3) ... Associated token address for a Serum token
ata = await get_ata(public_key, serum_token_address);
console.log('Associated Token Account Address for Serum on mainnet-beta: ', ata)