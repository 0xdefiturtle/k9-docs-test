# InstantPool

[_<mark style="color:yellow;">Link to InstantPool source code on Ethereum</mark>_](https://etherscan.io/address/0xe83e2397d73f306cbc21b132f6d40ba71d10cc8c#code)

InstantPool contract is responsible for the instant BONE payout. When user requests such instant payout, this contracts allows user to receive their BONE tokens instantly without creating a withdrawal request.  The fee `instantPoolUsageFee` is applied to such payout.

### Variables

<mark style="color:orange;">`bytes32 public constant PAUSE_ROLE = keccak256("PAUSE_ROLE");`</mark> - pauser role identifier\
<mark style="color:orange;">`bytes32 public constant UNPAUSE_ROLE = keccak256("UNPAUSE_ROLE");`</mark> - unpauser role identifier\
<mark style="color:orange;">`bytes32 public constant WITHDRAWER_ROLE = keccak256("WITHDRAWER_ROLE");`</mark> - withdrawer role identifier

### Methods

### initialize

```
function initialize(address _dao, address _knBONE) external initializer
```

Initializer function, not called after initialization. The following roles are granted:

* DEFAULT\_ADMIN\_ROLE - DAO (admin)
* WITHDRAWER\_ROLE - KnBONE contract

### withdraw

```
function withdraw(IERC20Upgradeable token, address receiver, uint256 amount) 
     external 
     whenNotPaused 
     onlyRole(WITHDRAWER_ROLE) 
```

Transfers the specified amount of the specified token (BONE) to receiver.&#x20;

### pause

```
function pause() external onlyRole(PAUSE_ROLE)
```

&#x20;Pauses the InstantPool contract.

### unpause

```
function unpause() external onlyRole(UNPAUSE_ROLE) 
```

Unpauses the InstantPool contract.
