# BridgeETH

[_<mark style="color:yellow;">Link to BridgeETH source code on Ethereum</mark>_](https://etherscan.io/address/0x21a1405b9f8a1a07befd1bd39af1785a10c1bff0#code)

BridgeETH contract is the Ethereum part of the K9-owned bridge. This bridge is used only by K9 Finance DAO for the platform purposes to transfer knBONE tokens from Ethereum to Shibarium and backwards.

## Variables

<mark style="color:orange;">`bytes32 public constant DAO_ROLE = keccak256("DAO_ROLE");`</mark> - dao role identifier\
<mark style="color:orange;">`bytes32 public constant VALIDATOR_ROLE = keccak256("VALIDATOR_ROLE");`</mark> - bridge validator role identifier\
<mark style="color:orange;">`bytes32 public constant PAUSE_ROLE = keccak256("PAUSE_ROLE");`</mark> - pauser role identifier\
<mark style="color:orange;">`bytes32 public constant UNPAUSE_ROLE = keccak256("UNPAUSE_ROLE");`</mark> - unpauser role identifier\
\
<mark style="color:orange;">`uint256 public minSignatures;`</mark> - minimum number of signatures from validators to accept a transaction\
\
<mark style="color:orange;">`uint256 public nextTransactionIDFromThisNetwork;`</mark> - the next transactionID that will be assigned to a transaction of this network\
\
<mark style="color:orange;">`IKnBONE public knBONE`</mark> - knBONE contract interface\
\
<mark style="color:orange;">`address public feeReceiver;`</mark> - bridging fee receiver address\
\
<mark style="color:orange;">`mapping(uint256 => mapping(uint256 => bool)) public processedTransaction;`</mark> - for each network, for each `in` and `out` transaction , it shows whether it was processed or not

## Events

<mark style="color:orange;">`event Deposit(uint256 indexed transactionID, address indexed from, address indexed to, uint256 amount);`</mark> - upon _depositForUser_ call (when user submits)\
<mark style="color:orange;">`event Execute(uint256 indexed chainID, uint256 indexed transactionID, uint8 indexed withdrawStatus);`</mark> - upon _execute_ call (processing an incoming transaction)

## Methods

### initialize

```
function initialize(
           address _dao, 
           address _feeReceiver, 
           IKnBONE _knBONE, 
           address[] calldata _validators, 
           uint256 _minSignatures) 
     external initializer
```

Initializer function, not called after initialization

### depositForUser

```
function depositForUser(address receiver, uint256 amount) 
     external 
     whenNotPaused 
     nonReentrant
```

&#x20;When user have done the deposit to protocol, claims the knBONE amount of the associated deposit to further transfer it from Ethereum to Shibarium.

### execute

```
function execute(
           uint256 chainID, 
           uint256 transactionID, 
           address receiver, 
           uint256 amountToReceive, 
           uint256 feeAmount, 
           uint256 _instantPoolAmount, 
           uint256 _requestWithdrawAmount, 
           bytes[] calldata signatures) 
           external 
     whenNotPaused 
     nonReentrant
```

Processes the incoming transaction of deposit or withdrawal.

If the `_instantPoolAmount` or/and `_requestWithdrawAmount` values are not zero, then it means that user wants to unstake from the protocol, so this function tries to unstake from knBONE contract with the specified parameters on behalf of the receiver. If zero, then user's deposit is processed.

{% hint style="warning" %}
It is necessary that there are at least minimum _minSignatures_ signatures from unique addresses having VALIDATOR\_ROLE in the signatures array.
{% endhint %}

### simulateExecute

```
function simulateExecute(uint256 chainID, 
           uint256 transactionID, 
           address receiver, 
           uint256 amountToReceive, 
           uint256 feeAmount, 
           uint256 _instantPoolAmount, 
           uint256 _requestWithdrawAmount) 
     external 
     whenNotPaused 
     nonReentrant
```

Does the same as `execute()` only without signatures - needed for simulation to check if the `execute()` will work on user call. Any chainID and transactionID may be specified.

{% hint style="warning" %}
Available only when the _sender_ is a zero address.
{% endhint %}

### setMinSignatures

```
function setMinSignatures(uint256 _minSignatures) external onlyRole(DAO_ROLE)
```

Sets minSignatures, cannot be set to 0.

### setFeeReceiver

```
function setFeeReceiver(address _feeReceiver) external onlyRole(DAO_ROLE)
```

Sets feeReceiver, cannot be set to 0 address.

### pause

```
function pause() external onlyRole(PAUSE_ROLE)
```

Pauses the BridgeETH contract.

### unpause

```
function unpause() external onlyRole(UNPAUSE_ROLE)
```

Unpauses the BridgeETH contract.
