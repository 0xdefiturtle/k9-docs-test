---
description: Decentralized multisig DAO operations
---

# Administration

K9 Finance DAO is governed by the decentralized autonomous organization. Members of the DAO — holders of the KNINE governance token — can vote on high-level proposals, such as whether to add new functionality. For day-to-day tasks, we have a much more narrowly scoped need for somebody to execute privileged operations: an administrator. The administrator rights reside with the DAO multisig wallet (k9safe.eth).

### Administrator responsibilities[​](https://docs.polygon.lido.fi/administration/#administrator-responsibilities) <a href="#administrator-responsibilities" id="administrator-responsibilities"></a>

K9 Finance DAO is a program that runs on the Ethereum and Shibarium blockchain. The Program has an upgrade authority: an address that can replace the program with a newer version. This upgrade authority has a lot of power, which means it is essential to have that power delegated to a multisig wallet on behalf of the DAO.

### Multisig administration[​](https://docs.polygon.lido.fi/administration/#multisig-administration) <a href="#multisig-administration" id="multisig-administration"></a>

Different administration methods exist, each with different advantages and disadvantages.

* A single person could act as the administrator. This has a very low overhead, and the administrator can move quickly when there is a need to deploy a critical bug fix. However, it also places a high degree of trust in a single person.
* On the opposite side of the spectrum, a DAO program could act as the administrator. Administrative tasks could only be executed after a majority of KNINE token holders approve. This is decentralized, but it makes it very difficult to act quickly when needed.
* A good middle ground between the two extremes above is a multi-sig, a program that executes administrative tasks after m-out-of-n members have approved. For m greater than 1, no single party can unilaterally execute administrative tasks, but we only need to coordinate with m parties to get something done, not with a majority of KNINE holders.

### Multisig details[​](https://docs.polygon.lido.fi/administration/#multisig-details) <a href="#multisig-details" id="multisig-details"></a>

For K9 Finance DAO, we use the [Safe Wallet](https://safe.global/), and we require approval from 3 out of 4 members. The members are:

The multi-sig instance is used both as the upgrade authority of the program and as the manager of the Liquid Staking at the K9 Finance DAO.&#x20;

Administrator authorities are also used for K9 Finance DAO contracts management at Shibarium network:

1. Farming
   1. k9safe.eth (eth:0xDA4Df6E2121eDaB7c33Ed7FE0f109350939eDA84)
2. Real Yield Staking
   1. k9safe.eth (eth:0xDA4Df6E2121eDaB7c33Ed7FE0f109350939eDA84)
3. Vesting
   1. k9safe.eth (eth:0xDA4Df6E2121eDaB7c33Ed7FE0f109350939eDA84)

### Pause/Unpause knBONE[​](https://docs.polygon.lido.fi/administration/#pauseunpause-stmatic) <a href="#pauseunpause-stmatic" id="pauseunpause-stmatic"></a>

The knBONE contract can be paused by:

1. k9safe.eth (eth:0xDA4Df6E2121eDaB7c33Ed7FE0f109350939eDA84)

The knBONE contract can be un-paused by:

1. k9safe.eth (eth:0xDA4Df6E2121eDaB7c33Ed7FE0f109350939eDA84)

#### The functions affected when the contract is on pause[​](https://docs.polygon.lido.fi/administration/#the-functions-affected-when-the-contract-is-on-pause) <a href="#the-functions-affected-when-the-contract-is-on-pause" id="the-functions-affected-when-the-contract-is-on-pause"></a>

* submit
* requestWithdrawSplit
* delegate
* claimTokens
* distributeRewards
* claimTokensFromValidatorToContract

### Pause/Unpause NodeOperatorRegistry[​](https://docs.polygon.lido.fi/administration/#pauseunpause-nodeoperatorregistry) <a href="#pauseunpause-nodeoperatorregistry" id="pauseunpause-nodeoperatorregistry"></a>

The NodeOperatorRegistry contract can be paused by:

1. k9safe.eth (eth:0xDA4Df6E2121eDaB7c33Ed7FE0f109350939eDA84)

The NodeOperatorRegistry contract can be un-paused by:

1. k9safe.eth (eth:0xDA4Df6E2121eDaB7c33Ed7FE0f109350939eDA84)

#### The functions affected when the contract is on pause[​](https://docs.polygon.lido.fi/administration/#the-functions-affected-when-the-contract-is-on-pause-1) <a href="#the-functions-affected-when-the-contract-is-on-pause-1" id="the-functions-affected-when-the-contract-is-on-pause-1"></a>

* removeInvalidNodeOperator
* setRewardAddress

### Stop Farming Pool <a href="#pauseunpause-nodeoperatorregistry" id="pauseunpause-nodeoperatorregistry"></a>

The FarmingInstance can be stopped by the Farming factory only.&#x20;

#### The functions affected when the contract is stopped[​](https://docs.polygon.lido.fi/administration/#the-functions-affected-when-the-contract-is-on-pause-1) <a href="#the-functions-affected-when-the-contract-is-on-pause-1" id="the-functions-affected-when-the-contract-is-on-pause-1"></a>

* deposit
* changeRPS
* stopMainPool
* stopBonusPool

### Emergency Stop Real Yield Staking <a href="#pauseunpause-nodeoperatorregistry" id="pauseunpause-nodeoperatorregistry"></a>

The Real Yield Staking contract can be stopped (in case of emergency) only by the DEFAULT\_ADMIN\_ROLE.

The functions affected when contract is stopped:

* deposit

### Pause/Unpause/EmergencyStop Vesting <a href="#pauseunpause-nodeoperatorregistry" id="pauseunpause-nodeoperatorregistry"></a>

The Vesting contract can be paused, unpaused and stopped (in case of emergency) only by the DEFAULT\_ADMIN\_ROLE.

The functions affected when contract is paused:

* deposit
* claim
* pause

The functions affected when contract is stopped:

* deposit
* emergencyStop
* changeIsOnlyLocked
* setBackingRatio
* setVestingRatio
* setVestingPeriod
