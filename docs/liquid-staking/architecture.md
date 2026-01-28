# Architecture

The K9 Finance DAO Liquid Staking architecture has 6 main parts:

* **KnBONE** contract
* **UnstBONE NFT** contract
* **NodeOperatorRegistry** contract
* **InstantPool** contract
* **BridgeETH** contract
* **BridgeSHIB** contract

## KnBONE contract[​](https://docs.polygon.lido.fi/architecture#stmatic-contract) <a href="#stmatic-contract" id="stmatic-contract"></a>

The KnBONE contract is an ERC20 token contract which performs the following functions:

* User interaction
* Delegate to validators
* Reward Distribution
* Manage withdrawals
* Manage reward fees
* Mint and burn NFTs

Sensitive contract interaction and management is executed by the following roles:

* PAUSE\_ROLE - pauses the KnBONE contract
* UNPAUSE\_ROLE - unpauses the KnBONE contract
* DAO\_ROLE - responsible for the main contract settings
* BRIDGE\_ROLE - manages the token transfer between Ethereum and Shibarium when user deposits/withdraws.

### User Interaction <a href="#user-interaction" id="user-interaction"></a>

A user can interact only with the KnBONE staking contract to:

* Submit ERC20 BONE
* Request Withdrawal
* Claim withdraw
* Call ERC20 functions

Users can submit BONE and get knBONE  automatically by calling the `submit` function inside the KnBONE contract and passing the delegated amount.

### Depositing BONE and minting knBONE[​](https://docs.polygon.lido.fi/architecture#minting-stmatic) <a href="#minting-stmatic" id="minting-stmatic"></a>

The total amount of knBONE that a user will get when delegate his BONE tokens is calculated as follows:

`sharePerUser = submittedBONE * totalShares / totalPooledBONE`

The **totalPooledBONE is the total amount of the buffered tokens (submitted by the user but not yet delegated) plus the total delegated.**

`totalPooledBONE = totalStaked + totalBuffered + calculatePendingBufferedTokens() - reservedFunds`

#### **Example:**[**​**](https://docs.polygon.lido.fi/architecture#example)

#### **Case 1**[**​**](https://docs.polygon.lido.fi/architecture#case-1)

Initial state

<table><thead><tr><th width="228">totalShares</th><th>0</th></tr></thead><tbody><tr><td>totalPooledBONE</td><td>0</td></tr></tbody></table>

User A submits:

* submit ==> 1000 BONE
* receive ==> 1000 knBONE

Updated state:

<table><thead><tr><th width="234">totalShares</th><th>1000</th></tr></thead><tbody><tr><td>totalPooledBONE</td><td>1000</td></tr></tbody></table>

Users Shares:

<table><thead><tr><th width="117">User</th><th>userP = userShares / totalShares</th><th>userBONE = userP * totalPooledBONE</th></tr></thead><tbody><tr><td>1</td><td>1 = 1000 / 1000</td><td>1 * 1000 = 1000</td></tr></tbody></table>

#### **Case 2**[**​**](https://docs.polygon.lido.fi/architecture#case-2)

User B submits:

* submit ==> 500 BONE
* receive ==> 500 \* 1000 / 1000 = 500 knBONE

Update state:

<table><thead><tr><th width="229">totalShares</th><th>1500</th></tr></thead><tbody><tr><td>totalPooledBONE</td><td>1500</td></tr></tbody></table>

Users Shares:

<table><thead><tr><th width="124">User</th><th>userP = userShares / totalShares</th><th>userBONE = userP * totalPooledBONE</th></tr></thead><tbody><tr><td>1</td><td>0.66 = 1000 / 1500</td><td>0.66 * 1500 = 1000</td></tr><tr><td>2</td><td>0.33 = 500/ 1500</td><td>0.33 * 1500 = 500</td></tr></tbody></table>

#### **Case 3**[**​**](https://docs.polygon.lido.fi/architecture#case-3)

The system was slashed => -100 BONE

Updated state:

<table><thead><tr><th width="236">totalShares</th><th>1500</th></tr></thead><tbody><tr><td>totalPooledBONE</td><td>1500 - 100 = 1400</td></tr></tbody></table>

Users Shares:

<table><thead><tr><th width="125">User</th><th>userP = userShares / totalShares</th><th>userBONE = userP * totalPooledBONE</th></tr></thead><tbody><tr><td>1</td><td>0.66 = 1000 / 1500</td><td>0.66 * 1400 = 933.33</td></tr><tr><td>2</td><td>0.33 = 500/ 1500</td><td>0.33 * 1400 = 466.66</td></tr></tbody></table>

#### **Case 4**[**​**](https://docs.polygon.lido.fi/architecture#case-4)

User C submits:

* submit ==> 500 BONE
* receive ==> 500 \* 1500 / 1400 = 535.71 knBONE

Updated state:

<table><thead><tr><th width="236">totalShares</th><th>2035.71</th></tr></thead><tbody><tr><td>totalPooledBONE</td><td>1900</td></tr></tbody></table>

