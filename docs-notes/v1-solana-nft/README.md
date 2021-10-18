Metaplex enables you to store a link tied to a non-fungible token. What is actually stored on the blockchain? A link, a name, a symbol, a token, and proof that the
supply of the token is one. There are two important notes regarding the link. 1) You can store anything you want in the link. It can be a video, an image, or data. 2) To make it fully decentralized, you
would want to store the file on some decentralized storage such as Arweave or IPFS. We enable you to easily store it on our end via Amazon S3 (centralized)
or provide the link yourself. While our API does not currently provide easy access to Arweave or IPFS, you can store it there first and then provide that link.


*You may have seen simple explanations on creating an NFT on Solana. Such processes consider creating a token with a supply of one and then 
turning off the ability to mint more of the token. However, you cannot store any other data with the token besides a name and symbol. This defeats
many use cases. The Metaplex API protocol enables the storing of a single link along with the token, but it is difficult to use and difficult to get working. 
This API enables you to use the protocol in a flexible, easy, and reliable way.*


*[EIP-721](https://eips.ethereum.org/EIPS/eip-721) is the protocol for NFTs on Ethereum, which Metaplex follows.*


*This endpoint takes approximately 50-65 seconds to complete. After completion, the NFT is minted.*