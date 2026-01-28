# Architecture

The K9 Finance DAO Vesting app is based on 1 main contract:

* **Vesting** contract

Which interacts with the RealYieldStaking contract to check if the basic rule is completed for user.

## Vesting contract

### **deposit**

Before you make your deposit, ensure you meet the following criteria:

* **esKNINE Token Holder:** You must possess the esKNINE tokens you intend to vest.
* **Locked KNINE in Real Yield Staking (Optional):** You need to have any amount of KNINE tokens locked at Real Yield Staking for at least 6 months. This locked KNINE acts as collateral for your vested esKNINE and defines your vesting limit.&#x20;

Users can deposit any amount of esKNINE within the vesting limit of a user (based on the backing ratio):

```
esKnineThreshold = 
    ( 
       _lockedAmount + 
       [_stakedAmount * lockedOnly] - 
       _currentReservedAmount 
    ) / backingRatio
```

Based on the vesting ratio, their reward will be calculated as:

**`rewardKnine = depositAmount * vestingRatio`**

and each second users will receive the KNINE:

**`rewardKninePerSecond = rewardKnine / vestingPeriod`**

### **claim**

To claim your vested KNINE tokens, you must meet the following criteria:

* **Active Vesting Position:** You must have an existing vesting position where your esKNINE tokens are being vested and converted.
* **Vested KNINE Availability:** A portion of your esKNINE tokens should have been converted into KNINE tokens based on the vesting ratio set at the time of deposit.

Claiming tokens available anytime if the accumulated KNINE amount is greater than zero. Associated esKNINE amount will be burned upon each reward claim according to the vesting ratio.

### **recalculate**

In case when Vesting accepts the non-locked staking positions as a collateral, and user unstakes such position from Real Yield Staking, vesting is recalculated to meet the vesting rules and vest only those esKNINE that are collateralized.&#x20;

Since the collateral has decreased, the deposited esKNINE amount will be decreased, and certain amount of esKNINE (according to backing ratio) is excluded from vesting.

```
_unstakeAmount = X     //how much a user has unstaked

_currentDepositAmount = _currentReservedAmount / backingRatio   //how much is 
currently used as collateral for vesting

esKnineExcluded = min(_currentDepositAmount, stakedAmount / backingRatio)  //how much
 esKNINE should be removed from vesting
 
_stakedAmount = stakedAmount - unstakeAmount   //calculating 
the staked amount for vesting info update

stakedAmount = _stakedAmount
```

As the collateral has decreased, so will the deposited esKNINE amount that is being vested.

```
_depositAmount = max(0, _currentDepositAmount - esKnineExcluded)  // how much 
esKNINE left for vesting

depositAmount = _depositAmount
```

Then the vesting schedule is recalculated to finish at the same end date, but the **`rewardKninePerSecond`** is decreased.

### **changeIsOnlyLocked**

Administrator is capable of switching the non-locked staking positions for vesting collateral. New state is applied only to new vesting deposits.

### **emergencyStop**

In case of emergency, admins are capable of terminating the staking contract. When it happens, users are able to claim their non-converted esKNINE and accumulated rewards. No new deposits are accepted.
