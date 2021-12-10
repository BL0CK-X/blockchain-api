import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = null;

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = null;

const get_is_nft = async (public_key, network, title) =>  {
    let apiInstance = new theblockchainapi.SolanaAccountApi();

    const result = await apiInstance.solanaGetAccountIsNFT(network, public_key).then((data) => {
       return data['is_nft'];
     }, (error) => {
       console.error(error);
       return null;
     });

     console.log(title, "Is NFT?", result)
     console.log("----------------------------------")
}


// Get an NFT
await get_is_nft("EEr5yQpNXf7Bru6Rt5podx56HGW9CEehXqgRGh2wa71w", 'mainnet-beta', "NFT Account")

// Get an SPL Token
await get_is_nft("SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt", 'mainnet-beta', "SPL Token")

// Get smart contract
await get_is_nft("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 'mainnet-beta', "Smart Contract")

// Get an associated token account
await get_is_nft("3CdXPzAgY72HnaReerSXhfaJa5WiBj6ftgsTB9sv6RKJ", 'mainnet-beta', "Associated Token Account")

// Get candy machine account
await get_is_nft("9htmDvW58pjCMQdjFbovo8cGBZviDfeP3j7DKnikHEy5", 'mainnet-beta', "Candy Machine Account")

// Get a system program (wallet account, such as the public key to your wallet)
await get_is_nft("31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj", 'mainnet-beta', "System Program")
