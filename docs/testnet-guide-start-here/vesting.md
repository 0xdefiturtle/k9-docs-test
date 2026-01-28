---
description: How to use Vesting interface for esKNINE
---

# Vesting

1. Click on "Vesting" in the left hand menu\
   ![](<../.gitbook/assets/image (4).png>)
2.  This interface is for vesting esKNINE rewards received via Real Yield Staking of KNINE.<br>

    <figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXeWMZu_qI5_hxbp5OQ2vyD6s46T-Gzg17c0637p_205gZEJdxfMpgZa6obOd_L21BYQ1vcLBTqjx0OI90XjhNZBNm2Cz380W42tS3oV8bP7mNyOMWBO5TqxV5agGqKRfrsLiRG-X-cqQmEr9fMGjlZqiWDy?key=UHJy3JQkr0xZIlPVeyb1AA" alt=""><figcaption></figcaption></figure>


3.  **Read the Real Yield Staking Rules/Preconditions:**&#x20;

    1. The **basic rule** for Vesting participation:
       * You must lock KNINE tokens at Real Yield Staking for at least 6 months (180 days). This locked amount defines your vesting potential according to the backing ratio.
    2. The user can deposit their esKNINE, which will be converted to KNINE according to the vesting ratio.
    3. esKNINE converts to KNINE linearly over the vesting period. The available amount of converted KNINE tokens can be claimed at any time (as long as it is not zero).&#x20;
    4. Once vesting has started, the user can add more esKNINE to the current vesting. Adding esKNINE to active vesting will lead to vesting restart - the new amount is added to the previously deposited esKNINE, and the vesting schedule starts from day 1.&#x20;
    5. Staked tokens (in addition to locked ones) at Real Yield Staking can be taken into account for Vesting (if lockedOnly = FALSE). In this case, if the user unstakes these staked (not locked) tokens, then the vesting will be recalculated.

    Preconditions

    1. Make sure you have esKNINE tokens in your wallet;
    2. Make sure you have BONE tokens in your wallet to pay the transaction fee;
    3. Make sure that you have an active deposit on the Real Yield Staking contract with a lock period of at least 6 months. (If not, then you need to create it).
    4. Make sure your wallet is connected to Puppynet
    5. Make sure your wallet is connected to the [K9 Finance Testnet App Vesting Interface](https://testnet-app.k9finance.com/vesting)


4.  **Next you will see a form for depositing tokens into Vesting:**

    ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeU3cqCgYHJCKRTvDtJiTqeTc6RUPP5txgs-CIfkqj-xq9ub6YN490J_0xGsWNgdSzj-9nCOWSHEwp4jaPZbSJZhgaiZfSpA5rZQ9Zh9-Iaw_QpPK44HeUhIzB-J_fBhRRWw-ednHeDjAuWOFudZM16CFBA?key=UHJy3JQkr0xZIlPVeyb1AA)

    * "Amount" input field for entering the esKNINE deposit amount;
    * Your current balance of esKNINE tokens and the “Use max” button to deposit the entire amount;
    * Backing ratio - the reserve ratio of KNINE staked at Real Yield to enable vesting esKNINE;
    * Vesting ratio - the conversion rate for esKNINE;
    * Your vesting limit - shows the maximum amount of esKNINE you can currently convert according to your KNINE staked at Real Yield and the backing ratio;
    * Vesting period - the time during which esKNINE will be linearly converted to KNINE;
    * "Vest" button;<br>
