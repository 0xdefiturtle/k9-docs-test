# Node Operators

One of the main parts of K9 Finance DAO protocol are node operators. Node operators are entities which are running Shibarium validators and are registered in the K9 Finance DAO NodeOperatorRegistry contract. They are responsible for managing a secure and stable infrastructure for running Shibarium validators for the benefit of the protocol. They are professional staking providers who can ensure the safety of the deposited funds (belonging to users) and correctness of validator operations.

### How to join as an Operator[​](https://docs.polygon.lido.fi/guides/node-operators#how-to-join-as-an-operator) <a href="#how-to-join-as-an-operator" id="how-to-join-as-an-operator"></a>

Only K9 Finance DAO can list new validators to the NodeOperatorRegistry. After the snapshot proposal with the proposed subset of node operators passes, K9 Finance DAO will list new validators in the NodeOperatorRegistry. No further action is required.

### How to exit the protocol as a Node Operator[​](https://docs.polygon.lido.fi/guides/node-operators#how-to-exit-the-protocol-as-a-node-operator) <a href="#how-to-exit-the-protocol-as-a-node-operator" id="how-to-exit-the-protocol-as-a-node-operator"></a>

Exit the Node Operator Registry by calling the `exitNodeOperatorRegistry` function. The caller address must be the reward address. By exiting, the validator is no longer part of the K9 Finance DAO protocol:

* Call `exitNodeOperatorRegistry()` function in the NodeOperatorRegistry contract.
