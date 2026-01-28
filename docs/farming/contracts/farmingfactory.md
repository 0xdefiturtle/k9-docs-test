# FarmingFactory

[_<mark style="color:yellow;">Link to FarmingFactory source code on Shibarium</mark>_](https://www.shibariumscan.io/address/0x8ed1A7c4736b5835560b0f9E961B8E3581774D42?tab=contract)

Farming pool Factory contract. Executes the functionality of deploying new farming pools (for Shibaswap liquidity), as well as their settings and management.

## Variables

<mark style="color:orange;">`bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");`</mark> - admin role identifier.

<mark style="color:orange;">`address public esKnine;`</mark> - esKNINE token address.\
<mark style="color:orange;">`address public router;`</mark> - UniswapV2Router02 (ShibaSwap) contract address. \
<mark style="color:orange;">`address public wbone;`</mark> - wrapped native coin address.\
<mark style="color:orange;">`address public farmingImplementation;`</mark> - contract storing the farming implementation code (FarmingInstanceV2) address.\
<mark style="color:orange;">`ZapFees public zapFees;`</mark> - ZapFees struct object.

<mark style="color:orange;">`struct ZapFees {`</mark>\ <mark style="color:orange;">`uint8 entry;`</mark> - zapping entry fee.\ <mark style="color:orange;">`uint8 exit;`</mark>  - zapping exit fee.\ <mark style="color:orange;">`}`</mark>

## Events

<mark style="color:orange;">`event CreateFarming(`</mark>\ <mark style="color:orange;">`address proxyDeployed,`</mark> - deployed farming pool (FarmingProxyV2) address.\ <mark style="color:orange;">`address currentImplementation,`</mark> - current implementation (FarmingInstanceV2) address.\ <mark style="color:orange;">`address token0,`</mark> -  `token0` address from the liquidity pool.\ <mark style="color:orange;">`address token1,`</mark> - `token1` address from the liquidity pool.\ <mark style="color:orange;">`);`</mark> - upon _createFarming_ method call.\
<mark style="color:orange;">`event NativeReceived(uint256 amount);`</mark> - upon receiving the native coin.

## Admin Functions

### LiquidityPool&#x20;

```
struct LiquidityPool {
address token0;
address token1;
}
```

Struct describing the liquidity pool used for farming pool creation.

### RewardPool&#x20;

```
struct RewardPool {
address rewardToken;
uint64startTime;
uint64endTime;
uint256 rps;
}
```

Struct describing the reward pool:

* Reward token address (for the main reward pool this is esKNINE),
* Reward distribution start time and end time,
* Reward per second.

### createFarming

```
function createFarming(
LiquidityPool memory liq,
RewardPool calldata rew
) external
```

Creates new farming pool based on the provided liquidity and reward pools info.

{% hint style="info" %}
Only for DEFAULT\_ADMIN\_ROLE or ADMIN\_ROLE role
{% endhint %}

### addBonusPool

```
function addBonusPool(
address farming,
RewardPool calldata rew
) external
```

Adds `rew` bonus reward pool  to the `farming` farming pool.

{% hint style="info" %}
Only for DEFAULT\_ADMIN\_ROLE or ADMIN\_ROLE role
{% endhint %}

### initialize

```
function initialize(
address _admin,
address _esKnine,
address _router,
address _wbone
) public
```

Initializer function, not called after initialization.

{% hint style="info" %}
Only for the initializer role
{% endhint %}

## Default Admin Functions

### setFarmingImplementation

```
function setFarmingImplementation(address instance) external
```

&#x20;Set the farming logic implementation contract address.

### setRouter

```
function setRouter(address instance) external
```

Set the address of UniswapV2Router02 (ShibaSwap).

### setWrappedBone

```
function setWrappedBone(address instance) external
```

Set the wrapped native coin address.

### setEsKnine

```
function setEsKnine(address instance) external
```

&#x20;Set the esKnine token address.

### setFees

```
function setFees(ZapFees calldata fees) external
```

&#x20;Replace zapping and unzapping fee.

### stopBonusPool

```
function stopBonusPool(
address farming,
uint256 halfId
) external
```

&#x20;Stop the rewards distribution of a specific bonus pool at a specific farming pool.

### stopFarming

```
function stopFarming(
address farming - farming address to stop
) external
```

Stop all rewards distribution (main reward pool and each bonus reward pool) for a specific farming.

### changeFarmingRPS

```
function changeFarmingRPS(address farming,
uint256 value
) external
```

Change the RPS `value` of the main reward pool at the specified `farming` farming pool.

### recovery

```
function recovery(address token) external
```

Withdraw transferred tokens from the contract.

{% hint style="info" %}
If the output is a wrapped native coin, it will unwrap and return the native coin itself
{% endhint %}

## **View Functions**

### getAllCreatedPools

```
function getAllCreatedPools() external view returns (address[] memory)
```

&#x20;Get a list of all farming pools ever deployed using this factory.