5.  **On the right you will see a form that displays your Vesting status:**

    ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXedrGrBMJP4xT5MZsfp4Ggh5v6uyygrHrlew5myNVTAX1cqcRAbLrIxHQ1Hwgvz0imtHaTCS8HQvuru07NFBLvhOnAri4ZKABC0OGud2Ju0CDYSsu5zWHYSedZz1Sa9LCJwwdQT1DWuvfcmDSqj89Oj3j7Z?key=UHJy3JQkr0xZIlPVeyb1AA)

    1. Time left - displays the remaining time until the end of the current vesting. If there is no active vesting, “No Vesting” will be indicated.
    2. Total vested - displays your balance of unconverted tokens;
    3. Reward - displays the amount of converted KNINE that you can claim;
    4. "Claim" button;
    5. "ELIGIBILITY" block:
       1. “Deposited on Real Yield” or “Locked on Real Yield” (depending on the lockedOnly status) - displays the amount of your KNINE deposit in Real Yield Staking that is taken into account for Vesting;
       2. Used for Vesting - shows the amount of your KNINE staked at Real Yield that is currently being used as collateral to convert your vested esKNINE;
       3. Available for Vesting - shows the amount of your KNINE staked at Real Yield that you can currently use to convert additional esKNINE;
       4. Lock days left - displays the number of remaining days of locking KNINE tokens in Real Yield Staking;<br>
6. **Enter the esKNINE deposit amount in the "Amount" field:**

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeU3cqCgYHJCKRTvDtJiTqeTc6RUPP5txgs-CIfkqj-xq9ub6YN490J_0xGsWNgdSzj-9nCOWSHEwp4jaPZbSJZhgaiZfSpA5rZQ9Zh9-Iaw_QpPK44HeUhIzB-J_fBhRRWw-ednHeDjAuWOFudZM16CFBA?key=UHJy3JQkr0xZIlPVeyb1AA)

* Make sure "Lock days left" is greater than "Vesting period";
* Make sure the amount entered does not exceed "Your vesting limit";

7. **Click "Vest" and confirm the transaction in your wallet;**
8. **Wait for the transaction to complete. Popup window displays the transaction progress:**\
   ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeVPLJYt36chu3g6tRGyGnQBu9DjVNaZrWRmvJ6L4iq5ZjUozzC2aMjFlYasbdeZDQHsdykWHneXCuTb2J8CAVwaWZhYfrwCn2qvj7hqDh_doz9ktonrc1OJ_EQqI8SPX1Qk2yO0IbrFgMH_Ka3eaaAZxRS?key=UHJy3JQkr0xZIlPVeyb1AA)
9. **Once the transaction is completed, the updated deposit amount will appear in "Total vested";**
10. **Wait a while and check the “Reward” field. The number of KNINE converted will increase according to the vesting ratio. You can withdraw these tokens at any time.**

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeTEyokyB5dkN4fs1Fnq-gDGcQOnVD-LW_vsty0O7q8QCBNG9r-LNuTAe71IW4t3dPozbsVM8CE228Xr2ZDe8Y2RngX1EEUBafZFUhuZNCoLPi0Z_AtsaWzeEJiJoQwiSHdHqn_0HuQZj3nxzAgDCd6QXMq?key=UHJy3JQkr0xZIlPVeyb1AA)

8. **Click the "Claim" button and confirm the transaction;**
9. **Wait for the transaction processing to complete (the transaction status is displayed in a modal window);**

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeXqtqpFiPGxgIKAK_7B4XrqKe6JIyf5GEoUuV0XrheZbVtiDaAbaslndAYdLbexAKSygpO1SZp1cs93htTUebkKzD7HjCcj4h4ArZyRvIqOSP8MOTFqsxdtrSkXkMLdUgWhQaoRyYusdljDXOR9b_ANn5G?key=UHJy3JQkr0xZIlPVeyb1AA)

10. After completing the transaction, check the KNINE balance in your wallet;<br>
11. Wait until the end of the “Vesting period” and click the “Claim” button again to receive the accumulated KNINE tokens.

### Steps to Add More esKNINE to Existing Vesting

