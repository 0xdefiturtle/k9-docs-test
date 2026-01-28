---
description: Step-by-step Instructions
---

# How K9 Finance DAO works

K9 Finance DAO user interface is accessible at this [<mark style="color:yellow;">**link**</mark>](https://app.k9finance.com).&#x20;

As the platform is based on 2 networks - Ethereum and Shibarium - its functionality is separated by:

* Ethereum
  * Liquid staking
* Shibarium&#x20;
  * Farming&#x20;
  * Real Yield Staking&#x20;
  * Vesting

Flowchart of the K9 Finance DAO platform:

<figure><img src=".gitbook/assets/image (13).png" alt=""><figcaption><p>K9 Finance DAO general use case</p></figcaption></figure>

1. Connect your wallet:

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdnnMGDOEfTL9XNsOFzlb0E9CMMGtzbnM3-sXnJH6I458T6J134Q_Qhp1i2x0-hgLgw3sLgaBy4oeFlz46jWSjdqXjeAb6VZi2abajDSj97JCDVA8NSp2wSWbxu8oI6nCZhd4F7Ejs1JA6tf4uZW8DAPUVW?key=RPSFst5cIoGXQstxU_6BQg)

* Choose the Ethereum or Shibarium network in your wallet and click the “Connect Wallet” button in the upper right corner.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfgXkpXZ9HQ0OuMeRbWfDn77bf1k4ibC7N9JQBsoukLk2u7E4GFrB9sxQ8ieu5vtF1t41RpWwTkk1yzY5PgV-xk1_FOihI-UNUn0CLLT2DAIij4o5gPO0dWX0TRqUqb04sPpljXDzTSZWxESuLSxNUx9faZ?key=RPSFst5cIoGXQstxU_6BQg)

* Make sure your wallet is connected to the Ethereum or Shibarium network, otherwise the connection to the app will not be completed.

## Liquid Staking

### Stake BONE

<figure><img src=".gitbook/assets/image (15).png" alt=""><figcaption><p>Staking UI</p></figcaption></figure>

The first step for users to take when trying stake their BONE in the K9 Finance DAO protocol is to `unlock` their tokens. The unlock process approves the knBONE contract to spend the amount to be staked from the user's balance. To unlock tokens, click on the `unlock` button and confirm the transaction in the confirmation page that shows up.

After confirmation, wait for the process to be completed and a success dialog box saying `x BONE unlocked` will be displayed on the screen.

1. To complete the staking process, click `Stake` on the app and confirm the transaction in your wallet. This transaction will send your BONE tokens to the staking protocol.
2. Wait for the transaction to complete. Popup window displays the transaction progress:\
   ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfej4WgL4MIMJ2lI9nKAul4Ml2F9DZr9k-__QyU2aHmyig5oKDEvI7TLgPkCV33LHn7oYPEJvSweTo7rfBYAfnsn2W_87vGSTk1AiEKqhe287qAosdtD0QuHyJgvRwpgkOVE5AaqN1hj9nU9zgMKzoAGZc?key=RPSFst5cIoGXQstxU_6BQg)
3. Once the transaction is complete, the updated deposit amount will appear in the form on the right and knBONE tokens will appear in your wallet.
   1. Your knBONE tokens will be automatically moved to the Shibarium network. So, to check the knBONE balance in your wallet, please switch to Shibarium. You may need to add the token contract to your wallet interface.

The K9 Finance DAO protocol receives submitted BONE tokens, calculates the current ratio between BONE and knBONE tokens and sends that amount of knBONE to the user. Since knBONE is a non-rebasable token, user will always have the same amount. Over time, while rewards are accumulated, the value of knBONE token increases. BONE tokens are then delegated across Shibarium validators that are part of K9 Finance DAO protocol.

Accumulated rewards are re-distributed once a day between the receivers and re-delegated.

### Unstake knBONE[​](https://docs.polygon.lido.fi/how-lido-on-polygon-works/#unstake-tokens) <a href="#unstake-tokens" id="unstake-tokens"></a>

