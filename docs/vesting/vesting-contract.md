# Vesting Contract

The contract is responsible for managing users deposits and converting esKNINE into KNINE. The esKNINE tokens are burned upon claimint KNINE. KNINE rewards are manually replenished.

## Variables

<mark style="color:orange;">`bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");`</mark> - admin role identifier.

<mark style="color:orange;">`uint8 public constant DENOMINATOR = 1_00;`</mark> - denominator for correct backing/vesting ratio calculation.

<mark style="color:orange;">`address public KNINE;`</mark> - KNINE token address.

<mark style="color:orange;">`address public esKNINE;`</mark> - esKNINE token address.

<mark style="color:orange;">`address public STAKING;`</mark> - RealYieldStaking contract address.

<mark style="color:orange;">`uint64 public endTime;`</mark> - emergency stop time of the contract (if the _emergencyStop_ method was not called, then == 0).

<mark style="color:orange;">`Settings public settings;`</mark> - vesting parameters in the Settings struct format.

<mark style="color:orange;">`mapping(address => Deposit) public deposits;`</mark> - mapping, assigning the Deposit struct for each user address.\
\
<mark style="color:orange;">`struct Settings {`</mark>\ <mark style="color:orange;">`bool lockedOnly;`</mark> - true - only locked deposits at RealYieldStaking are allowed for collateral; otherwise - false (means that non-locked are also accounted, but locked deposit must be present anyway).\ <mark style="color:orange;">`uint64backingRatio;`</mark> - collateral ratio for desired deposit amount, defines how much KNINE must be locked at Real Yield Staking based on the input amount; the value has a 2 decimals precision (i.e. if you need to set the backing ratio == 2, then the input value for the contract must be 200).\ <mark style="color:orange;">`uint64vesting;`</mark> - reward conversion ratio, defines how much KNINE user will receive based on his deposit; the value has a 2 decimals precision (i.e. if you need to set the vesting ratio == 2, then the input value for the contract must be 200).\ <mark style="color:orange;">`uint64fortressPeriod;`</mark> - vesting duration, seconds.\ <mark style="color:orange;">`}`</mark>\
\
<mark style="color:orange;">`struct Deposit {`</mark> \ <mark style="color:orange;">`uint64startTime;`</mark> - deposit vesting start time.\ <mark style="color:orange;">`uint64endTime;`</mark> - vesting end time for the specified deposit.\ <mark style="color:orange;">`uint256 depositAmount;`</mark> - esKNINE deposited amount.\ <mark style="color:orange;">`uint256 reservedAmount;`</mark> - amount of KNINE tokens used as collateral for this deposit.\ <mark style="color:orange;">`uint256 lockedAmount;`</mark> - amount of  locked KNINE deposit at the RealYieldStaking contract.\ <mark style="color:orange;">`uint256 stakedAmount;`</mark> - amount of non-locked KNINE deposit at the RealYieldStaking contract.\ <mark style="color:orange;">`uint256 potentialRewards;`</mark> - the amount of KNINE tokens that the user would receive at the end of vesting.\ <mark style="color:orange;">`uint256 claimed;`</mark> - claimed amount.\ <mark style="color:orange;">`Settings settings;`</mark> - vesting parameters in the Settings struct format.\ <mark style="color:orange;">`Debt debt;`</mark> - how much is in debt (Debt structure).\ <mark style="color:orange;">`}`</mark> - the data is written upon `deposit` and upon `recalculate` method call, if it worked; exception - _claim_ field is kept as current, does not change.

<mark style="color:orange;">`struct Debt {`</mark>\ <mark style="color:orange;">`uint256 deposited;`</mark> - how much esKNINE is in debt to be claimed.\ <mark style="color:orange;">`uint256 earned;`</mark> - how much KNINE is in debt to be claimed.\ <mark style="color:orange;">`}`</mark>

#### Events

<mark style="color:orange;">`event Deposited(`</mark>\ <mark style="color:orange;">`address user,`</mark>\ <mark style="color:orange;">`uint256 amount,`</mark>\ <mark style="color:orange;">`uint256 potentialReward,`</mark>\ <mark style="color:orange;">`uint64lockEnd`</mark> \ <mark style="color:orange;">`);`</mark> - upon `deposit` call.

<mark style="color:orange;">`event Claimed(address user,uint256 amount);`</mark> - upon `claim` call, returns:

* The user's address,
* How many KNINE tokens he claimed.

