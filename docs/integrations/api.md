# API

Response schema and examples are available in the <mark style="color:yellow;">**link**</mark> <mark style="color:yellow;"></mark>_<mark style="color:yellow;">(will update when protocol goes live)</mark>_

## Liquid Staking&#x20;

### Liquid Staking APR[​](https://docs.lido.fi/integrations/api#lido-apr) <a href="#lido-apr" id="lido-apr"></a>

This APR value is based on Simple Moving Average of APR values over a period of 7 days.

{% code fullWidth="false" %}
```
(will update when protocol goes live)
```
{% endcode %}

### ETH Price[​](https://docs.lido.fi/integrations/api#lido-apr) <a href="#lido-apr" id="lido-apr"></a>

Returns the ETH price for further calculations.

{% code fullWidth="false" %}
```
(will update when protocol goes live)
```
{% endcode %}

### Liquid Staking rewards[​](https://docs.lido.fi/integrations/api#lido-apr) <a href="#lido-apr" id="lido-apr"></a>

Returns the liquid staking rewards history stats per user.

```
(will update when protocol goes live)
```

#### Parameters[​](https://docs.lido.fi/integrations/api#parameters) <a href="#parameters" id="parameters"></a>

The only required query parameter is `address`.

Optional Parameters:

* `currency`: USD/EUR/GBP - Fiat currency in which to display stETH denominated in fiat. **USD** by default.
* `onlyRewards`: true/false - Include only rewards without transfers or staking, **false** by default.
* `sort`: asc/desc - Sort of transactions by blockTime. **desc** by default.
* `skip`: number - Amount of data items to skip.
* `limit`: number - Maximum amount of data items to respond with.

`skip` and `limit` params are used for pagination eg:

```
skip: 0, limit: 100 = 1 page
skip: 100, limit: 100 = 2 page
skip: 200, limit: 100 = 3 page
```

### Liquid Staking stats[​](https://docs.lido.fi/integrations/api#lido-apr) <a href="#lido-apr" id="lido-apr"></a>

Returns the liquid staking protocol stats.

```
(will update when protocol goes live)
```

### knBONE total supply <a href="#lido-apr" id="lido-apr"></a>

Returns the knBONE token total supply.

```
(will update when protocol goes live)
```

### Validators <a href="#lido-apr" id="lido-apr"></a>

Returns the list of validators connected to the liquid staking protocol.

```
(will update when protocol goes live)
```

## Farming

### Farming pools list[​](https://docs.lido.fi/integrations/api#lido-apr) <a href="#lido-apr" id="lido-apr"></a>

Returns the list of all farming pools within the Farming functionality of K9 Finance DAO.

{% code fullWidth="false" %}
```
(will update when protocol goes live)
```
{% endcode %}

### Farming pool info[​](https://docs.lido.fi/integrations/api#lido-apr) <a href="#lido-apr" id="lido-apr"></a>

Returns the full info about the farming pool within the Farming functionality of K9 Finance DAO from ordered list.

{% code fullWidth="false" %}
```
(will update when protocol goes live)
```
{% endcode %}

### Farming pool info[​](https://docs.lido.fi/integrations/api#lido-apr) <a href="#lido-apr" id="lido-apr"></a>

Returns the full info about the farming pool within the Farming functionality of K9 Finance DAO by pool address.

{% code fullWidth="false" %}
```
(will update when protocol goes live)
```
{% endcode %}

### Farming pool - Bonus reward[​](https://docs.lido.fi/integrations/api#lido-apr) pools <a href="#lido-apr" id="lido-apr"></a>

Returns the full info about the bonus reward pools of the farming pool by its address.

{% code fullWidth="false" %}
```
(will update when protocol goes live)
```
{% endcode %}

### Farming pool - Bonus reward[​](https://docs.lido.fi/integrations/api#lido-apr) pool <a href="#lido-apr" id="lido-apr"></a>

Returns the full info about the bonus reward pool of the farming pool by its address and bonus pool id.

{% code fullWidth="false" %}
```
(will update when protocol goes live)
```
{% endcode %}

### Price rates[​](https://docs.lido.fi/integrations/api#lido-apr) <a href="#lido-apr" id="lido-apr"></a>

Returns a list of multiple rates for further calculations.

{% code fullWidth="false" %}
```
(will update when protocol goes live)
```
{% endcode %}

{% hint style="info" %}
Testnet response schema and examples are available in the !testnet app swagger link!
{% endhint %}

