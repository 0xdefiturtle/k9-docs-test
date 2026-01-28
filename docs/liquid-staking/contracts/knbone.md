# knBONE

[_<mark style="color:yellow;">Link to knBONE source code on Ethereum</mark>_ ](https://etherscan.io/address/0x3358fca51d7c0408750fbbe7777012e0b67c027f#code)

[_<mark style="color:yellow;">Link to knBONE source code on Shibarium</mark>_](https://www.shibariumscan.io/address/0x3358FCA51d7C0408750FBbE7777012E0b67C027F?tab=contract)

knBONE is the core contract which acts as a liquid staking pool. The contract is responsible for deposits, withdrawals, minting and burning liquid tokens, delegating funds to node operators, applying fees and distributing rewards.

knBONE contract also defines knBONE, an ERC20 token that represents the account's share of the BONE tokens inside K9 Finance DAO protocol. It is a non-rebasable token, which means that the amount of tokens in the user's wallet is not going to change by itself, only by user actions. During time, the value of this token is changing, since the amount of BONE tokens inside the protocol is not constant. knBONE will be integrated in variety of DeFi applications across Ethereum and Shibarium.

knBONE  is inherited from IKnBONE, ERC20Upgradeable, AccessControlUpgradeable, PausableUpgradeable

## Variables

<mark style="color:orange;">`IERC20Upgradeable public token;`</mark> - BONE token address\
\
<mark style="color:orange;">`INodeOperatorRegistry public nodeOperatorRegistry;`</mark> - NodeOpeartorRegistry contract address\
\
<mark style="color:orange;">`IStakeManager public stakeManager;`</mark> - Shibarium StakeManager contract address\
<mark style="color:orange;">`IUnstBONE public unstBONE;`</mark> - UnstBONE contract address\
\
<mark style="color:orange;">`IInstantPool public instantPool;`</mark> - InstantPool contract address\
\
<mark style="color:orange;">`IDepositManager public depositManager;`</mark> - DepositManager address of the bridge in Shibarium (this bridge is owned by K9 Finance DAO)\
\
<mark style="color:orange;">`IBridge public bridge;`</mark> - Bridge contract address in Ethereum\
\
<mark style="color:orange;">`address public l2Staking;`</mark> - Real Yield Staking contract address that will receive a share of rewards from Liquid Staking\
\
<mark style="color:orange;">`address public dao;`</mark> - DAO Treasury reward address (this address does not necessarily have a DAO role) that will receive a share of rewards from Liquid Staking\
\
<mark style="color:orange;">`FeeDistribution public entityFees;`</mark> - Protocol fee distribution structure\
\
<mark style="color:orange;">`uint256 public instantPoolUsageFee;`</mark> - Fee percentage that user pays when withdrawing instant reward\
\
<mark style="color:orange;">`uint256 public totalBuffered;`</mark> - amount of BONE that is buffered but not delegated, includes reservedFunds\
\
<mark style="color:orange;">`uint256 public delegationLowerBound;`</mark> - the minimum required for successful delegate() on this contract\
\
<mark style="color:orange;">`uint256 public rewardDistributionLowerBound;`</mark> - the minimum reward amount that is required for successful distributeRewards() on this contract\
\
<mark style="color:orange;">`uint256 public reservedFunds;`</mark> - replenished if, when creating a request from a user, some amount did not fit into our requests to validators (included in totalBuffered)\
\
<mark style="color:orange;">`bytes32 public constant DAO_ROLE = keccak256("DAO_ROLE");`</mark> - dao role identifier\
<mark style="color:orange;">`bytes32 public constant PAUSE_ROLE = keccak256("PAUSE_ROLE");`</mark> - pauser role identifier\
<mark style="color:orange;">`bytes32 public constant UNPAUSE_ROLE = keccak256("UNPAUSE_ROLE");`</mark> - unpauser role identifier\
\
<mark style="color:orange;">`bytes32 public constant BRIDGE_ROLE = keccak256("BRIDGE_ROLE");`</mark> - bridge executor role identifier (should be granted to bridge)\
\
<mark style="color:orange;">`RequestWithdraw[] public knBONEWithdrawRequest;`</mark> - an array of withdrawal request structures specifically for withdrawal to this contract (will be filled in only when creating a withdrawal request from the validator to KnBONE for reasons other than the user’s withdrawal, filled in when rebalanceDelegatedTokens() and withdrawTotalDelegated())\
\
<mark style="color:orange;">`mapping(uint256 => RequestWithdraw[]) public token2WithdrawRequests;`</mark> - for each unstBONE tokenID returns an array of withdrawal request structures\
\
<mark style="color:orange;">`uint8 public protocolFee;`</mark> - Protocol fee total percentage which will then be distributed in accordance with entityFees

## Structures

#### RequestWithdraw

Withdrawal requests structure

<table><thead><tr><th width="297">Name</th><th>Description</th></tr></thead><tbody><tr><td>uint256 amount2WithdrawFromKnBONE</td><td>BONE amount to withdraw</td></tr><tr><td>uint256 validatorNonce</td><td>filled in as <em>ValidatorShare.unboundNonces(address(this))</em> or 0 if the sub-application amount did not fit into our requests to validators</td></tr><tr><td>uint256 requestEpoch</td><td>when withdrawal is available, filled in as <em>StakeManager.epoch() + StakeManager.withdrawalDelay()</em></td></tr><tr><td>address validatorAddress</td><td>ValidatorShare address or zero address in case if the sub-request amount does not fit into our requests to validators</td></tr></tbody></table>



```
struct RequestWithdraw {
uint256 amount2WithdrawFromKnBONE;
uint256 validatorNonce;
uint256 requestEpoch;
address validatorAddress;
}
```

#### FeeDistribution

Protocol fee distribution structure

<table><thead><tr><th width="306">Name</th><th>Description</th></tr></thead><tbody><tr><td>dao</td><td>DAO Treasury protocol fee share</td></tr><tr><td>operators</td><td>Node operators protocol fee share</td></tr><tr><td>instantPool</td><td>Instant reward pool protocol fee share</td></tr><tr><td>staking</td><td>Real Yield Staking rewards protocol fee share</td></tr></tbody></table>

```
struct FeeDistribution {
uint8 dao; 
uint8 operators; 
uint8 instantPool;
uint8 staking;
}
```

## Events

<mark style="color:orange;">`event SubmitEvent(address indexed _from, uint256 _amount, address indexed _receiver, bool _transferToL2);`</mark> - upon submit() call

<mark style="color:orange;">`event InstantPoolWithdraw(address indexed _from, uint256 _amountWithFeeInBONE, uint256 _feeAmountInBONE);`</mark> - when withdrawing using only instant pool, BONE amounts are provided

<mark style="color:orange;">`event RequestWithdrawEvent(address indexed _from, uint256 _amountInBONE);`</mark> - when withdrawing using only withdrawal request, BONE amount is provided

<mark style="color:orange;">`event RequestWithdrawSplit(address indexed _from, uint256 _totalAmountInKnBONE);`</mark> - upon completion of the transaction requestWithdrawSplit(), amount knBONE amount is provided

<mark style="color:orange;">`event DistributeRewardsEvent(uint256 indexed _amount, uint256 indexed totalPooledBefore, uint256 indexed totalPooledAfter);`</mark> - upon distribureRewards() call

<mark style="color:orange;">`event WithdrawTotalDelegatedEvent(`</mark> \ <mark style="color:orange;">`address indexed _from, uint256 indexed _amount );`</mark> - upon withdrawTotalDelegated() call

<mark style="color:orange;">`event DelegateEvent(uint256 indexed _amountDelegated, uint256 indexed _remainder );`</mark> - upon delegate() call

<mark style="color:orange;">`eventClaimTokensEvent(address indexed _from, uint256 indexed _id, uint256 indexed _amountClaimed);`</mark> - upon claimTokens() call

<mark style="color:orange;">`event SetNodeOperatorRegistryAddress(address indexed _newNodeOperatorRegistryAddress );`</mark> - upon setNodeOperatorRegistryAddress() call

<mark style="color:orange;">`event SetDelegationLowerBound(uint256 indexed _delegationLowerBound);`</mark> - upon setDelegationLowerBound() call

<mark style="color:orange;">`event SetRewardDistributionLowerBound(uint256 oldRewardDistributionLowerBound, uint256 newRewardDistributionLowerBound );`</mark> - upon setRewardDistributionLowerBound() call

<mark style="color:orange;">`event SetUnstBONE(address oldUnstBONE, address newUnstBONE);`</mark> - upon setUnstBONE() call

<mark style="color:orange;">`event SetDaoAddress(address oldDaoAddress, address newDaoAddress);`</mark> - upon setDaoAddress() call

<mark style="color:orange;">`event SetFees(uint256 daoFee, uint256 operatorsFee, uint256 instantPoolFee, uint256 stakingFee);`</mark> - upon setFees() call

<mark style="color:orange;">`event SetProtocolFee(uint8 oldProtocolFee, uint8 newProtocolFee);`</mark> - upon setProtocolFee() call

<mark style="color:orange;">`event SetInstantPoolUsageFee(uint256 oldInstantPoolUsageFee, uint256 newInstantPoolUsageFee);`</mark>  - upon setInstantPoolUsageFee() call

<mark style="color:orange;">`event SetInstantPool(address instantPool);`</mark> - upon setInstantPool() call

<mark style="color:orange;">`event SetDepositManager(address depositManager);`</mark>- upon setDepositManager() call

<mark style="color:orange;">`event SetBridge(address bridge);`</mark> -  upon setBridge() call

<mark style="color:orange;">`event SetL2Staking(address l2Staking);`</mark> -  upon setL2Staking() call

<mark style="color:orange;">`event ClaimTotalDelegatedEvent(address indexed validatorShare, uint256 indexed amountClaimed );`</mark> - upon claimTokensFromValidatorToContract() call

## View functions

### name()[​](https://docs.polygon.lido.fi/contracts/st-matic#name) <a href="#name" id="name"></a>

```
function name() returns (string)
```

Returns the name of the token

### symbol()[​](https://docs.polygon.lido.fi/contracts/st-matic#symbol) <a href="#symbol" id="symbol"></a>

```
function symbol() returns (string)
```

Returns the symbol of the token, usually a shorter version of the name

### decimals()[​](https://docs.polygon.lido.fi/contracts/st-matic#decimals) <a href="#decimals" id="decimals"></a>

```
function decimals() returns (uint8)
```

Returns the number of decimals for getting user representation of a token amount.

### totalSupply()[​](https://docs.polygon.lido.fi/contracts/st-matic#totalsupply) <a href="#totalsupply" id="totalsupply"></a>

```
function totalSupply() returns (uint256)
```

Returns the amount of tokens in existence.

### balanceOf()[​](https://docs.polygon.lido.fi/contracts/st-matic#balanceof) <a href="#balanceof" id="balanceof"></a>

```
function balanceOf(address _account) returns (uint256)
```

Returns the amount of tokens owned by the `_account`

### getTotalWithdrawRequest

```
function getTotalWithdrawRequest()
        public
        view
        returns (RequestWithdraw[] memory)
```

Returns the entire knBONEWithdrawRequest array.

### getTotalStake

```
function getTotalStake(IValidatorShare _validatorShare)
        public
        view
        returns (uint256, uint256)
```

The same as _ValidatorShare.getTotalStake(address(this))._ API for getting total stake of this contract from validatorShare.

### getLiquidRewards

```
function getLiquidRewards(IValidatorShare _validatorShare)
        external
        view
        returns (uint256)
```

The same as _ValidatorShare.getLiquidRewards(address(this))._ API for liquid rewards of this contract from validatorShare.

### getTotalStakeAcrossAllValidators

```
function getTotalStakeAcrossAllValidators()
        public
        view
        returns (uint256)
```

Returns the BONE amount staked in all validators.

### getTotalPooledBONE

```
function getTotalPooledBONE() public view returns (uint256)
```

Returns total pooled BONE as\
&#xNAN;_&#x67;etTotalStakeAcrossAllValidators() +_ \
_totalBuffered +_ \
_calculatePendingBufferedTokens() -_ \
_reservedFunds_

### getToken2WithdrawRequests

```
function getToken2WithdrawRequests(uint256 _tokenId)
        external
        view
        returns (RequestWithdraw[] memory)
```

Returns the withdrawal request structure for tokenID.

### getBONEFromTokenId

```
function getBONEFromTokenId(uint256 _tokenId)
        external
        view
        returns (uint256)
```

Retrieves the amount of BONE that will be claimed from the unstBONE NFT request.

### convertKnBONEToBONE

```
function convertKnBONEToBONE(uint256 _amountInKnBONE)
        external
        view
        returns (
            uint256 amountInBONE,
            uint256 totalKnBONEAmount,
            uint256 totalPooledBONE
        )
```

Calculates BONE amount from the provided knBONE amount.

### convertBONEToKnBONE

```
function convertBONEToKnBONE(uint256 _amountInBONE)
        public
        view
        returns (
            uint256 amountInKnBONE,
            uint256 totalKnBONESupply,
            uint256 totalPooledBONE
        )
```

Calculates knBONE amount from the provided BONE amount.

## Methods

### initialize

```
function initialize(
        INodeOperatorRegistry _nodeOperatorRegistry,
        IERC20Upgradeable _token,
        address _dao,
        IStakeManager _stakeManager,
        IUnstBONE _unstBONE,
        IInstantPool _instantPool,
        IDepositManager _depositManager,
        IBridgeETH _bridge,
        address _l2Staking
    ) external initializer
```

Initializer function, not called after initialization.

### submit

```
function submit(uint256 _amount, address _receiver, bool _transferToL2)
        external
        whenNotPaused
        nonReentrant
        returns (uint256)
```

Send funds to knBONE contract and mint knBONE to receiver. Requires that msg.sender has approved \_amount of BONE to this contract.

{% hint style="info" %}
* \_amount - Amount of BONE sent from msg.sender to this contract&#x20;
* \_receiver - receiver address&#x20;
* \_transferToL2 - whether or not transfer knBONE to Shibarium
{% endhint %}

### requestWithdrawSplit

```
function requestWithdrawSplit(uint256 _instantPoolAmount, 
      uint256 _requestWithdrawAmount, address _user) 
       external 
       whenNotPaused 
       nonReentrant 
       returns(uint256)
```

Request withdrawal function, allows using the instant pool and/or creating requests. \
\_user must be the _sender_ or _any address_ if the function is called from BRIDGE\_EXECUTOR\_ROLE. When executed:

* knBONE amount of the withdrawal request is burned&#x20;
* knBONE amount that is withdrawn through the Instant pool is sent to the DAO Treasury address.

Returns _tokenID_ if there was a request or _0_ if there was no request.

{% hint style="info" %}
* \_instantPoolAmount - Amount of knBONE that is requested to withdraw using instant reward pool&#x20;
* \_requestWithdrawAmount - Amount of knBONE that is requested to withdraw using withdrawal request
* \_user - user to withdraw from
{% endhint %}

### delegate

```
function delegate() external whenNotPaused nonReentrant
```

Delegates the amount of BONE (totalBuffered - reservedFunds) to validator.

### claimTokens

```
function claimTokens(uint256[] calldata _tokenId) external whenNotPaused
```

Claims tokens from validator share and sends them to the user. Requires the processed withdrawal request associated with unstBONE NFT.

### distributeRewards

```
function distributeRewards() external whenNotPaused nonReentrant
```

Distributes the protocol rewards received from validator.&#x20;

{% hint style="info" %}
* Creates a variable _totalRewards_ equal to (contract balance - totalBuffered).&#x20;
* Calculates the protocol fee amount based on protocolFee%.&#x20;
* Then distributes the protocol fee amount according to the entity fees, the rest is added to totalBuffered for re-delegation.
{% endhint %}

### withdrawTotalDelegated

```
function withdrawTotalDelegated(address _validatorShare)
        external
        nonReentrant
```

Called only by NodeOperatorRegistry contract. Creates a withdrawal request of the total delegated amount from the specified ValidatorShare. Withdraws funds from stopped validator.

### rebalanceDelegatedTokens

```
function rebalanceDelegatedTokens() external onlyRole(DAO_ROLE)
```

Rebalane the system by request withdraw from the validators that contains more token delegated to them.

{% hint style="info" %}
* Calculates amountToReDelegate as \
  `(totalBuffered - reservedFunds + calculatePendingBufferedTokens())`.&#x20;
* Sends it into`NodeOperatorRegistry.getValidatorsRebalanceAmount()` and gets a response.&#x20;
* Based on the response, creates a withdrawal request for each `ValidatorShare`.&#x20;
{% endhint %}

### calculatePendingBufferedTokens

```
function calculatePendingBufferedTokens()
        public
        view
        returns (uint256 pendingBufferedTokens)
```

Calculate the total amount of BONE stored in knBONEWithdrawRequest array that can not be delegated.

### claimTokensFromValidatorToContract

```
function claimTokensFromValidatorToContract(uint256 _index)
        external
        whenNotPaused
        nonReentrant
```

Processes the specified request in _knBONEWithdrawRequest_. Claims tokens from validator share and sends them to the knBONE contract.

## Admin Methods

{% hint style="info" %}
This method can be called by ADMIN-only roles
{% endhint %}

### pause

```
function pause() external onlyRole(PAUSE_ROLE)
```

&#x20;Pause knBONE contract

### unpause

```
function unpause() external onlyRole(UNPAUSE_ROLE)
```

Unpause knBONE contract

## DAO Methods - setters

{% hint style="info" %}
These methods can be called by DAO-only roles
{% endhint %}

### setProtocolFee

```
function setProtocolFee(uint8 _newProtocolFee)
     external
     onlyRole(DAO_ROLE)
```

Sets protocolFee value that will be distributed between receivers.

### setInstantPoolUsageFee

```
function setInstantPoolUsageFee(uint256 _instantPoolUsageFee) 
     external 
     onlyRole(DAO_ROLE)
```

Sets fee percentage that user pays when withdrawing instant reward

### setDaoAddress

```
function setDaoAddress(address _newDAO)
      external 
      onlyRole(DAO_ROLE)
```

&#x20;Sets the DAO Treasury reward address

### setNodeOperatorRegistryAddress

<pre><code>function setNodeOperatorRegistryAddress(address _address)
<strong>     external
</strong><strong>     onlyRole(DAO_ROLE)
</strong></code></pre>

&#x20;Sets nodeOperatorRegistry address

### setInstantPool

```
function setInstantPoolUsageFee(uint256 _instantPoolUsageFee) 
     external 
     onlyRole(DAO_ROLE)
```

Sets InstantPool address

### setDepositManager

```
function setDepositManager(IDepositManager _depositManager) 
     external 
     onlyRole(DAO_ROLE)
```

Sets depositManager address

### setBridge

```
function setBridge(IBridge _bridge) external onlyRole(DAO_ROLE)
```

Sets K9 bridge address

### setL2Staking

```
function setL2Staking(address _l2Staking) external onlyRole(DAO_ROLE)
```

Sets Real Yield Staking address

### setDelegationLowerBound

```
function setDelegationLowerBound(uint256 _delegationLowerBound)
```

Function that sets new lower bound for delegation

### setRewardDistributionLowerBound

```
function setRewardDistributionLowerBound(
        uint256 _newRewardDistributionLowerBound
    ) external onlyRole(DAO_ROLE)
```

&#x20;Function that sets new lower bound for rewards distribution
