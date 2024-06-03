# Addresses

see address.csv file

# Number of addresses in this cluster

347

# Reasoning

This cluster, funded by **Indirect Common Funder**, employs smart contracts to obscure the from-to relationship of fund transfers. It contains over 20 addresses sourced from the snapshot database, none of which are initially labeled. The funder address originates from a non-CEX source. Notably, batch funding activities on this cluster has been observed across multiple chains, as listed below. These factors strongly suggest the cluster's potential for being a sybil, controlled and financed by a single entity.

Also, We do behavioral verfication on this cluster to show this cluster is not only funded by single entity but they are not independent in performing activities.

# Behavioral verification

**PSD**

We create a unique transaction identifier PSD by concatenating the following attributes together.

PSD = concat(SOURCE_CHAIN, SOURCE_CONTRACT, DESTINATION_CHAIN, DESTINATION_CONTRACT)

From the snapshot database, we calculate the PSD frequencies.

$$ p_i = \text{freq}(PSD_i) $$

There are more than 63000 different transactions in total and the most called transaction is

$$
p_{max} = p(Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Optimism_0x701a95707a0) = 0.031870928992508665
$$

**Greatest Common Transaction Set (GCTS)**

The Greatest Common Transaction Set (GCTS) is a set of unique transaction patterns shared among users within a cluster. The presence of a GCTS suggests that users within the group are engaging in similar transactions or following common strategies.

$$
\text{GCTS} = \{ \text{PSD}_1, \text{PSD}_2, \ldots, \text{PSD}_k \}
$$

**GCTS under independent user group**

We calculate the probability that a group of $n$ **independent** users has a GCTS of size $k$, where each $PSD_𝑖$ has a frequency $p_i$.
​

- Probability of a single user including a specific $PSD_i$, the probability is $p_i$
- For all n users to include the same PSD, the probability is $p_i^n$
- Probability of Including a Specific Set of 𝑘 PSDs:
  The probability that all $n$ users include the same specific set of $k$ PSDs (let's call this set $GCTS=\{PSD_1,PSD_2,…,PSD_𝑘\}$) is the product of the individual probabilities:

$$
P(GCTS = k | group\ is\ independent) = \prod_{i=1}^{k} p_i^n
$$

when $n > 20$ and $p_{max} < 0.032$

$$
P(CGTS = 1 | group\ is\ independent) < 0.032^{20} = 1.267*10^{-30} \rightarrow 0
$$

Therefore, the probability for an independent group of users to have GCTS is close to 0.

**Users are not independent if GCTS observed**

i.e. $P(\text{group is not independent} | \text{GCTS} > 0) \rightarrow 1$ for group of users larger than 20.

According to Bayesian Inference:

$$
P(\text{group is not independent } | \text{GCTS} > 0) = \frac{P(\text{GCTS} > 0 | \text{group is not independent}) \cdot P(\text{group is not independent})}{P(\text{GCTS} > 0 | \text{group is independent}) \cdot P(\text{group is independent}) + P(\text{GCTS} > 0 | \text{group is not independent}) \cdot P(\text{group is not independent})}
$$

where

- Prior Probability:
  We assume $P(\text{group is not independent}) = 0.5$

- Likelihood:
  $P(\text{GCTS} > 0 | \text{group is not independent})$
  This is the probability of observing a GCTS if the group is indeed not acting independently.

- Likelihood Under Independence:
  $P(\text{GCTS} > 0 | \text{group is independent})$
  This is the expected probability of a GCTS for a group of independent users. The value $P \rightarrow 0$ as we calculate earlier.

- Prior Probability of Independence:
  $P(\text{group is independent}) = 0.5$
  Since the prior probability of the group being not independent is 0.5, this is also 0.5.

Plug ​

$$
P(\text{GCTS } > 0 | \text{group is independent }) \rightarrow 0
$$

into

$$
P(\text{group is not independent } | \text{GCTS} > 0) = \frac{P(\text{GCTS} > 0 | \text{group is not independent}) \cdot 0.5}{0 \cdot 0.5 + P(\text{GCTS} > 0 | \text{group is not independent}) \cdot 0.5}
\rightarrow 1
$$


---

**Chain**

fantom

**Funder Address**

0xd2236f80c801c0b6474da0a923d9c0b124cea6e2

**Number of addresses involved on chain fantom**

347

**Transactions executing fund transfer**

https://ftmscan.com/tx/0x1461a095167d3df96eaf85600d9d374d74739dd96affbbb301bd83860c1aa32f
https://ftmscan.com/tx/0x077174f8596563562c710c12844781a0a0ad56c289c7bb74065daf9a0dc23c23



---

**Chain**

polygon

**Funder Address**

0xd2236f80c801c0b6474da0a923d9c0b124cea6e2

**Number of addresses involved on chain polygon**

347

**Transactions executing fund transfer**

https://polygonscan.com/tx/0x946b556e386e427b6a60e121631615de28918c12f7dc31f15373a8b8a0ae858b
https://polygonscan.com/tx/0x0a51a74f4ea3bf71e4b74e39fa2f092c29129bd7845be0372acbeb3ac3484009
https://polygonscan.com/tx/0x1002f10ff3bb06a129793be0f9a1e5bd28c64f48f20ebfe71b89688dc24a5855



---

**Chain**

op

**Funder Address**

0xd2236f80c801c0b6474da0a923d9c0b124cea6e2

**Number of addresses involved on chain op**

195

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0x224b58282dfda17c8bf90805fb6e1d650bc9df419c8284491d635505db9277c8



---

**Chain**

op

**Funder Address**

0xf0a5598ea2d8e7aa570fd4a5e6e0edd29452f390

**Number of addresses involved on chain op**

103

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0xf90cfe5d2e9e8fe04ec1bc3e8de852fa94cf91f4aea8f8992e4382e1dfb97c66



---

**Chain**

op

**Funder Address**

0xc7341e6e2a6a02f9e58ae2cba8dc4c4b95582ca8

**Number of addresses involved on chain op**

49

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0x7fd48fca7e1fe2e80f43d36faff2535c77ae0350b2af1d1b440fb4614ed91546



---

**Chain**

fantom

**Funder Address**

0x023a9e71848964720aa938d50f1232d34f46b470

**Number of addresses involved on chain fantom**

237

**Transactions executing fund transfer**

https://ftmscan.com/tx/0xbdc3a5ca003c0f9b52aa38c7adf1aa11a2f9e6e0b04be33d8da0ddfdea6c22ea
https://ftmscan.com/tx/0xb5c4009989d19b67de28fd049c7c9b268681e3f1fdd5a6d6f28220f05581b565



---

**Chain**

arb

**Funder Address**

0xd2236f80c801c0b6474da0a923d9c0b124cea6e2

**Number of addresses involved on chain arb**

101

**Transactions executing fund transfer**

https://arbiscan.io/tx/0x117986e0c0aa54221cd4e82121e8437a6f21213b61a031c151b3eb07562e83f1
https://arbiscan.io/tx/0x29ba9284b41f17a68517641d7c75cc7ccfed32dc3d7d0ac84ccfa2b1effdc7ba



---

**Chain**

polygon

**Funder Address**

0xc7341e6e2a6a02f9e58ae2cba8dc4c4b95582ca8

**Number of addresses involved on chain polygon**

81

**Transactions executing fund transfer**

https://polygonscan.com/tx/0x83a836f0dabd5a7d56b98b6887a4fff55707b8d05abe34869d6cb49955b8f8bf



# Observed GCTS

3 common PSDs observed:

Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883
Arbitrum_0x1bacc2205312534375c8d1801c27d28370656cff_0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa
Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883_Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