Users Shares:

<table><thead><tr><th width="123">User</th><th>userP = userShares / totalShares</th><th>userBONE = userP * totalPooledBONE</th></tr></thead><tbody><tr><td>1</td><td>0.4912= 1000 / 2035.71</td><td>0.4912 * 1900 = 933.33</td></tr><tr><td>2</td><td>0.2456= 500 / 2035.71</td><td>0.2456 * 1900 = 466.66</td></tr><tr><td>3</td><td>0.2631= 535.71 / 2035.71</td><td>0.2631 * 1900 = 500</td></tr></tbody></table>

#### **Case 5**[**​**](https://docs.polygon.lido.fi/architecture#case-4-1)

The system accumulates reward => +200 BONE

Updated state:

<table><thead><tr><th width="238">totalShares</th><th>2035.71</th></tr></thead><tbody><tr><td>totalPooledBONE</td><td>1900 + 200 = 2100</td></tr></tbody></table>

Users Shares:

<table><thead><tr><th width="119">User</th><th>userP = userShares / totalShares</th><th>userBONE = userP * totalPooledBONE</th></tr></thead><tbody><tr><td>1</td><td>0.4912= 1000 / 2035.71</td><td>0.4912 * 2100=1031.52</td></tr><tr><td>2</td><td>0.2456= 500 / 2035.71</td><td>0.2456 * 2100= 515.76</td></tr><tr><td>3</td><td>0.2631= 535.71 / 2035.71</td><td>0.2631 * 2100= 552.62</td></tr></tbody></table>

When the system gets slashed, the total pooled BONE decreases, and it increases when a user submits BONE again or the system gets rewarded.

### Delegate to Validators[​](https://docs.polygon.lido.fi/architecture#delegate-to-validators) <a href="#delegate-to-validators" id="delegate-to-validators"></a>

The knBONE contract is used to delegate tokens to validators.

The delegation flow is based on the actual `totalBuffered` BONE contained inside the KnBONE contract, when we reach the `delegationLowerBound`, we start to delegate to all the Staked operators.

Delegation is performed as a scheduled job by a Delegator/Distributor bot.

### Manage Withdrawals[​](https://docs.polygon.lido.fi/architecture/#manage-withdrawals) <a href="#manage-withdrawals" id="manage-withdrawals"></a>

The withdrawal uses the ValidatorShare API - an interface of ValidatorShare contract to interact with the validator. This allows us to have a nonce that we can use to map each user request with this nonce. The knBONE contract tracks each validatorShare nonce which will increment each time a new withdrawal request happens.

1. Request withdrawal: When a user requests the system to withdraw his BONE tokens by withdrawal request, a new ERC721 token is minted and mapped to this request. The owner can trade this token, sell it or use it to claim his BONE tokens.
   1. The user requests withdrawal
   2. Withdrawal request NFT is minted and mapped with the request by its id
   3. The request nonce of the validatorShare and validatorShare address are stored
   4. The sellVoucher\_new function is called
2. Instant Withdraw: When a user requests the instant withdrawal, BONE is withdrawn from the instant reward pool and the instant reward fee is applied.
   1. The user requests instant withdrawal
   2. BONE is withdrawn from instant reward pool, no interaction with the ValidatorShare API
3. Claim tokens:
   1. The user calls the claim token function and passes the tokenId
   2. Check if the msg.sender is the owner of this NFT
   3. Call the claim unstake tokens function on the validatorShare contract
   4. Transfer tokens to the user
   5. Burn the NFT

### Distribute Rewards[​](https://docs.polygon.lido.fi/architecture/#distribute-rewards) <a href="#distribute-rewards" id="distribute-rewards"></a>

BONE tokens are accumulated and stored inside the KnBONE contract upon 2 events:

1. Each time a user requests to withdraw, the validatorShare contract transfers the rewards
2. Scheduled job by the Delegator/Distributor bot.

&#x20;The protocol regularly check if the amount is greater than `rewardDistributionLowerBound` (a variable that can be set). If that requirement is fulfilled, knBONE calculates the amount of Protocol Fee, transfers it to the receivers. Finally, the remaining BONE tokens are added to the BONE buffer and re-delegated to validators, which increases totalPooledBONE value.&#x20;

The Protocol Fee is distributed between:

* DAO treasury - used to cover the DAO costs and other expenses;&#x20;
* Operator reward - split evenly between all validators;
* Instant Withdraw pool - the amount that is accumulated for instant rewards payment (when claimed by a user);
* Real Yield Staking - the share of tokens that is used to refill the rewards.

### Withdraw Total Delegated[​](https://docs.polygon.lido.fi/architecture/#withdrawtotaldelegated) <a href="#withdrawtotaldelegated" id="withdrawtotaldelegated"></a>

