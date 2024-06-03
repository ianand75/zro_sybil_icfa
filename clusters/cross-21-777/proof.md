# Addresses

see address.csv file

# Number of addresses in this cluster

777

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

op

**Funder Address**

0x9dd3fea9b2b22c45c2c50cb5532987a3fd243741

**Number of addresses involved on chain op**

777

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0x083586564308542c0403d4f80297624c974486c2a0deeffe46ab59ad5b238002
https://optimistic.etherscan.io/tx/0xc6076af263a1a22f2d9516addfc9cac435babdea8f42e584451dbd794bf31b84
https://optimistic.etherscan.io/tx/0x86d8f9d9f52d36af25513c062f1a89e4ecda6f4db8a4e878725526da6788e3ff
https://optimistic.etherscan.io/tx/0x14684d0f16c12bdf0754fe6ce549b332b61f8d42fa8bcf8579042cd2d667434e
https://optimistic.etherscan.io/tx/0xcd9ddbd73ab872a2943a0c6aadfc574d1a39d8270e73f1468634e78c5a3e3a15



---

**Chain**

arb

**Funder Address**

0x9dd3fea9b2b22c45c2c50cb5532987a3fd243741

**Number of addresses involved on chain arb**

777

**Transactions executing fund transfer**

https://arbiscan.io/tx/0xbc19484b34b0c2ea67bad1705361ad157230e67f0f062d1e3d2dde08373d8274
https://arbiscan.io/tx/0x2d21d3eb8188c30539269f6c82bd8c8b8c8440d252211c747511052ce4d38e58
https://arbiscan.io/tx/0x7a5a0441b9c2f0f0c76415c857d233412a9d07a7c06144c63467689021be96d8
https://arbiscan.io/tx/0x70c7c91225802cb76a9842d7c35962f91ddb8dd5781c1849d9e64cb05dbeff6c
https://arbiscan.io/tx/0x05090af0b1f5ae14d1e1c538e7545504657dbce48b2c3df0fe67ffbf08248b3e



---

**Chain**

polygon

**Funder Address**

0x1695593276658f7e2e8199314d4855bc7e3bf444

**Number of addresses involved on chain polygon**

777

**Transactions executing fund transfer**

https://polygonscan.com/tx/0x29a08c22283ae506d7bd57dd031daaad7b8e24f4670af9e49569f23c134c65a6
https://polygonscan.com/tx/0xf3f50f08c41cb83261e501dd514f95e99f578b93c8b1f3069dc5b1e14ce2875b
https://polygonscan.com/tx/0xbd80d7b11493767d20bcb0d856c9f9057a4a4219478f4806cb04a3f566d41eb2



---

**Chain**

op

**Funder Address**

0x563be223d261b833ad15ac0ea48b90eda9c0a4eb

**Number of addresses involved on chain op**

59

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0x29d62a7ef563a25222b302576a1d42bdd12a4cb5abcd573574d9267500e72505



---

**Chain**

arb

**Funder Address**

0x86fef3c4fd6d2bdbd38de737b1eed5c388475c4b

**Number of addresses involved on chain arb**

200

**Transactions executing fund transfer**

https://arbiscan.io/tx/0x3f67fcf014a816ae6425a9eaff43681ae76419359a834cb42c7e620e388520df



# Observed GCTS

5 common PSDs observed:

Arbitrum_0x1bacc2205312534375c8d1801c27d28370656cff_0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa
BNB Chain_0x128aedc7f41ffb82131215e1722d8366faad0cd4_Harmony_0x7ffd57563ef54c464f23b5497dd1f54481e4c008
Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883_Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
