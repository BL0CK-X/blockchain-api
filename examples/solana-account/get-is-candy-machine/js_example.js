import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair: https://dashboard.blockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

const get_is_candy_machine = async (public_key, network, title) =>  {
    let apiInstance = new theblockchainapi.SolanaAccountApi();

    const result = await apiInstance.solanaGetAccountIsCandyMachine(network, public_key).then((data) => {
       return data;
     }, (error) => {
       console.error(error);
       return null;
     });

     console.log(title, "Is Candy Machine?", result)
     console.log("----------------------------------")
}


// Get an NFT
await get_is_candy_machine(
    "EEr5yQpNXf7Bru6Rt5podx56HGW9CEehXqgRGh2wa71w", 'mainnet-beta', "NFT Account"
)

// Get an SPL Token
await get_is_candy_machine(
    "SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt", 'mainnet-beta', "SPL Token"
)

// Get smart contract
await get_is_candy_machine(
    "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", 'mainnet-beta', "Smart Contract"
)

// Get an associated token account
await get_is_candy_machine(
    "3CdXPzAgY72HnaReerSXhfaJa5WiBj6ftgsTB9sv6RKJ", 'mainnet-beta', "Associated Token Account"
)

// Get candy machine account, v1 smart contract
await get_is_candy_machine(
    "9htmDvW58pjCMQdjFbovo8cGBZviDfeP3j7DKnikHEy5", 'mainnet-beta', "Candy Machine Account"
)

// Get candy machine account, v2 smart contract
await get_is_candy_machine(
    "C3gQisQbf2tHdiwTJPXjV3AoYkZg6vsmKvtCkhxM9oP4", "mainnet-beta", "Candy Machine Account: v2"
)

// Get candy machine account, Magic Eden
await get_is_candy_machine(
    "8eF9sgCopyfMo5JBLCLxCdwBvU1WvKG2y56hcgdJ43Fc", "mainnet-beta", "Candy Machine Account: Magic Eden V1"
)

// Get a system program (wallet account, such as the public key to your wallet)
await get_is_candy_machine(
    "31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj", 'mainnet-beta', "System Program"
)
