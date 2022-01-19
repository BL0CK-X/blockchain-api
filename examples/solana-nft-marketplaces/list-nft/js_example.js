import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.blockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

// (1) Create a new wallet and get a SOL airdrop

let walletApiInstance = new theblockchainapi.SolanaWalletApi();

const private_key = await walletApiInstance.solanaGeneratePrivateKey().then((data) => {
  return data;
}, (error) => {
  console.error(error);
  return null;
});

const b58_private_key = private_key['b58_private_key'];
console.log("This is a base58-encoded private key. This is what Phantom shows when you click `Show Private Key`");
console.log(b58_private_key);
console.log("------")

// Then, derive a public key owned by the seed phrase.

let getPublicKeyRequest = new theblockchainapi.GetPublicKeyRequest(); // GetPublicKeyRequest |
getPublicKeyRequest.wallet = {
    'b58_private_key': b58_private_key
};

const public_key = await walletApiInstance.solanaDerivePublicKey(getPublicKeyRequest).then((data) => {
  console.log('API called successfully.');
  return data['public_key'];
}, (error) => {
  console.error(error);
  return null;
});

console.log("Public Key: ", public_key);

const getAirdrop = async (public_key) => {
    // Now get an airdrop
    const airdrop_request = new theblockchainapi.AirdropRequest();
    airdrop_request.recipient_address = public_key;

    const tx_sig = await walletApiInstance.solanaGetAirdrop({
        'airdropRequest': airdrop_request
        }).then((data) => {
        console.log('0.015 SOL airdrop received called successfully.');
        return data['transaction_signature'];
    }, (error) => {
        console.error(error);
        return null;
    });
}

await getAirdrop(public_key);
await getAirdrop(public_key);
await getAirdrop(public_key);

// (2) Create an NFT

let nftApiInstance = new theblockchainapi.SolanaNFTApi();

const nftMintRequest = new theblockchainapi.NFTMintRequest(); // NFTMintRequest

nftMintRequest.wallet = {
    'b58_private_key': b58_private_key
}

let opts = {
  'nFTMintRequest': nftMintRequest // NFTMintRequest |
};

const nft_result = await nftApiInstance.solanaCreateNFT(opts).then((data) => {
  console.log('NFT created successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});
const mintAddress = nft_result['mint'];
console.log("NFT Mint Address:", mintAddress);

const getNftOwner = async (network, mintAddress) => {
    let apiInstance = new theblockchainapi.SolanaNFTApi();

    const result = await apiInstance.solanaGetNFTOwner(network, mintAddress).then((data) => {
      return data;
    }, (error) => {
      console.error(error);
      return null;
    });

    const nft_owner = result['nft_owner'];

    console.log("Retrieved the NFT Owner: " + nft_owner)
}

let network = 'devnet'; // String | The network ID (devnet, mainnet-beta)

console.log("We are the owner.")
getNftOwner(network, mintAddress);

// (3) List the NFT

let marketplaceApi = new theblockchainapi.SolanaNFTMarketplacesApi();
let exchange = 'solsea';
// let exchange = 'magic-eden'; // Uncomment this line to use Magic Eden

let listRequest =  new theblockchainapi.ListRequest() // SolSeaListRequest |
listRequest.wallet = {
  'b58_private_key': b58_private_key
};
listRequest.nft_price = 20;  // 20 lamports, NOT SOL
let listOpts = {
  'listRequest': listRequest
};

let result = await marketplaceApi.solanaListNFT(network, exchange, mintAddress, listOpts).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

console.log(result);

console.log("We are no longer the owner because the NFT is held in escrow. We can remove it at anytime by delisting and thus put it back in our wallet..")
getNftOwner(network, mintAddress);

// (4) Get the listing

let listingDetails = await marketplaceApi.solanaGetNFTListing(network, mintAddress).then((data) => {
  return data;
}, (error) => {
  console.error(error);
  return null;
});

console.log(listingDetails);

// (5) Delist the NFT

let delistRequest =  new theblockchainapi.DelistRequest() // DelistRequest |
delistRequest.wallet = {
  'b58_private_key': b58_private_key
};
let delistOpts = {
  'delistRequest': delistRequest
};


result = await marketplaceApi.solanaDelistNFT(network, exchange, mintAddress, delistOpts).then((data) => {
  console.log('API called successfully.');
  return data;
}, (error) => {
  console.error(error);
  return null;
});

console.log(result);
console.log("We are the owner again.")
getNftOwner(network, mintAddress);