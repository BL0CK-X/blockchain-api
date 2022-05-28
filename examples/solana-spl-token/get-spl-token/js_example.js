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

const get_spl_token = async(pub_key, title, network) => {
    console.log(title)
    let apiInstance = new theblockchainapi.SolanaSPLTokenApi();
    const data = await apiInstance.solanaGetSPLToken(pub_key, network).then((data) => {
        console.log('API called successfully. Returned data: ' + data);
        return data;
    }, (error) => {
        console.log('Error! Not found or wrong network. Log error for more details.')
        // console.error(error);
    });
    console.log(data);
}

// Get an NFT -- actually an SPL token behind the scenes!
await get_spl_token("EEr5yQpNXf7Bru6Rt5podx56HGW9CEehXqgRGh2wa71w", "NFT Account", "mainnet-beta")

// Get an SPL Token
await get_spl_token("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v", "USDC Token", "mainnet-beta")

// Get an SPL Token
await get_spl_token("MangoCzJ36AjZyKwVj3VnYU4GTonjfVEnJmvvWaxLac", "Mango Token", "mainnet-beta")

// Get an SPL Token
await get_spl_token("SRMuApVNdxXokk5GT7XD5cUUgXMBCoAz2LHeuAoKWRt", "Serum Token", "mainnet-beta")

// Get smart contract
await get_spl_token("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", "Smart Contract", "mainnet-beta")

// Get candy machine account, v1
await get_spl_token(
    "9htmDvW58pjCMQdjFbovo8cGBZviDfeP3j7DKnikHEy5", "Candy Machine Account: v1", "mainnet-beta"
)

// Get candy machine account, v2
await get_spl_token(
    "C3gQisQbf2tHdiwTJPXjV3AoYkZg6vsmKvtCkhxM9oP4", "Candy Machine Account: v2", "mainnet-beta"
)

// Get candy machine account, magic-eden
await get_spl_token(
"8eF9sgCopyfMo5JBLCLxCdwBvU1WvKG2y56hcgdJ43Fc", "Candy Machine Account: Magic Eden v1", "mainnet-beta"
)

// Get a system program (wallet account, such as the public key to your wallet)
await get_spl_token("31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj", "System Program", "mainnet-beta")