<figure><img src=".gitbook/assets/image (17).png" alt=""><figcaption><p>Unstaking UI - Request withdraw</p></figcaption></figure>

To unstake your staked tokens from the network

1. Click on the unstake tab on the app&#x20;
2. Choose how you would like to unstake your tokens - by withdrawal request&#x20;
3. Enter the unstake amount:
   1. In the AMOUNT input field, enter the number of knBONE tokens.
   2. Click on the "Use MAX" button to use all knBONE tokens.
   3. If you enter an amount higher than your knBONE balance in Ethereum and Shibarium combined, you will be prompted:\
      <img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXes6kx1rZkJE12nvkhW2QHqy65EjHx91yAgTnHC-A7lOGmM_uRXQXzbu83pPO31qAtVxRP-MKuSqUJLFEjZUY_zoaiddFbCM0IKXnI0VcKUKDjauT9D4AaE__3aHuTT9bNbejjA6MsnlwBy7fstgRnElWE?key=RPSFst5cIoGXQstxU_6BQg" alt="" data-size="line">
4. Below the input field you will see the following information:
   1. You will receive - the amount of BONE that you will receive as a result of executing a withdrawal request, in accordance with the rate in the system.
   2. Exchange rate - BONE:knBONE rate in the system.
5. Click on the Unstake button
   1. If you are connected to the wrong network, the system will prompt you to switch to Shibarium. Click on the “Switch to Shibarium” button and confirm the action in your wallet.\
      ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfWZ-Nd8G-dBghzyDPWbCl2vCHpm-prJ-Ge3gjDjI6-fYSvcoJqLpySPJ-dG1c87jDj5Yt271oRLCdCkcDvW6F07sqX9tHSh_VDR0KHudOxKskITjKt4XnsWgPG9L-ohepHz7UHKg5rubWhu-8lWldC_Fb_?key=RPSFst5cIoGXQstxU_6BQg)
6. Wait while the system switches to another network and refreshes the page.
7. Click on the Unstake button.&#x20;
8. The system will request confirmation to use the amount of knBONE tokens you specified. Popup window displays the transaction progress:\
   ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXda5lO71MzsUk0Xf14eETeTlU08o0e4FUX87k6D8rFX5D88XN4thegDHvCWHSg9ocsipp4C7MRfzOmXz78j2VSV_CKeF28KzSUbJVtbmLEaH2EQsaK9LSQS6oNiNX8cOc1ELtiAGgM-kyCWJGQbYhyWIfEw?key=RPSFst5cIoGXQstxU_6BQg)<br>
9. Confirm the transaction in your wallet.&#x20;
10. Next, the system will display a window to confirm the operation. During this transaction, your knBONE tokens in Shibarium will be transferred to Ethereum and debited from your wallet.
    1. For transferring  tokens from Shibarium to Ethereum , the system charges a fee to cover the costs of the transaction fee, the amount is indicated in the Bridging fee field.\
       ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfdO68kx9N6pbbiC6vtZ14W8A56rX_5Yl5w6fT926aANQKevG6Yelcwm9WN6MVJxB0bdYVRmFj_8YiRlOdwt0iwycP0jRWpLSveACC746G1qdvFMGPhZoQCeforGw5uRe8EAPIvREKXv3Vzr-B8CF5XA_Vu?key=RPSFst5cIoGXQstxU_6BQg)
11. Click the “Confirm” button and confirm the transaction in your wallet.
    1. Wait for the transaction to complete. It may take longer than the previous transactions. Popup window displays the transaction progress:\
       ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXc1_9LXFZu1v8wt1vy5uYlHW7XbnWfh1rTpZGHOQPAr6u87rm2LcmOkwG5T9yvEtE-XuY7R-FojadvoTtgqNmJf-2N5NI32Kx5GCTxKRNWyC8YoMOHOeuDPciLhcAzUFyvMZz3zzQQpsz97KxzHkcVvbf3B?key=RPSFst5cIoGXQstxU_6BQg)
