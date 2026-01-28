# RealYieldStaking Contract

The contract is responsible for staking KNINE tokens to receive BONE  rewards. Two types of deposits (locked and non-locked) are available.

## Variables

<mark style="color:orange;">`bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");`</mark> - admin role identifier.

<mark style="color:orange;">`IERC20 public KNINE;`</mark> - KNINE token address.

<mark style="color:orange;">`uint256 public maxLockMultiplier;`</mark> - maximum multiplier value (for 12-months lock), multiplied by 10^18 (must be stored this way for correct calculations).\
<mark style="color:orange;">`uint256 public excessReward;`</mark> - extra amount of reward (in native). This extra amount appears from solidoty-specific integer division.

<mark style="color:orange;">`uint256 public totalStakers;`</mark> - number of unique stakers in the pool.

<mark style="color:orange;">`PoolInfo public poolInfo;`</mark> - general information on the reward pool in form of the PoolInfo struct (see below).

<mark style="color:orange;">`struct PoolInfo {`</mark>\ <mark style="color:orange;">`uint256 startTime;`</mark> - global contract start time.\ <mark style="color:orange;">`uint256 endTime;`</mark> - global contract shutdown time.\ <mark style="color:orange;">`uint256 periodFinish;`</mark> - time of the last or upcoming end of reward distribution.\ <mark style="color:orange;">`uint256 lastUpdate;`</mark> - last update time.\ <mark style="color:orange;">`uint256 rps;`</mark> - current reward per second distribution amount.\ <mark style="color:orange;">`uint256 totalStaked;`</mark> - how many tokens are currently locked.\ <mark style="color:orange;">`uint256 totalWeight;`</mark> - total weight of stakers in the pool.\ <mark style="color:orange;">`uint256 acc;`</mark> - last updated accumulator value. \ <mark style="color:orange;">`}`</mark>

## Events

<mark style="color:orange;">`event Deposited(`</mark>\ <mark style="color:orange;">`address user,`</mark>\ <mark style="color:orange;">`uint256 amount,`</mark>\ <mark style="color:orange;">`uint256 weight,`</mark>\ <mark style="color:orange;">`uint256 lockEnds`</mark>\ <mark style="color:orange;">`);`</mark> - upon `deposit` call, returns:

* The user's address,
* The number of deposited tokens,
* The new final weight of the user when his lock ends.

<mark style="color:orange;">`event LockIncreased(address user,uint256 newLockEnd, uint256 newWeight);`</mark> - upon `increaseLockup` call, returns:

* The user's address,
* New lock end time,
* New weight.

<mark style="color:orange;">`event Withdrawed(address user,uint256 amount);`</mark> - upon `withdraw` call, returns:

* The user’s address,
* How many tokens user has withdrawn.

<mark style="color:orange;">`event ClaimedReward(address user,uint256 amount);`</mark> - upon `claimTotalRewards`, `claimRewards` and `withdraw` call, returns:

* The user's address,
* The claimed reward amount.

## Default Admin Functions

### initialize

```
function initialize(address _knine, address _admin) public
```

{% hint style="info" %}
For the initializer role only
{% endhint %}

Initializer function, not called after initialization.

### start

```
function start(
uint256 startTime,
uint256 rps
) external
```

Starts staking contract (setting the global start time and primary RPS).

### emergencyStop

```
function emergencyStop() external
```

Global contract stopping method.

### withdrawExcessReward

```
function withdrawExcessReward() external
```

Withdraw excess reward from excessReward.

### withdrawStockTokens

```
function withdrawStockTokens(address token) external
```

Withdraw excess tokens (not reward) from the contract.

## **Default Admin and Admin Functions**

setRPS

```
function setRPS(uint256 value) external
```

Set a new reward per second value.

### setMaxMultiplier

```
function setMaxMultiplier(uint256 value) external
```

Set the maximum multiplier value.

{% hint style="warning" %}
input value should be multiplied by 10^18
{% endhint %}

## **User Functions**

### deposit

```
function deposit(uint256 amount, uint8 lockDuration) external
```

Making a new deposit or adding to the current one with the ability to set a lockup.

{% hint style="warning" %}
&#x20;For <mark style="color:orange;">`lockDuration`</mark>- input the number of months for a lockup, 0 means no lockup
{% endhint %}

### increaseLockup

```
function increaseLockup(uint8 lockDuration) external
```

Increasing the lockup.&#x20;

{% hint style="warning" %}
For <mark style="color:orange;">`lockDuration`</mark> - input the number of months for lockup, the lock period will restart
{% endhint %}

### withdraw

```
function withdraw(bool isLocked) external 
```

Withdrawing a deposit.

{% hint style="info" %}
* <mark style="color:orange;">`isLocked == true`</mark> - withdrawal of a locked deposit (which lockup period has ended)
* <mark style="color:orange;">`isLocked==false`</mark> - withdrawal of a non-locked deposit
{% endhint %}

### claimRewards

```
function claimRewards(bool isLocked) public
```

&#x20;Claiming rewards.

{% hint style="info" %}
* <mark style="color:orange;">`isLocked == true`</mark> - withdrawal of a locked deposit (which lockup period has ended)
* <mark style="color:orange;">`isLocked==false`</mark> - withdrawal of a non-locked deposit
{% endhint %}

### claimTotalRewards

```
function claimTotalRewards() external
```

Claiming all available rewards from both deposits at once.

## **View Functions**

### pendingRewards

```
function pendingRewards(
address user
) public view returns (uint256, uint256) 
```

Show accumulated rewards by user address.

{% hint style="info" %}
* the first value is a locked deposit rewards
* the second value is a non-locked deposit rewards
{% endhint %}

### userDeposits

```
function userDeposits(
address user
) external view returns (UserInfo[2] memory)
```

Information on the user’s deposits in the _UserInfo_ struct format.

{% hint style="info" %}
* the first value is a locked deposit rewards
* the second value is a non-locked deposit rewards
{% endhint %}

### UserInfo&#x20;

<mark style="color:orange;">`struct UserInfo {`</mark>\ <mark style="color:orange;">`uint256 amount;`</mark> - number of staked tokens.\ <mark style="color:orange;">`uint256 weight;`</mark> - deposit weight.\ <mark style="color:orange;">`uint256 acc;`</mark> - last recorded battery value.\ <mark style="color:orange;">`uint256 debt;`</mark> - last counted recorded reward.\ <mark style="color:orange;">`uint256 lockEnd;`</mark> - when the lock ends (for unlocked deposits there will be 0).\ <mark style="color:orange;">`}`</mark>
