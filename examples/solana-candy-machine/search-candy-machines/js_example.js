import theblockchainapi from 'theblockchainapi';

let defaultClient = theblockchainapi.ApiClient.instance;

// Get a free API Key Pair here: https://dashboard.theblockchainapi.com/api-keys

let APIKeyID = defaultClient.authentications['APIKeyID'];
APIKeyID.apiKey = 'API-KEY-ID';

let APISecretKey = defaultClient.authentications['APISecretKey'];
APISecretKey.apiKey = 'API-SECRET-KEY';

let apiInstance = new theblockchainapi.SolanaCandyMachineApi();

const search_candy_machines = async (request, title) =>  {
    let result = await apiInstance.solanaSearchCandyMachines(
        {
          'candyMachineSearchRequest': request
        }
    ).then((data) => {
      console.log('API called successfully.');
      return data;
    }, (error) => {
      console.error(error);
      return null;
    });
    console.log(title);
    console.log(result);
    console.log("----------------------------------");
};

let request = new theblockchainapi.CandyMachineSearchRequest(); // CandyMachineSearchRequest |
request.update_authority = '31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj';
request.network = 'mainnet-beta';
request.candy_machine_contract_version = 'v1';
await search_candy_machines(request, "Searching for candy machines with an update authority of `31LKs39pjT5oj6fWjC3F76dHWf9489asCthmgj8wu7pj`.");

request = new theblockchainapi.CandyMachineSearchRequest(); // CandyMachineSearchRequest |
request.symbol = 'SOL';
request.symbol_search_method = 'begins_with';
request.candy_machine_contract_version = 'v2';
request.network = 'mainnet-beta';
await search_candy_machines(request, "Searching for candy machines that have a symbol that begins with `SOL`.");

request = new theblockchainapi.CandyMachineSearchRequest(); // CandyMachineSearchRequest |
request.symbol = 'SOL';
request.symbol_search_method = 'exact_match';
request.candy_machine_contract_version = 'v2';
request.network = 'mainnet-beta';
await search_candy_machines(request, "Searching for candy machines that have the symbol `SOL`.");

request = new theblockchainapi.CandyMachineSearchRequest(); // CandyMachineSearchRequest |
request.nft_name = 'Genesis';
request.nft_name_index = 0;
request.nft_name_search_method = 'begins_with';
request.candy_machine_contract_version = 'v2';
request.network = 'mainnet-beta';
await search_candy_machines(request, "Searching for candy machines whose first stored NFT has a name that begins with `Genesis`.");


request = new theblockchainapi.CandyMachineSearchRequest(); // CandyMachineSearchRequest |
request.uuid = '3qt9aB';
request.candy_machine_contract_version = 'v2';
request.network = 'mainnet-beta';
await search_candy_machines(request, "Searching for candy machines with the uuid `3qt9aB` (there should only be one).");