12. After completing the operation, a window with the NFT of your request will be displayed.\
    ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcR-eVXme-G2oq9qVaUXvKFm-XK2EzC5DQj1CR16rHXyzUt3brlk4KVcjOaJPBdGiA8UdY3vMwaV6WXwDCgiPMdbTkAIKyNTtENTAn6rM-Jk63YoNBJiRDZO83D18gQZ4NkYpKk-TWkV3nULHUb71geOBli?key=RPSFst5cIoGXQstxU_6BQg)

Your request has been created in the system and is awaiting execution. When it is executed, you will be able to receive your BONE tokens. Upon unstaking, you submit your knBONE tokens, and in case of withdrawal request or split you will receive an NFT as a voucher for BONE token claim after the unbonding period.

<figure><img src=".gitbook/assets/image (18).png" alt=""><figcaption><p>Instant withdraw options</p></figcaption></figure>

When you decide to unstake your tokens by Instant Withdraw, you may be offered to split your unstake between the instant withdrawal and withdrawal request if the amount you want to unstake exceeds the available instant reward balance. You are free to use this 'split' option or refuse and unstake the available amount:

1. Enter the unstake amount:
   1. If the entered amount does not exceed the available Instant reward balance in the protocol, the following information will be displayed:\
      <img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeO3huIRzWqIKzJfgsa4btxhv9rpUYvLh2KBl-Ixp7Heq1bsNRnDJmI8fu81QVv8lKan2_76F4irpYvA8D_jAYBBQxCry0Y1-fTFarkJ9ROz8kujBgaKd-cV3fIo_FYEPISAPdwic5ob3tR9LR8uE3NZxo?key=RPSFst5cIoGXQstxU_6BQg" alt="" data-size="original">
   2. If the entered amount exceeds the available Instant reward balance in the protocol, leave the Split checkbox enabled. In this case, your amount will be divided into 2 parts, and the missing amount will be withdrawn via Request Withdraw:\
      ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdcQ5kyQmiptlpQS44kuyYDcBcwFiUa5iubp4EXcg97iYWlYyxPvYwHjzk_wmduDzR4JmXGaWoKIrW1bykmywwcSSA5CmwtfRqemKwGqrYIfgHm7at9X1ye_2r9TzY4cCTFe98lMEhBRgUD89qW-oeOZ-I?key=RPSFst5cIoGXQstxU_6BQg)
   3. If you disable the Split checkbox when the Instant reward balance is exceeded, an error will be displayed warning that the Instant pool balance is not enough for your unstake operation:\
      ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdHjFwbWylRPnI93BCLtxduQKA-Hs6sIjDK96t40Fh8fhBLlIk4M8tk5JWeGijxzeTfdYbL9wyrtNaxwoztGu08xxGTO8Owf6HlcUfjKEzo5YifNx7EFYOo15h0sjmcr90SBz4ZlnjBmlMNKWR6DxWtLW8?key=RPSFst5cIoGXQstxU_6BQg)
2. The following information will be displayed below the input field:
   1. Reward fee - fee for withdrawal of funds through Instant Withdraw.
   2. Exchange rate - BONE:knBONE rate in the system.
3. Click on the Unstake button
   1. If you are connected to the wrong network, the system will prompt you to switch to Shibarium. Click on the “Switch to Shibarium” button and confirm the action in your wallet.\
      ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfWZ-Nd8G-dBghzyDPWbCl2vCHpm-prJ-Ge3gjDjI6-fYSvcoJqLpySPJ-dG1c87jDj5Yt271oRLCdCkcDvW6F07sqX9tHSh_VDR0KHudOxKskITjKt4XnsWgPG9L-ohepHz7UHKg5rubWhu-8lWldC_Fb_?key=RPSFst5cIoGXQstxU_6BQg)
      1. Wait while the system switches to another network and refreshes the page.
      2. Click on the Unstake button.&#x20;