<mark style="color:orange;">`event Recalculated(address user,uint256 esKnineExcluded);`</mark> - upon `recalculate` call, returns:

* The user's address,
* How many esKNINE tokens were excluded from his deposit.

<mark style="color:orange;">`event Paused();`</mark> - upon `pause` call.

<mark style="color:orange;">`event Unpaused();`</mark> - upon `unpause` call.

<mark style="color:orange;">`event Stopped(uint64endTime);`</mark> - upon `emergencyStop` call, returns the emergency stop time of the contract.

<mark style="color:orange;">`event StockTokensWithdrawed(address token,uint256 amount);`</mark> - upon `withdrawStockTokens` call; returns:

* The token address,
* Amount withdrawn from the contract.

<mark style="color:orange;">`event OnlyLockedChanged(bool status);`</mark> - upon `changeIsOnlyLocked` call; returns the new bool status.

<mark style="color:orange;">`event BackingRatioChanged(uint64ratio);`</mark> - upon `setBackingRatio` call; returns new backing ratio.

<mark style="color:orange;">`event VestingRatioChanged(uint64ratio);`</mark> - upon `setVestingRatio` call; returns new rate.

<mark style="color:orange;">`event VestingPeriodChanged(uint64duration);`</mark> - upon `setVestingPeriod` call; returns new vesting period value.

<mark style="color:orange;">`event DepositDebtTransfer(address user,uint256 debt);`</mark> - triggered when the deposited esKNINE tokens (during the vesting pause) cannot be sent to the user and are put into debt to be claimed later.

<mark style="color:orange;">`event EarnedDebtTransfer(address user,uint256 debt);`</mark> - triggered when the reward tokens (during the vesting pause) cannot be sent to the user and are put into debt to be claimed later.

## Initializer Functions

### initialize

```
function initialize(
address _knine,
address _esknine,
address _staking,
address _admin,
Settings calldata _settings
) public
```

{% hint style="info" %}
For the initializer role only
{% endhint %}

Initializer function, not called after initialization.

## **Default admin Functions**

### emergencyStop

```
function emergencyStop() external
```

&#x20;Stops the contract (permanently).

### pause

```
function pause() external
```

Pause the contract

### unpause

```
function unpause() external
```

Unpause the contract.

### withdrawStockTokens

```
function withdrawStockTokens(
address token
) external
```

Withdraw tokens from the contract (any ERC20, except esKNINE)

## Default admin and Admin Functions

### changeIsOnlyLocked

```
function changeIsOnlyLocked() external
```

&#x20;Change lockedOnly bool value.

### setBackingRatio

```
function setBackingRatio(uint64value) external
```

Change the backingRatio value.

### setVestingRatio

```
function setVestingRatio(uint64value) external 
```

Change the vestingRatio value.

### setVestingPeriod

```
function setVestingPeriod(uint64value) external
```

Change the vestingPeriod value.

## **RealYieldStaking Interaction**

### recalculate

```
function recalculate(address user,uint256 unstakeAmount) external
```

When a non-locked deposit is unstaked at Real Yield Staking, if it was initially used as collateral, calculates currently undersecured esKNINE tokens in the vesting deposit and returns them to the user.

## **Public Functions**

### deposit

```
function deposit(uint256 amount) external
```

Deposit esKNINE tokens (creating new deposit or adding to an existing deposit).

### claim

```
function claim() external
```

&#x20;Claiming the converted KNINE tokens.

### **View Functions**

### pendingRewards

```
function pendingRewards(address user) public view returns (uint256)
```

&#x20;Current amount of KNINE tokens available for withdrawal (including debt).

### beforeDeposit

```
function beforeDeposit(address user) external view
returns (
uint256 esKnineBalance,
uint256 depositLimit,
Settings memory userSettings
)
```

Returns the current user's vesting limit:

* esKNINE balance at user's wallet,
* Vesting deposit limit - how much a user can deposit,
* Vesting parameters that will be applied upon deposit.

### depositInfo

```
function depositInfo(address user) external view
returns (
uint256 inVesting,
uint64vestingEnds,
uint256 reward,
uint256 lockedInStaking,
uint256 usedForVesting,
uint256 availableForVesting,
uint256 stakingEnds
)
```

Returns the deposit info by user address:

* Deposited amount (upon `deposit`),
* Vesting end time,
* Available KNINE amount that can be claimed,
* Real Yield Staking deposit amount according to the lockedOnly bool value,
* Currently used collateral for the remaining esKNINE,
* User's vesting limit,
* Real Yield Staking lockup end time.
