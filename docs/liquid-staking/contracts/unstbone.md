# UnstBONE

[_<mark style="color:yellow;">Link to UnstBONE source code on Ethereum</mark>_](https://etherscan.io/address/0xe9f0954974c1cf68f7ee9b7fc217e6371dbeb1b5#code)

UnstBONE contract is an ERC721 contract used by the KnBONE contract to manage withdrawal requests.&#x20;

## Variables

<mark style="color:orange;">`address public knBONE;`</mark> - knBONE contract address.\
\
<mark style="color:orange;">`uint256 public tokenIdIndex;`</mark> - _totalSupply_ value of the contract. Burned NFTs are not taken into account, so it shows how many tokens were minted.\
\
<mark style="color:orange;">`mapping(address => uint256[]) public owner2Tokens;`</mark> - for each address returns an array of tokens that this address owns.\
<mark style="color:orange;">`mapping(uint256 => uint256) public token2Index;`</mark> - for each token returns the index in the _owner2Tokens_ array.\
<mark style="color:orange;">`mapping(address => uint256[]) public address2Approved;`</mark> - for each address returns an array of tokens that have been approved for this address. Does not take into account approvals via _approvalForAll_.\
<mark style="color:orange;">`mapping(uint256 => uint256) public tokenId2ApprovedIndex;`</mark> - for each approved token returns the index in the returned array _address2Approved._

## Modifiers

<mark style="color:orange;">`isKnBONE()`</mark> - requires the function caller to be knBONE.

## Methods

### initialize

```
function initialize(
        address _knBONE,
        address _dao
    ) external initializer
```

\- initializer function, not called after initialization.

### mint

```
function mint(address _to) external isKnBONE returns (uint256)
```

Mint new token.

{% hint style="info" %}
&#x20;tokenID starts from 1, not from 0
{% endhint %}

### burn

```
function burn(uint256 _tokenId) external isKnBONE
```

Burns the token.

### approve

```
function approve(address _to, uint256 _tokenId)
        public
        override(ERC721Upgradeable, IERC721Upgradeable)
```

Rewritten 'approval' from ERC721, in addition to what it usually does, it also interacts with _address2Approved_ and _tokenId2ApprovedIndex._

### isApprovedOrOwner

```
function isApprovedOrOwner(address _spender, uint256 _tokenId)
        external
        view
        returns (bool)
```

Shows whether the spender is authorized to use the token (approved or owned). An approve that was made via _approvalForAll_ is taken into account.

### setKnBONE

```
function setKnBONE(address _knBONE) external onlyOwner
```

Sets knBONE contract address.

### getOwnedTokens

```
function getOwnedTokens(address _address)
        external
        view
        returns (uint256[] memory)
```

Duplicates _owner2Tokens -_ for each address returns an array of tokens that this address owns.

### getApprovedTokens

```
function getApprovedTokens(address _address)
        external
        view
        returns (uint256[] memory)
```

Duplicates address2Approved - for each address returns an array of tokens that have been approved for this address. Does not take into account approvals via _approvalForAll_.

### togglePause

```
function togglePause() external onlyOwner
```

Switches pause on/off.