4. The system will request confirmation to use the amount of knBONE tokens you specified. A popup window displays the transaction progress:\
   ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXda5lO71MzsUk0Xf14eETeTlU08o0e4FUX87k6D8rFX5D88XN4thegDHvCWHSg9ocsipp4C7MRfzOmXz78j2VSV_CKeF28KzSUbJVtbmLEaH2EQsaK9LSQS6oNiNX8cOc1ELtiAGgM-kyCWJGQbYhyWIfEw?key=RPSFst5cIoGXQstxU_6BQg)
5. Confirm the transaction in your wallet.&#x20;
6. Next, the system will display a window to confirm the operation. During this transaction, your knBONE tokens in Shibarium will be transferred to the target network and debited from your wallet.
   1. For the transfer of tokens from Shibarium to Ethereum, the system charges a commission to cover the costs of the transaction fee, the amount is indicated in the Bridging fee field.\
      ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfdO68kx9N6pbbiC6vtZ14W8A56rX_5Yl5w6fT926aANQKevG6Yelcwm9WN6MVJxB0bdYVRmFj_8YiRlOdwt0iwycP0jRWpLSveACC746G1qdvFMGPhZoQCeforGw5uRe8EAPIvREKXv3Vzr-B8CF5XA_Vu?key=RPSFst5cIoGXQstxU_6BQg)
7. Click the “Confirm” button and confirm the transaction in your wallet.
   1. Wait for the transaction to complete. It may take longer than the previous transactions. Popup window displays the transaction progress:\
      ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfs3biLqG6EgjnpauHg4FiTS42nyXZj-e2LkErKITLlSO38ju097F4ZggPrLhFUwseZUbknTAOxRGNJcTwSZDQhEEsxW930iZ1Ht0wTx0GMORuQbwTXxfNhj80Nxs1xLmZb8C0ss43bZk5k2eYzIiT1haE?key=RPSFst5cIoGXQstxU_6BQg)
8. When the transaction is complete, the popup will display the transaction result:\
   ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXe0ZGsIhxnmGOXxMzpyfADw4b7mDb0C-b6s4mEdx5J6C1kp0Btvoif8btdJGMBOgOf6Qp6-Q9z-UbnO4pcUC1WRTowpufdkw19Ya2IUnD0IAVb2NkgHkxxcpWzUdgIpRWyxKEYK9BtCCwT5vABs_IrKKGA?key=RPSFst5cIoGXQstxU_6BQg)

BONE tokens are credited to your wallet on the target network (Ethereum Mainnet or Sepolia).

### Claim BONE[​](https://docs.polygon.lido.fi/how-lido-on-polygon-works/#claim-tokens) <a href="#claim-tokens" id="claim-tokens"></a>

<figure><img src=".gitbook/assets/image (19).png" alt=""><figcaption><p>Claiming UI</p></figcaption></figure>

After the unbonding period, a user will be able to submit his NFT to K9 Finance DAO. NFT gets burned and user receives his BONE. To claim your tokens, click on the claim tab:

1. In the "My Requests" field, select requests.
2. Click the “Claim” button in the “Reward” field and confirm the transaction in your wallet. A popup window displays the transaction progress:\
   ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXc4ujjq7WqllxcCLM-7l5jmpmxq1PtE-1MNEFQfbgX0NI89Zjz4BrgilsDzv5MvhJi1SYmVfNmBm73b6PQjITlzusYsvBK0l63Q4-WUrbuAAO3bJoeIqpaWBSoyHao6pJKrAY78N_A1wVT31jLYh0sc6Xg?key=RPSFst5cIoGXQstxU_6BQg)&#x20;
3. Wait for the transaction to complete. BONE tokens will be credited to your wallet.\
   ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdq-hGt7vKdH1WJrk6hTosfr42YtZyX2XRg13GpnXNeoCVxB0gAvrh-V4Gr5IylIWm5qOZYq8oXgXtYvAjLPJ208oZb9f9z6Z6LWc1j61Srbhwlhjylc7Z93tp9e2kiL88AFodgLwGJdKeAf4Ar1VOBWLU?key=RPSFst5cIoGXQstxU_6BQg)

## Farming

The K9 Finance DAO Farming pools allow you to be an active participant in our decentralized ecosystem and earn rewards for providing liquidity at Shibaswap (UniV2 liquidity).

