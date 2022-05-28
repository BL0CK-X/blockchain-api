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

let blockchain = 'ethereum';
let network = 'mainnet'; // or `ropsten`
let unit = 'ether';
let blockchain_identifier = '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045';
let usdc_identifier = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48';

// let blockchain = 'solana';
// let network = 'mainnet-beta';  // `devnet`
// let unit = 'sol';
// let blockchain_identifier = 'DbjWJmYbn4dA4atBJsMKpwM9R72z18HLJc8ws8ekDhmY';
// let usdc_identifier = 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v';

// ------- EXAMPLE #1: GET SOL/ETH BALANCE

const balance_request = new theblockchainapi.GeneralBalanceRequest();

balance_request.blockchain_identifier = blockchain_identifier;
balance_request.network = network;
balance_request.unit = unit;

let opts = {
  'generalBalanceRequest': balance_request
};

let balance_result = await apiInstance.getBalance(blockchain, opts).then((data) => {
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

const get_balance = async (my_blockchain_identifier, token_blockchain_identifier) => {

    const my_balance_request = new theblockchainapi.BalanceRequest(); // BalanceRequest |
    my_balance_request.blockchain_identifier = my_blockchain_identifier;
    my_balance_request.token_blockchain_identifier = token_blockchain_identifier;
    my_balance_request.network = network;

    const opts = {
      'generalBalanceRequest': my_balance_request
    };

    let my_balance_result = await new theblockchainapi.WalletApi().getBalance(blockchain, opts).then((data) => {
      console.log('API called successfully.');
      return data;
    }, (error) => {
      console.error(error);
      return error;
    });
    return my_balance_result;
}

balance_result = await get_balance(
    blockchain_identifier,
    usdc_identifier
);
console.log("USDC Balance Retrieved: ", balance_result);


// ------- EXAMPLE #3: Get NFT Balance (Either 0 or 1)

if (blockchain == 'ethereum') {
    // Ethereum
    // We have an NFT from this collection: 0x1542B05412Dfecd80E734929F9087f8766934275
    // We know that the address 0xE3Ad30ee62126ee4f82894683c7Eb5a42264b536 DOES NOT OWN an NFT from this collection.
    // We know that the address 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045 OWNS an NFT from this collection.

    balance_result = await get_balance(
        '0xE3Ad30ee62126ee4f82894683c7Eb5a42264b536',
        '0x1542B05412Dfecd80E734929F9087f8766934275'
    );
    console.log("Balance should be 0 because they do NOT own an NFT. ", balance_result);

    balance_result = await get_balance(
        '0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045',
        '0x1542B05412Dfecd80E734929F9087f8766934275'
    );
    console.log("Balance should be at least one 1 because they own at least one NFT. ", balance_result);

} else {

    // Solana
    // We have an NFT: 4zH3Rwm1QXdfTSUqsYmeUBY4QqQmQEXJVbv4ErSK736Q
    // We know that the public key GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ DOES NOT OWN this NFT.
    // We know that the public key 31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj OWNS this NFT.

    balance_result = await get_balance(
        'GKNcUmNacSJo4S2Kq3DuYRYRGw3sNUfJ4tyqd198t6vQ',
        '4zH3Rwm1QXdfTSUqsYmeUBY4QqQmQEXJVbv4ErSK736Q'
    );
    console.log("Balance should be 0 because they do NOT own the NFT. ", balance_result);

    balance_result = await get_balance(
        '31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj',
        '4zH3Rwm1QXdfTSUqsYmeUBY4QqQmQEXJVbv4ErSK736Q'
    );
    console.log("Balance should be 1 because they own the NFT. ", balance_result);

}
