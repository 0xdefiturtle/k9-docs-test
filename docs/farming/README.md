# Farming

The K9 Finance DAO Farming pools allow you to be an active participant in our decentralized ecosystem and earn rewards for providing liquidity on [Shibaswap](https://shibaswap.com/) (UniV2 liquidity). By providing liquidity to knBONE/BONE and other pairs, you'll contribute to a smoother trading experience for everyone while earning esKNINE rewards.

The rules are simple:

1. Gain LP tokens of knBONE/BONE liquidity at [Shibaswap](https://shibaswap.com/) or hold knBONE and BONE tokens
2. Deposit your LP tokens \
   OR&#x20;
3. Zap your knBONE or BONE tokens
4. The bigger your deposit, the bigger your reward.

Here is the flowchart describing the farming flow:

<figure><img src="../.gitbook/assets/image (29).png" alt=""><figcaption><p>Farming Overview</p></figcaption></figure>

* There is a 0.5% fee to zap in and zap out of a pool using K9 Bonecrusher
* If you zap in, you must zap out
* There is frontrunning protection in the zap function to ensure that once your transaction goes through, the realized value of the trade does not exceed +/- 3% variance
* There is **NOT** slippage protection for the user. this means that if you are zapping a large amount of funds, and the pool is small, that **you MAY experience slippage**. The pool will grow throughout the day tomorrow, but if you are transacting right away, it is highly likely the pool will be low liquidity relative to the size of the positions entering the pool

For this: K9 Finance DAO recommends not using the Zap feature if you are using large trading size for 2 reasons:

1. Potential slippage
2. Avoiding fees (more size = more fee)