### Stake/Unstake

<figure><img src=".gitbook/assets/image (20).png" alt=""><figcaption><p>Farming pool, Staking UI</p></figcaption></figure>

To start farming using "Stake" option, you need the LP tokens of knBONE/BONE pair from Shibaswap. Once you have the LP, you are ready to deposit:

1. Connect your wallet, switch to Shibarium chain
2. Open the "Stake" tab
3. Enter the amount of LP you would like to deposit
4. Click "Stake" and confirm the transaction in your wallet
5. Wait for the transaction to complete.

Once the deposit transaction is completed, you will start accumulating the esKNINE rewards. Claiming available anytime.

When you decide to unstake your LP, you need to:

1. Connect your wallet, switch to Shibarium chain
2. Open the "Stake" tab
3. Click "Unstake" and confirm the transaction in your wallet
4. Wait for the transaction to complete.

Once the unstake transaction is completed, you will receive your previously deposited LP and the accumulated rewards.

### Zap/Unzap

<figure><img src=".gitbook/assets/image (21).png" alt=""><figcaption><p>Farming Pool, Zapping UI</p></figcaption></figure>

If you don't want to provide liquidity or simply don't have the LP tokens, there is the Zapping option to participate in farming. The difference is that you can deposit your knBONE or BONE tokens and start farming, and the rest will be done automatically. Zapping fee is applied for both entering and exiting the farming pool.

To start farming using "Zap" option, you need to have knBONE or BONE tokens. Once you get one of these, you are ready to deposit:

1. Connect your wallet, switch to Shibarium chain
2. Open the "Zap" tab
3. Select the token you would like to deposit and enter the amount
4. Click "Zap" and confirm the transaction in your wallet
5. Wait for the transaction to complete.

During the deposit transaction, your deposited amount is swapped to provide knBONE/BONE liquidity on Shibaswap.

Once the zap (deposit) transaction is completed, you will start accumulating the esKNINE rewards the same way as if you use the 'stake' option. Claiming rewards is available at anytime.

When you decide to Unzap, you need to:

1. Connect your wallet, switch to Shibarium chain
2. Open the "Zap" tab
3. Click "Unzap", the Unzap options window will open\
   ![](/broken/files/822hmZLEZXp97vTPApU3)
4. Select the token you would like to receive&#x20;
5. Click "Unzap" and confirm the unzap transaction in your wallet
6. Wait for the transaction to complete.

During the unzap (unstake) transaction, previously provided liquidity is removed and swapped to the token of your choice on Shibaswap.

Once the unzap transaction is completed, you will receive your BONE or knBONE tokens and the accumulated rewards.

### Bonus rewards

Farming functionality goes beyond standard reward structures. We offer multiple **Bonus reward pools** to incentivize participation and magnify your rewards. These special reward pools provide additional rewards from our partners on top of the base rewards earned through regular staking and zapping.

<figure><img src=".gitbook/assets/image (22).png" alt=""><figcaption><p>Bonus rewards</p></figcaption></figure>

No extra actions are required to receive these rewards. The only requirement is that you need to have the staked or zapped deposit in the farming pool while bonus rewards are being distributed. Your bonus reward share is the same as the main reward. So, the bigger your deposit, the more bonus rewards you receive.

## Real Yield Staking

The Real Yield Staking functionality empowers you to unlock the earning potential of your KNINE holdings. This innovative feature allows you to passively accumulate **BONE** rewards simply by staking your KNINE tokens. Whether you prefer the flexibility of a non-locked staking position or aim to maximize your returns through a strategic lockup period, Real Yield Staking caters to your investment goals.

### Lock/Withdraw

<figure><img src=".gitbook/assets/image (23).png" alt=""><figcaption><p>Lock KNINE - Real Yield Staking</p></figcaption></figure>

To start staking at Real Yield Staking with the Lock option, you need to choose the lockup period and lock your KNINE tokens in the staking protocol. The longer you lock, the larger your deposit boost and rewards will be:

