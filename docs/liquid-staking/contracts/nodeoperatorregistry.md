# NodeOperatorRegistry

[_<mark style="color:yellow;">Link to NodeOperatorRegistry source code on Ethereum</mark>_](https://etherscan.io/address/0xbbba91ad8978e27c15c57fee803bd95c32c60d0a#code)

The NodeOperatorRegistry contract is the core contract that allows node operators to participate in the K9 Finance liquid staking protocol. Node Operators participate on the protocol as validators and get rewarded for their work. A Node Operator gets added to the Registry by the DAO. Validator reward is distributed evenly amongst all active operators. The contract contains a list of operators, their public keys, and the logic for managing their state.

## Roles[​](https://docs.polygon.lido.fi/contracts/node-operators-registry#roles) <a href="#roles" id="roles"></a>

The NodeOperatorRegistry contract has the following roles

| Name                         | Description                                   |
| ---------------------------- | --------------------------------------------- |
| DAO\_ROLE                    | DAO role                                      |
| PAUSE\_ROLE                  | Allows to pause the contract                  |
| UNPAUSE\_ROLE                | Allows to unpause the contract                |
| ADD\_NODE\_OPERATOR\_ROLE    | Allows to add new node operator the contract  |
| REMOVE\_NODE\_OPERATOR\_ROLE | Allows to remove a node operator the contract |

## Variables

<mark style="color:orange;">`IStakeManager public stakeManager;`</mark> - Shibarium stakeManager contract address.

<mark style="color:orange;">`IKnBONE public knBONE;`</mark> - knBONE contract address.

<mark style="color:orange;">`bytes32 public constant DAO_ROLE = keccak256("DAO_ROLE");`</mark> - dao role identifier.

<mark style="color:orange;">`bytes32 public constant PAUSE_ROLE = keccak256("PAUSE_ROLE");`</mark> - pauser role identifier.

<mark style="color:orange;">`bytes32 public constant UNPAUSE_ROLE = keccak256("UNPAUSE_ROLE");`</mark> - unpauser role identifier.

<mark style="color:orange;">`bytes32 public constant ADD_NODE_OPERATOR_ROLE =`</mark>\ <mark style="color:orange;">`keccak256("ADD_NODE_OPERATOR_ROLE");`</mark> - role identifier of adding node operator authority

<mark style="color:orange;">`bytes32 public constant REMOVE_NODE_OPERATOR_ROLE =`</mark>\ <mark style="color:orange;">`keccak256("REMOVE_NODE_OPERATOR_ROLE");`</mark> - role identifier of removing node operator authority.

<mark style="color:orange;">`uint256 public DISTANCE_THRESHOLD_PERCENTS;`</mark> - the maximum number (percentage) at which the system considers itself balanced. The distance will be 100 in case where the operator’s minimum stake is equal to the maximum. The distance is calculated as `(max * 100) / min`.

<mark style="color:orange;">`uint256 public MAX_WITHDRAW_PERCENTAGE_PER_REBALANCE;`</mark> - the maximum percentage that can be withdrawn from the total delegated amount when rebalancing the system.

<mark style="color:orange;">`uint8 public MIN_REQUEST_WITHDRAW_RANGE_PERCENTS;`</mark> - a percentage added to the withdrawal percentage when withdrawing from validators. Applicable only when the system is in a balanced state. It is used to “split” the withdrawal between validators.&#x20;

Does not affect the withdrawal amount.&#x20;

_Example_: the total stake of the system is 100 BONE and there are 4 active validators. A user wants to withdraw 10 BONE, i.e. 10%.&#x20;

```
totalValidatorToWithdrawFrom =
            (((withdrawAmountPercentage + MIN_REQUEST_WITHDRAW_RANGE_PERCENTS) *
                length) / 100) +
            1;
```

Without this extra percentage value, user would have withdrawn from one validator:

```
totalValidatorToWithdrawFrom = (10 + 0) * 4 / 100 + 1 = 1
```

BUT if this value is applied and suppose it is equal to 15%, then he will withdraw from two validators.

```
totalValidatorToWithdrawFrom = (10 + 15) * 4 / 100 + 1 = 2
```

<mark style="color:orange;">`uint256[] public validatorIds;`</mark> - IDs of all validators in the protocol

<mark style="color:orange;">`mapping(uint256 => address) public validatorIdToRewardAddress;`</mark> - returns rewardAddress for each validator ID

<mark style="color:orange;">`mapping(address => uint256) public validatorRewardAddressToId;`</mark> - returns validator ID for each rewardAddress of the validator&#x20;

## Structs[​](https://docs.polygon.lido.fi/contracts/node-operators-registry#structs) <a href="#structs" id="structs"></a>

#### NodeOperatorStatus[​](https://docs.polygon.lido.fi/contracts/node-operators-registry#nodeoperatorstatus) <a href="#nodeoperatorstatus" id="nodeoperatorstatus"></a>

Node operator statuses

| Name     | Description                        |
| -------- | ---------------------------------- |
| INACTIVE | When the node operator is INACTIVE |
| ACTIVE   | When the node operator is ACTIVE   |
| JAILED   | When the node operator is JAILED   |
| EJECTED  | When the node operator is EJECTED  |
| UNSTAKED | When the node operator is UNSTAKED |

```
enum NodeOperatorRegistryStatus {
        INACTIVE,
        ACTIVE,
        JAILED,
        EJECTED,
        UNSTAKED
}
```

***

#### FullNodeOperatorRegistry[​](https://docs.polygon.lido.fi/contracts/node-operators-registry#fullnodeoperatorregistry) <a href="#fullnodeoperatorregistry" id="fullnodeoperatorregistry"></a>

| Name           | Description                                                            |
| -------------- | ---------------------------------------------------------------------- |
| validatorId    | Shibarium validator id                                                 |
| commissionRate | The commission rate applied by the validator on Shibarium stakeManager |
| validatorShare | The validatorShare contract address                                    |
| rewardAddress  | The validator reward address                                           |
| delegation     | The validator delegation status on Shibarium stakeManager              |
| status         | The validator status                                                   |

```
struct FullNodeOperatorRegistry {
        uint256 validatorId;
        uint256 commissionRate;
        address validatorShare;
        address rewardAddress;
        bool delegation;
        NodeOperatorRegistryStatus status;
}
```

***

#### ValidatorData[​](https://docs.polygon.lido.fi/contracts/node-operators-registry#validatordata) <a href="#validatordata" id="validatordata"></a>

The node operator data

| Name           | Description                                          |
| -------------- | ---------------------------------------------------- |
| validatorShare | The validatorShare contract address of the validator |
| rewardAddress  | The validator reward address                         |

```
struct ValidatorData {
        address validatorShare;
        address rewardAddress;
}
```

## Events

<mark style="color:orange;">`event AddNodeOperator(uint256 validatorId, address rewardAddress);`</mark> - new validator was added to the protocol\
\
<mark style="color:orange;">`event RemoveNodeOperator(uint256 validatorId, address rewardAddress);`</mark> - validator was removed from the protocol\
\
<mark style="color:orange;">`event RemoveInvalidNodeOperator(uint256 validatorId, address rewardAddress);`</mark> - an invalid validator was removed from the protocol\
\
<mark style="color:orange;">`event SetKnBONEAddress(address oldKnBONE, address newKnBONE);`</mark> - KnBONE contract address is set\
\
<mark style="color:orange;">`event SetRewardAddress(uint256 validatorId, address oldRewardAddress,address newRewardAddress);`</mark> - rewardAddress is set for the validator\
\
<mark style="color:orange;">`event SetDistanceThreshold(uint256 oldDistanceThreshold, uint256 newDistanceThreshold);`</mark>  - DISTANCE\_THRESHOLD\_PERCENTS is set\
\
<mark style="color:orange;">`event SetMinRequestWithdrawRange(uint8 oldMinRequestWithdrawRange, uint8 newMinRequestWithdrawRange);`</mark> - MIN\_REQUEST\_WITHDRAW\_RANGE\_PERCENTS is set\
\
<mark style="color:orange;">`event SetMaxWithdrawPercentagePerRebalance(uint256 oldMaxWithdrawPercentagePerRebalance, uint256 newMaxWithdrawPercentagePerRebalance);`</mark>  - MAX\_WITHDRAW\_PERCENTAGE\_PER\_REBALANCE is set\
\
<mark style="color:orange;">`event ExitNodeOperator(uint256 validatorId, address rewardAddress);`</mark> - the validator removed himself from the protocol

## View functions <a href="#view-methods" id="view-methods"></a>

### listDelegatedNodeOperators <a href="#view-methods" id="view-methods"></a>

```
function listDelegatedNodeOperators()
        external
        view
        returns (ValidatorData[] memory)
```

Returns an array of structures ValidatorData for all validators whose status ACTIVE and whose ValidatorShare.delegation() returns true.

### listWithdrawNodeOperators

```
function listWithdrawNodeOperators()
        external
        view
        returns (ValidatorData[] memory)
```

Returns an array of ValidatorData structures for all validators whose status is not INACTIVE.

### getValidatorsDelegationAmount

```
function getValidatorsDelegationAmount(uint256 _amountToDelegate)
        external
        view
        returns (
            ValidatorData[] memory validators,
            uint256[] memory operatorRatiosToDelegate,
            uint256 totalRatio
        )
```

Calculate how _totalBuffered_ should be delegated between the active validators, depending on if the system is balanced or not: &#x20;

* If the system is **balanced - r**eturns a list of validators with zero&#x73;**.**
* &#x20;If the system is **not balanced - r**eturns a list of validators, a list of shares and the total amount of shares, how to delegate these shares to validators.

{% hint style="info" %}
Will return an error if:

* the number of validators on the contract is 0
* there are no validators with the ACTIVE status and with ValidatorShare.delegation() == TRUE
* validators with EJECTED or UNSTAKED status are present&#x20;
{% endhint %}

### getValidatorsRebalanceAmount

```
function getValidatorsRebalanceAmount(uint256 _amountToReDelegate)
        external
        view
        returns (
            ValidatorData[] memory validators,
            uint256[] memory operatorRatiosToRebalance,
            uint256 totalRatio,
            uint256 totalToWithdraw
        )
```

Calculate how the system could be rebalanced depending on the current buffered tokens. This function utilizes MAX\_WITHDRAW\_PERCENTAGE\_PER\_REBALANCE.

If the system is **not balanced**, it will return

* a list of validators
* how many shares to withdraw from them
* the sum of shares
* the amount to withdraw that corresponds to the sum of shares.&#x20;

{% hint style="info" %}
Will return an error if:

* the number of validators on the contract is < 2
* there are no validators with the ACTIVE status and with ValidatorShare.delegation() = TRUE
* validators with EJECTED or UNSTAKED statuses are present&#x20;
* the system is balanced&#x20;
* totalToWithdraw value is 0 (if there is no need to transfer funds between validators to achieve the balanced state).&#x20;
{% endhint %}

### getValidatorsRequestWithdraw

```
function _getValidatorsRequestWithdraw()
        private
        view
        returns (
            ValidatorData[] memory activeValidators,
            uint256[] memory stakePerOperator,
            uint256 totalDelegated,
            uint256 minAmount,
            uint256 maxAmount
        )
```

Depending on whether the system is balanced and the amount to withdraw, it returns a list of validators the system can withdraw from:

* list of validators
* how much is delegated
* IDs of those who have delegated more than the average
* IDs of those who have delegated less than average
* how much can be withdrawn from each validator if the system is **not balanced**&#x20;
* how many validators can be withdrawn from if the system is **balanced**

### getNodeOperator

```
function getNodeOperator(uint256 _validatorId)
        external
        view
        returns (FullNodeOperatorRegistry memory nodeOperator)
```

Returns the validator information by ID.

### getNodeOperator

```
function getNodeOperator(address _rewardAddress)
        external
        view
        returns (FullNodeOperatorRegistry memory nodeOperator)
```

Returns the validator information by rewardAddress.

### getNodeOperatorStatus

```
 function getNodeOperatorStatus(uint256 _validatorId)
        external
        view
        returns (NodeOperatorRegistryStatus operatorStatus)
```

Returns operator status according to ID.

### getValidatorIds

```
function getValidatorIds()
        external
        view
        returns (uint256[] memory)
```

Return a list of all validator ids in the system.

### getProtocolStats

```
function getProtocolStats()
        external
        view
        returns (
            bool isBalanced,
            uint256 distanceMinMaxStake,
            uint256 minAmount,
            uint256 maxAmount
        )
```

Return the statistics about the protocol as a list:

* whether the system is balanced
* the distance between the maximum and minimum validator stake
* minimum validator stake
* maximum validator stake

### getStats

```
 function getStats()
        external
        view
        returns (
            uint256 inactiveNodeOperator,
            uint256 activeNodeOperator,
            uint256 jailedNodeOperator,
            uint256 ejectedNodeOperator,
            uint256 unstakedNodeOperator
        )
```

Returns the number of operators for each status.

## Methods[​](https://docs.polygon.lido.fi/contracts/node-operators-registry#methods) <a href="#methods" id="methods"></a>

### initialize

```
function initialize(
        IStakeManager _stakeManager,
        IKnBONE _knBONE,
        address _dao
    ) external initializer
```

Initializer function, not called after initialization.



### exitNodeOperatorRegistry[​](https://docs.polygon.lido.fi/contracts/node-operators-registry#exitnodeoperatorregistry) <a href="#exitnodeoperatorregistry" id="exitnodeoperatorregistry"></a>

```
function exitNodeOperatorRegistry() external nonReentrant
```

Exit the node operator registry. ONLY the owner of the node operator can call this function.

### removeInvalidNodeOperator[​](https://docs.polygon.lido.fi/contracts/node-operators-registry#removeinvalidnodeoperator) <a href="#removeinvalidnodeoperator" id="removeinvalidnodeoperator"></a>

```
function removeInvalidNodeOperator(uint256 _validatorId)
        external
        whenNotPaused
        nonReentrant
```

Remove a node operator from the system if the Node Operator is either Unstaked or Ejected.[**​**](https://docs.polygon.lido.fi/contracts/node-operators-registry#parameters-9)

### setRewardAddress <a href="#setrewardaddress" id="setrewardaddress"></a>

```
function setRewardAddress(address _newRewardAddress)
        external
        whenNotPaused
```

Update the reward address of a Node Operator. ONLY Operator owner can call this function

## Admin Methods <a href="#pasue" id="pasue"></a>

{% hint style="info" %}
This method can be called by ADMIN-only roles
{% endhint %}

### pause[​](https://docs.polygon.lido.fi/contracts/node-operators-registry#pasue) <a href="#pasue" id="pasue"></a>

```
function pause() external onlyRole(PAUSE_ROLE) 
```

Allows an authorized user with `PAUSE ROLE` to pause the NodeOperatorRegistry contract.

### unpause[​](https://docs.polygon.lido.fi/contracts/node-operators-registry#unpasue) <a href="#unpasue" id="unpasue"></a>

```
function unpause() external onlyRole(UNPAUSE_ROLE)
```

Allows an authorized user with `UNPAUSE ROLE` to unpause the NodeOperatorRegistry contract.

## DAO Methods[​](https://docs.polygon.lido.fi/contracts/node-operators-registry#dao-methods) <a href="#dao-methods" id="dao-methods"></a>

{% hint style="info" %}
These methods can be called by DAO-only roles.
{% endhint %}

### addNodeOperator <a href="#addnodeoperator" id="addnodeoperator"></a>

```
function addNodeOperator(uint256 _validatorId, address _rewardAddress)
        external
        onlyRole(ADD_NODE_OPERATOR_ROLE)
        nonReentrant
```

Add a new node operator to the system.[**​**](https://docs.polygon.lido.fi/contracts/node-operators-registry#parameters-11)

### removeNodeOperator <a href="#removenodeoperator" id="removenodeoperator"></a>

```
function removeNodeOperator(uint256 _validatorId)
        external
        onlyRole(REMOVE_NODE_OPERATOR_ROLE)
        nonReentrant
```

Remove a node operator from the system and withdraw total delegated tokens to it. ONLY DAO can execute this function.[**​**](https://docs.polygon.lido.fi/contracts/node-operators-registry#parameters-12)

### setKnBONEAddress[​](https://docs.polygon.lido.fi/contracts/node-operators-registry#setstmaticaddress) <a href="#setstmaticaddress" id="setstmaticaddress"></a>

```
function setKnBONEAddress(address _newKnBONE)
        external
        onlyRole(DAO_ROLE)
```

Allows the DAO to set the knBONE contract address.

### setDistanceThreshold[​](https://docs.polygon.lido.fi/contracts/node-operators-registry#setdistancethreshold) <a href="#setdistancethreshold" id="setdistancethreshold"></a>

```
function setDistanceThreshold(uint256 _newDistanceThreshold)
        external
        onlyRole(DAO_ROLE)
```

Allows the DAO to set the distance threshold for balancing the system.

### setMinRequestWithdrawRange[​](https://docs.polygon.lido.fi/contracts/node-operators-registry#setminrequestwithdrawrange) <a href="#setminrequestwithdrawrange" id="setminrequestwithdrawrange"></a>

```
function setMinRequestWithdrawRange(
        uint8 _newMinRequestWithdrawRangePercents
    ) external onlyRole(DAO_ROLE)
```

Allows the DAO to set the minimum request withdraw range to keep the system balanced

### setMaxWithdrawPercentagePerRebalance <a href="#setmaxwithdrawpercentageperrebalance" id="setmaxwithdrawpercentageperrebalance"></a>

```
setMaxWithdrawPercentagePerRebalance(
        uint256 _newMaxWithdrawPercentagePerRebalance
    ) external onlyRole(DAO_ROLE)
```

Allows the DAO to set the maximum withdraw percentage per balance of each validator
