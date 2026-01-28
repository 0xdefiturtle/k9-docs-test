# FarmingInstance

[_<mark style="color:yellow;">Link to FarmingInstance source code on Shibarium</mark>_](https://www.shibariumscan.io/address/0xC014af4e4eb97D33A8c7112791FBF6af8FF9a93E?tab=contract)

Implementation of the logic of the UniV2 liquidity farming contract (version for ShibaSwap) &#x20;

UniV2 farming implementation contract for Shibaswap with a main reward pool and several bonus (up to 9) pools. Main pool reward is esKNINE token which is minted by the farming contract.

## Variables

<mark style="color:orange;">`uint8 public constant MAX_POOL_LENGTH = 10;`</mark> - maximum number of reward pools.\
<mark style="color:orange;">`uint256 public constant MULTIPLIER = 10**20;`</mark> - calculations multiplier.

<mark style="color:orange;">`address public pool;`</mark> - liquidity pool address (ShibaSwap LP Token) for which the farming was created.\
<mark style="color:orange;">`address public router;`</mark> - UniswapV2Router02 (ShibaSwap) contract address.\
<mark style="color:orange;">`address public factory;`</mark> - FarmingFactory contract address.\
<mark style="color:orange;">`LiquidityPool public liquidityPool;`</mark> - an object of LiquidityPool type.\
<mark style="color:orange;">`Intermediate public intermediate;`</mark> - object of the Intermediate type (see below).\
<mark style="color:orange;">`RewardPool[] public rewardPools;`</mark> - an array of reward pools like RewardPool.

<mark style="color:orange;">`struct Deposit {`</mark> - struct to describe the deposit.\ <mark style="color:orange;">`uint256 liquidity;`</mark> - number of user LP tokens.\ <mark style="color:orange;">`uint256[] accumulators;`</mark> - an array of batteries for each rewardPool.\ <mark style="color:orange;">`uint256[] debts;`</mark> - an array of calculated 'not claimed' rewards (updated upon actions with a deposit) for each rewardPool.\ <mark style="color:orange;">`}`</mark>

<mark style="color:orange;">`struct Intermediate {`</mark> - struct for storing intermediary calculations.\ <mark style="color:orange;">`uint256 totalLiquidity;`</mark> - the total amount of liquidity stored in farming pool at the moment.\ <mark style="color:orange;">`uint256[] lastUpdate;`</mark> - an array of the latest updates timestamps for each rewardPool (will not be visible through mapping, check through the getUserDeposits method).\ <mark style="color:orange;">`uint256[] accumulators;`</mark> - an array of accumulators for each rewardPool (will not be visible through mapping, check through the getUserDeposits method).\ <mark style="color:orange;">`}`</mark>

## Events

<mark style="color:orange;">`event Deposited(address user,`</mark> - user address.

<mark style="color:orange;">`uint256 liquidity`</mark> - number of LP tokens.

<mark style="color:orange;">`);`</mark> - Upon `zap` or `deposit` call.

\
<mark style="color:orange;">`event Withdrawed(address user,`</mark> - user address.

<mark style="color:orange;">`uint256 liquidity`</mark> - number of LP tokens.

<mark style="color:orange;">`);`</mark> - Upon `withdraw` or `unzap` call.

\
<mark style="color:orange;">`event ClaimedReward(`</mark>

<mark style="color:orange;">`address user,`</mark> - user address.\ <mark style="color:orange;">`uint256 halfId,`</mark> - reward pool id.\ <mark style="color:orange;">`bool fromZap,`</mark> - `true` - reward withdrawn for deposit made via zap; otherwise - `false`\ <mark style="color:orange;">`address rewardToken,`</mark> - reward token.\ <mark style="color:orange;">`uint256 amount`</mark> - number of cliamied rewards.\ <mark style="color:orange;">`);`</mark> - upon reward withdrawal (claimRewards, claimRewardsAll, withdraw, unzap).

\
<mark style="color:orange;">`event Zap(address inputToken,`</mark> - token submitted for input.

<mark style="color:orange;">`uint256 amount,`</mark> - the number of tokens (except for phi) submitted to the input.

<mark style="color:orange;">`uint256 fee`</mark> -  how many tokens went to the factory as a fee.

<mark style="color:orange;">`);`</mark> - upon `zap` call.

\
<mark style="color:orange;">`event Unzap(address outputToken,`</mark> - output token.

<mark style="color:orange;">`uint256 amount,`</mark> - number of tokens at the output (excluding fee).

<mark style="color:orange;">`uint256 fee`</mark> - how many tokens were received by the factory as a fee.&#x20;

<mark style="color:orange;">`);`</mark> - upon `unzap` call.

<mark style="color:orange;">`event BonusPoolAdded(`</mark>\ <mark style="color:orange;">`uint256 halfId,`</mark> - index in the rewardPools array assigned to the created pool.\ <mark style="color:orange;">`address rewardToken,`</mark> - reward token of the created pool.\ <mark style="color:orange;">`uint64starts,`</mark> - start time.\ <mark style="color:orange;">`uint64ends,`</mark> - end time.\ <mark style="color:orange;">`uint256 rps`</mark> - reward per second.

<mark style="color:orange;">`);`</mark> - upon `addBonusPool` call.

<mark style="color:orange;">`event BonusPoolStopped(uint256 halfId);`</mark> - upon `stopBonusPool` or when the pool  stopped itself by the endTime.

<mark style="color:orange;">`event MainRewardPoolStopped();`</mark> - upon `stopMainPool` or when the pool  stopped itself by the endTime.

<mark style="color:orange;">`event RewardPerSecondChanged(uint256 rps);`</mark> - upon `changeRPS`, returns a new RPS value for the main pool.

## Factory Functions

### addBonusPool

```
function addBonusPool(RewardPool calldata rew) external
```

Add a bonus pool (call from farmingFactory.addBonusPool).

### stopBonusPool

```
function stopBonusPool(uint256 halfId) external
```

&#x20;Stop the bonus pool (call from farmingFactory.stopBonusPool).

### stopMainPool

```
function stopMainPool() external
```

&#x20;Stop the main pool and all bonus ones (call with farmingFactory.stopFarming).

### changeRPS

```
function changeRPS(uint256 value) external
```

&#x20;Change the RPS value in the main reward pool (call from `farmingFactory.changeFarmingRPS`).

## **Initializer Functions**

### initialize

```
function initialize(
address _factory,
address _router,
address _pool,
LiquidityPool memory _liq,
RewardPool calldata _rew
) public
```

Initializer function, not called after initialization.

{% hint style="info" %}
Only for the initializer role
{% endhint %}

## **User Functions**

### deposit

```
function deposit(uint256 amount) external
```

&#x20;Depositing LP tokens.

### withdraw

```
function withdraw() external
```

Withdraw  all LP tokens from user's deposits made via `deposit` method.

### claimRewardsAll

```
function claimRewardsAll() external
```

Withdraw all rewards both from a deposit via `zap` and from a regular `deposit` at the same time (withdraws rewards from all pools).

### claimRewards

```
function claimRewards(
uint256 halfId,
bool fromStake
) external 
```

Withdraw reward from the specified reward pool for the specified type of the deposit (made through zap == `false`, otherwise == `true`).

### zap

```
function zap(
address inputToken,
uint256 amount
) external payable
```

An option for making a deposit without the user having LP tokens.

{% hint style="info" %}
User deposits one of the available tokens `token0` or `token1` (if one of them is a wrapped native, then a zero address should be specified in `inputToken`and send the native, then the contract will wrap it itself).&#x20;

Then part of the deposited tokens is swapped into another and this pair is added into liquidity, which is how LP tokens are formed. These LP are used for farming and accumulate the reward.
{% endhint %}

### unzap

```
function unzap(address tokenOut) external
```

Withdraw a deposit made through `zap` .

{% hint style="info" %}
* Liquidity is removed,
* LP tokens are burned,
* Share of tokens (a token other than `tokenOut`) is swapped to `tokenOut` and transferred to the user.
{% endhint %}

## **View Functions**

### pendingReward

```
function pendingReward(
address user,
uint256 halfId
) public view returns (uint256 fromStake, uint256 fromZap)
```

Method for displaying earned rewards in a specific reward pool (will return two values: first for a deposit via `deposit`, second for a deposit via `zap`).

### pendingRewardsMultiple

```
function pendingRewardsMultiple(
address user - user address
) external view returns (uint256[] memory fromStake, uint256[] memory fromZap) 
```

Method for displaying earned rewards in all reward pools.

### getActualPools

```
function getActualPools()
external
view
returns (uint256[] memory ids, RewardPool[] memory pools)
```

Method for displaying a list of active reward pools (the ones that are still distributing rewards).&#x20;

{% hint style="info" %}
<mark style="color:orange;">`ids`</mark> - its indexes in the array of reward pools,

<mark style="color:orange;">`pools`</mark> - its contents
{% endhint %}

### getUserDeposits

```
function getUserDeposits(
address user -
) external view returns (Deposit[2] memory dept)
```

Method for displaying user deposits.&#x20;

{% hint style="info" %}
* Deposits marked with <mark style="color:orange;">`index 0`</mark> are made via <mark style="color:orange;">`deposit`</mark>
* Deposits marked with <mark style="color:orange;">`index 1`</mark> are made via <mark style="color:orange;">`zap`</mark>
{% endhint %}

### getFarmingState

```
function getFarmingState() external view returns (Intermediate memory)
```

&#x20;Method for displaying the intermediate variable in full.