1. Connect your wallet, switch to the Shibarium chain
2. Open the "Lock" tab
3. Enter the amount of KNINE you would like to lock
4. Choose the lockup period ( 1 to 12 months)
5. Click "Lock" and confirm the transaction in your wallet
6. Wait for the transaction to complete

Once the deposit transaction is completed, you will start accumulating the BONE rewards. Claiming rewards is available at anytime.

{% hint style="info" %}
For the ongoing **locked** staking you have 3 more options:

1. Increase lock period without depositing
2. Add more KNINE to current deposit
3. Add more KNINE and increase your deposit

When increasing the lockup (options 1 and 3), you are basically setting the new lockup period. So, you won't be able to choose the lockup lower then your remaining lockup time.
{% endhint %}

When the lockup period is finished, you will be able to unstake your KNINE:

1. Connect your wallet, switch to the Shibarium chain
2. Open the "Lock" tab
3. Click the "Withdraw" button and confirm the transaction in your wallet
4. Wait for the transaction to complete

{% hint style="info" %}
If "Withdraw" button is unavailable, then your tokens are currently locked and unavailable to withdraw.
{% endhint %}

Once the unstake transaction is completed, you will receive your previously deposited KNINE and the accumulated rewards.

### Stake/Withdraw

<figure><img src=".gitbook/assets/image (24).png" alt=""><figcaption><p>Stake KNINE - Real Yield Staking</p></figcaption></figure>

To start staking at Real Yield Staking with Stake option, you need to simply deposit your KNINE to staking protocol. No locking is applied, you are free to deposit and withdraw anytime. Staking earns the rewards at a base rate:

1. Connect your wallet, switch to Shibarium chain
2. Open the "Stake" tab
3. Enter the amount of KNINE you would like to deposit
4. Click "Stake" and confirm the transaction in your wallet
5. Wait for the transaction to complete.

Once the deposit transaction is completed, you will start accumulating the BONE rewards. Claiming available anytime.

For the ongoing staking (without locking) you have an option to add more KNINE. This will increase your reward share and is also available to unstake anytime.

When you decide to unstake, you need to:

1. Connect your wallet, switch to the Shibarium chain
2. Open the "Stake" tab
3. Click the "Withdraw" button and confirm the transaction in your wallet
4. Wait for the transaction to complete.

Once the unstake transaction is completed, you will receive your previously deposited KNINE and the accumulated rewards.

## Vesting

The Vesting app at K9 Finance DAO empowers you to unlock the value of your esKNINE (Escrowed KNINE) tokens gradually over a predetermined period. This feature allows you to lock your esKNINE tokens and convert it into KNINE tokens, distributed linearly throughout the vesting period.

### Deposit/Claim

<figure><img src=".gitbook/assets/image (25).png" alt=""><figcaption><p>esKNINE Vesting UI</p></figcaption></figure>

{% hint style="success" %}
The basic rule for Vesting participation:&#x20;

You must lock KNINE tokens at Real Yield Staking for at least 6 months (180 days). This locked amount defines your vesting potential according to the backing ratio.
{% endhint %}

To enable vesting, at first, you need to complete the **basic rule.** After that you will become eligible:

1. Connect your wallet, switch to the Shibarium chain
2. Open the Vesting page
3. Enter the amount of esKNINE you would like to deposit
4. Click "Vest" and confirm the transaction in your wallet
5. Wait for the transaction to complete

Once the deposit transaction is completed, you will start accumulating the KNINE tokens. Claiming available anytime.

{% hint style="info" %}
Vesting page displays your vesting status:

1. Your vesting limit - how much esKNINE you can vest
2. Your vesting stats
   1. Vested amount
   2. Time left
   3. Accumulated KNINE tokens
{% endhint %}

When you want to claim your accumulated KNINE, you need to:

1. Connect your wallet, switch to the Shibarium chain
2. Open the Vesting page
3. Click the "Claim" button and confirm the transaction in your wallet
4. Wait for the transaction to complete

Once the claim transaction completed, you will receive your accumulated KNINE.