When an operator gets unstaked, the nodeOperator contract calls `withdrawTotalDelegated` function which claims all the delegated BONE from the unstaked validator. An NFT token is minted and mapped with this request, later a `claimTokensFromValidatorToContract` function is called to withdraw BONE from the validatorShare.

### ValidatorShare contract interaction[​](https://docs.polygon.lido.fi/architecture/#validatorshare-behaviour) <a href="#validatorshare-behaviour" id="validatorshare-behaviour"></a>

When a user requests withdrawal, the validatorShare contract automatically transfers the accumulated rewards. The same thing happens when BONE tokens are delegated.&#x20;

When this transfer happens, we consider the received BONE tokens, same as any BONE that was not submitted and buffered, as a reward. And later these tokens are distributed and re-delegated.&#x20;

#### ValidatorShare API[​](https://docs.polygon.lido.fi/architecture/#validatorshare-api) <a href="#validatorshare-api" id="validatorshare-api"></a>

The KnBONE implements the validatorShare contract API:

1. BuyVoucher: buy shares from a validator link
2. SellVoucher\_new: sell an amount of shares
3. unstakeClaimTokens\_new: claim the token by a nonce
4. getTotalStake: get the total staked amount
5. getLiquidRewards: get the accumulated rewards

and other functions to interact with the ValidatorShare contract of a node operator.

## UnstBONE NFT contract[​](https://docs.polygon.lido.fi/architecture/#polidonft) <a href="#polidonft" id="polidonft"></a>

The UnstBONE contract is an ERC721 contract used by the KnBONE contract to manage withdrawal requests.

Each time a user calls the `requestWithdrawSplit` function inside the KnBONE contract and creates a withdrawal request, a new NFT is minted and mapped with the request.

When a user owns an NFT he can:

* Claim BONE from the withdraw request
* Trade NFT to someone else, who will then be able to claim
* Approve it to someone else who will then also be able to claim

This ERC721 is slightly modified so it returns a list of owned tokens of an address by using the public mapping `owner2Tokens`. Same goes for retrieving the list of approved tokens by using the mapping `address2Approved`.

## NodeOperatorRegistry contract[​](https://docs.polygon.lido.fi/architecture#operator-contract) <a href="#operator-contract" id="operator-contract"></a>

This contract is responsible for the Node operators management and their parameters. All decisions are made by DAO and and then executed by the following roles:

* PAUSE\_ROLE - pauses the NodeOperatorRegistry contract
* UNPAUSE\_ROLE - unpauses the NodeOperatorRegistry contract
* DAO\_ROLE - responsible for the main contract settings. Some functions are available only to the Node operator owner.
* ADD\_NODE\_OPERATOR\_ROLE - adds new node operator to the protocol
* REMOVE\_NODE\_OPERATOR\_ROLE - removes the node operator from protocol

### Manage Operators[​](https://docs.polygon.lido.fi/architecture#manage-operators) <a href="#manage-operators" id="manage-operators"></a>

1. Add an operator
   1. A new Operator expresses their interest to join the K9 Finance DAO protocol.
   2. The DAO votes to include the new operator
   3. The validator is added to the Node Operators List by `ADD_NODE_OPERATOR_ROLE` using `addNodeOperator`
2. Exit Node operator registry
   1. Node Operator owner decides to leave the K9 Finance DAO protocol
   2. This owner calls `exitNodeOperatorRegistry` (only the owner can call this function)
   3. Delegated BONE is withdrawn from validator and claimed later by a cron job
   4. Node operator is removed from the operators list
3. Remove Node operator
   1. DAO made a decision about removing an operator
   2. Node operator is removed by `REMOVE_NODE_OPERATOR_ROLE` using `removeNodeOperator`
   3. Delegated BONE is withdrawn from validator and claimed later by a cron job
   4. Node operator is removed from the operators list
4. Remove invalid Node operator
   1. An invalid operator was detected by DAO (UNSTAKED or EJECTED status)
   2. This invalid operator is removed using `removeInvalidNodeOperator`
   3. Delegated BONE is withdrawn from validator and claimed later by a cron job
   4. Node operator is removed from the operators list

Multiple 'view' functions are implemented to get the updated info about validators and the system state.&#x20;

## InstantPool contract <a href="#operator-contract" id="operator-contract"></a>

Instant pool is used for storing and paying out BONE tokens when user requests instant rewards. Only the following roles can interact with the contract:

* PAUSE\_ROLE - pauses the InstantPool contract
* UNPAUSE\_ROLE - unpauses the InstantPool contract
* WITHDRAWER\_ROLE - transfers BONE from contract to user.

So, when user requests instant rewards, the `withdraw` function is called by KnBONE contract. By calling this function the BONE transfer is performed to the user's wallet. Only the KnBONE contract can call this function since it is the only instance that manages the rewards.

## BridgeETH and BridgeSHIB

These two contracts are used for:

* when user submits - transfer the knBONE tokens from Ethereum to Shibarium
* when user withdraws - transfer the knBONE tokens from Shibarium to Ethereum.
