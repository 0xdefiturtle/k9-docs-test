# Architecture

The K9 Finance DAO Farming architecture has 2 main parts:

* **FarmingFactory** contract
* **FarmingInstance** contract

and utilizes the Shibaswap v2 liquidity.

## FarmingInstance contract

FarmingInstance contract represents the farming pool. Each farming pool on the platform is a separate smart-contract deployed by the FarmingFactory contract.

### Deposit

Users can deposit their knBONE/BONE LP (received from [Shibaswap](https://shibaswap.com/)) via "Stake" UI and `deposit()` function. LPs other than mentioned in the farming pool are not accepted.

### Withdraw

Users can withdraw their total deposited funds via `withdraw()`. By doing so, users receive their LP tokens and the accumulated rewards.

### Zap

This function allows depositing one of the `token0` and `token1` of the liquidity pair.

When users deposit via `zap()` , the following steps are executed:

1. The entry fee is taken,
2. The received deposit is split according to the liquidity ratio of `token0/token1` on [Shibaswap](https://shibaswap.com/),
3. One half is swapped to another token in order to provide liquidity,
4. Once the swapped amount is received, the `token0` and `token1` amounts are used to provide liquidity,
5. Once the liquidity provided and the LP tokens are received, these LP tokens are deposited into farming pool.

So, the `zap()` function executes providing liquidity, which allows users to eliminate providing liquidity manually by themselves. Zapping fee is applied to cover the providing liquidity cost.

### Unzap

`Unzap()` function executes the opposite steps:

1. Yser selects the token to receive,
2. esKNINE + bonusToken (optional) reward is claimed,
3. LP tokens are withdrawn from the farming pool,
4. Liquidity is removed from the [Shibaswap](https://shibaswap.com/) v2 liquidity pool,
5. `token0` or `token1` amount is swapped accordingly to `token1` or `token0` (defined by the user's choice of `tokenOut),`
6. Once the swapped tokens received, the exit fee is taken,
7. The full `tokenOut` amount is transferred to the user's wallet.

Exit fee is applied to cover the removing liquidity cost.

### **claimRewardsAll**

By calling this function user can claim all the accumulated rewards of a single farming pool. This includes:

* Main reward received from stake, zap or both (whichever is present),
* Accumulated bonus reward (if present).

### **claimRewards**

This function allows claiming rewards from 'stake' or 'zap' separately. `fromStake` value defines which reward is claimed:

* `FALSE` - zapping reward,
* `TRUE` -  staking reward.

The associated bonus reward is also claimed.

## FarmingFactory contract

Farming factory contract is responsible for creating new farming pools that support [Shibaswap](https://shibaswap.com/) liquidity pairs. Users can't interact with this contract.

### Management

The administrators have the following access to manage the farming factory:

* create/stop new farming pool,
* create/stop bonus reward pool,
* set the farming pool reward payout,
* set zapping and unzapping fees,
* manage the factory parameters.