You can increase your esKNINE deposit to active vesting by entering a new amount in the "Amount" field and clicking the "Vest" button:

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfaX1kmrib-1jwXPrYBYuZMv2FmXQgqRh0NpYXv850B2q6kmeKvuORmtImWufVaCS0Mb1sC5SMwKty4h349tJWA1lZc37R79Y72lYGO2CpqzDlcYsLnqZn0ysaOuFWikgNSw2UqjaOf6Qfk8NhRD6RJJOq7?key=UHJy3JQkr0xZIlPVeyb1AA" alt=""><figcaption></figcaption></figure>

1. Make sure that the new amount does not exceed "Your vesting limit";
2. Make sure that the "Lock days left" of your Real Yield Staking deposit is greater than the "Vesting period";
3. Confirm the transaction in your wallet and wait until the transaction is processed (the transaction status is displayed in a modal window);\
   ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcvu9jYicU9i6Z5Hj-NEQPA772OTIhQYHf8dHUUm8C1j3R7GfKdENt78n9oZa-VxuUvExJ_h8QhsWFrtkmWQqN6g-PvBD_7ZKxisl6TfsMkYQFtDgd-iTT92kI1tULsWijczgDeMN-UDs8NJHqvjqyAc5M?key=UHJy3JQkr0xZIlPVeyb1AA)

Vesting will be restarted and the new deposit will be added to the esKNINE balance. Wait for a while and check that the number of converted KNINEs increases in accordance with the new vesting ratio.

1. Make sure the reward amount is displayed in the "Reward" field;\
   ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeaimPYti3O3UN24ehbSlWaKeWTIWU89C36o7qfnzcuTKEx6UeVx4HSEg71uXVAh_JoMTmaTUOEVbwORow_Ts0JBgPfwdF-NBufWcw9XShs0Rrar-Hf7cHZWkkABsVgx1aOzTq-PFQv29Ip84l_bj6wrWU?key=UHJy3JQkr0xZIlPVeyb1AA)
2. Click the "Claim" button and confirm the transaction:
   * Make sure that the amount of KNINE on your balance has increased by the stated amount;
3. Wait until the end of the new “Vesting period” and press the “Claim” button again to claim the rest of the reward:
   * Make sure that the remaining reward (KNINE) has been successfully received.

### How unstaking from Real Yield Staking affects your Vesting

An option is available for Vesting - take into account KNINE tokens from Real Yield Staking that are deposited without lockup.&#x20;

You can determine whether this option is available by looking at the Deposited on Real Yield / Locked on Real Yield field in the ELIGIBILITY block. If ‘Deposited on Real Yield’ is specified, then Vesting is allowed to additionally use KNINE tokens staked without lockup.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXe5F2uOaDFvPhs59VFMhjjvTh3NS4tVCKls3uV87FrkeQpBoL7eu8_yj-SGhR0YLKcegSuw-0IIRQLCphVuoWHnBfLlP1fYx9T1IXTkSe1akjDS4udycDO-EIk7H2l688J3IWnq314_L_f8UybYFJSCbzzP?key=UHJy3JQkr0xZIlPVeyb1AA)

If such tokens are used to provide your vesting, then their premature withdrawal will affect such vesting. The amount of your esKNINE deposit will be reduced in proportion to the amount of KNINE withdrawn from staking.

1.  Unstake your staked (not locked) KNINE tokens on the Real Yield Staking -> Stake page (see Real Yield Staking Guide);<br>

    <figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXecaKp_Wk3CkEQIhRifd_Q5kRHZj9PZwAfKLRNt7Jpf7VaLE0rmob_hs5Ysq4WCHW_Q7IGPadZXjFlPvlbpzMOnJDR9F8pcO-OiVuwGaF2y23m-IjCOiNxjD4wdfn3jL9X5C0Yuo77jU1oY5cvh34qtjEg?key=UHJy3JQkr0xZIlPVeyb1AA" alt=""><figcaption></figcaption></figure>
2. Go to the Vesting page to see your updated Vesting settings (form on the right):
   * Make sure that the esKNINE deposit balance has been recalculated in accordance with the new conditions.

