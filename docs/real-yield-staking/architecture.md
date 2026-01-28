# Architecture

The K9 Finance DAO Real Yield Staking app is based on 1 main contract:

* **RealYieldStaking** contract

## RealYieldStaking contract

This contract is responsible for managing user deposits and rewards, including:

* Accepting deposits,
* Rewards calculation,
* Rewards claiming and withdrawals.

### deposit

Real Yield Staking provides two options for depositing your KNINE tokens:

1. **Staking without Lockup:** This option offers flexibility as users can withdraw their KNINE tokens and any accrued rewards at any time. However, it comes with a base multiplier of x1, meaning user  earns rewards based solely on their staked KNINE amount.
2. **Locked Staking:** This option allows users to lock your KNINE tokens for a predetermined period (1 to 12 months) in exchange for a higher reward multiplier. The longer the lockup duration users choose, the greater the multiplier applied to their staked KNINE, resulting in amplified BONE rewards. You can add more KNINE to your existing deposit with or without extending the lockup period.

### **increaseLockup**

You can choose to only extend the lockup period without depositing more KNINE if you currently have an active locked staking position. Extending lockup is not applicable to KNINE staked without a lockup period.

You can increase your lockup and choose the lockup period not less than the remaining lockup time. Basically, you are setting the new lockup period, and it can't be decreased.

Adding more KNINE while increasing lockup is available.

### **withdraw**

Withdrawing staked KNINE tokens terminates the staking position and claims associated rewards. User has to initiate a new staking position to participate again.

For locked position, withdrawal is available only after the lockup period end.

### **claimRewards**

Claiming rewards does not affect the staking position. It is available anytime for both locked and non-locked positions.

### **claimTotalRewards**

Claiming total rewards is available for users who have both locked and non-locked positions at Real Yield Staking. It also does not affect the staking position and available anytime.

### **setMaxMultiplier**

Admins are capable of managing the maximum multiplier for locked positions.

### **emergencyStop**&#x20;

In case of emergency, admins are capable of terminating the staking contract. When it happens, users are able to claim their deposits and accumulated rewards. No new deposits are accepted.

### **Reward Calculation**

Real Yield Staking rewards you with BONE tokens based on your staked KNINE and the chosen staking option. Here's a simplified explanation:

* The APR is calculated based on the reward tokens distributed per second, token prices, and the total staked KNINE amount.
* Staking without a lockup applies a base multiplier of x1 to your KNINE amount for reward calculation.
* Locked staking applies a multiplier that increases with the lockup duration (up to maxLockMultiplier). The longer you lock your KNINE, the higher the multiplier and the more BONE rewards you earn.
