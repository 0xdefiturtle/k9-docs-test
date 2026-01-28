# BridgeSHIB

[_<mark style="color:yellow;">Link to BridgeETH source code on Shibarium</mark>_](https://www.shibariumscan.io/address/0x21a1405B9f8a1a07BEfD1Bd39af1785A10c1bFf0?tab=contract)

BridgeSHIB contract is the Shibarium part of the K9-owned bridge. This bridge is used only by K9 Finance DAO for the platform purposes to transfer knBONE tokens from Shibarium to Ethereum and backwards.

## Variables

<mark style="color:orange;">`bytes32 public constant DAO_ROLE = keccak256("DAO_ROLE");`</mark> - dao role identifier\
<mark style="color:orange;">`bytes32 public constant VALIDATOR_ROLE = keccak256("VALIDATOR_ROLE");`</mark> - bridge validator role identifier\
<mark style="color:orange;">`bytes32 public constant ACCEPTOR_ROLE = keccak256("ACCEPTOR_ROLE");`</mark> - role identifier of the recipient of the transaction\
<mark style="color:orange;">`bytes32 public constant PAUSE_ROLE = keccak256("PAUSE_ROLE");`</mark> - pauser role identifier\
<mark style="color:orange;">`bytes32 public constant UNPAUSE_ROLE = keccak256("UNPAUSE_ROLE");`</mark> - unpauser role identifier\
\
<mark style="color:orange;">`uint256 public minSignatures;`</mark> - minimum number of signatures from validators to accept a transaction\
\
<mark style="color:orange;">`uint256 public nextTransactionIDFromThisNetwork;`</mark> - the next _transactionID_ that will be assigned to a transaction leaving this network\
\
<mark style="color:orange;">`IKnBONESHIB knBONE;`</mark> - knBONE contract interface\
\
<mark style="color:orange;">`mapping(uint256 => bool) public acceptedSignature;`</mark> - for each nonce of an outgoing transaction, it shows whether it was accepted or not, this is necessary as protection against signature replay of transaction receivers\
<mark style="color:orange;">`mapping(uint256 => mapping(uint256 => bool)) public processedTransaction;`</mark> - for each network, for each `in` and `out` transaction , it shows whether it was processed or not

## Events

<mark style="color:orange;">`event Deposit(uint256 indexed transactionID, address indexed from, address indexed to, uint256 amountToReceive, uint256 feeAmount, uint256 _instantPoolAmount, uint256 _requestWithdrawAmount);`</mark> - upon _depositForUserOrUnstake_ call (when user submits or unstakes)\
<mark style="color:orange;">`event Execute(uint256 indexed chainID, uint256 indexed transactionID);`</mark> - upon _execute_ call (processing an incoming transaction)

## Methods

### initialize

```
function initialize(
           address _dao, 
           IKnBONESHIB _knBONE, 
           address _acceptor, 
           address[] calldata _validators, 
           uint256 _minSignatures) 
     external 
     initializer
```

Initializer function, not called after initialization.

### depositForUserOrUnstake

```
function depositForUserOrUnstake(
            address receiver, 
            uint256 amountToReceive, 
            uint256 feeAmount, 
            uint256 _instantPoolAmount, 
            uint256 _requestWithdrawAmount, 
            uint256 signatureNonce, 
            uint256 signatureDeadline, 
            bytes calldata signature) 
     external 
     whenNotPaused 
     nonReentrant
```

Allows the user to _transfer_ tokens from Shibarium to Ethereum or _transfer and unstake_.

If _transfer and unstake_, the `receiver` must match the `sender` of the transaction.&#x20;

{% hint style="warning" %}
The transaction receiver signature  is required.
{% endhint %}

### execute

```
function execute(
           uint256 chainID, 
           uint256 transactionID, 
           address receiver, 
           uint256 amount, bytes[] 
           calldata signatures) 
     external 
     whenNotPaused 
     nonReentrant
```

Executes a transaction from the origin network.

{% hint style="warning" %}
It is necessary that there are at least minimum _minSignatures_ signatures from unique addresses having VALIDATOR\_ROLE in the signatures array.
{% endhint %}

### setMinSignatures&#x20;

```
function setMinSignatures(uint256 minSignatures) 
     external 
     onlyRole(DAO_ROLE)
```

Sets minSignatures, cannot be set to 0.

### pause

```
function pause() external onlyRole(PAUSE_ROLE)
```

Pauses the BridgeSHIB contract.

### unpause

```
function unpause() external onlyRole(UNPAUSE_ROLE)
```

Unpauses the BridgeSHIB contract.
