# Addresses

see address.csv file

# Number of addresses in this cluster

206

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

0xdf674bd92a383d6ddf29d3270d72157b2f97d77f

**Number of addresses involved on chain op**

206

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0xde46f813f61e1a4292b3edca8ca320f16a2943889584a7fd51cdb4f02d9846e6



---

**Chain**

arb

**Funder Address**

0xdf674bd92a383d6ddf29d3270d72157b2f97d77f

**Number of addresses involved on chain arb**

206

**Transactions executing fund transfer**

https://arbiscan.io/tx/0x07e7258f01b8c8db4e00a956546db01bd68a9106858945dfd5af26d9ea0d1566



---

**Chain**

polygon

**Funder Address**

0xdf674bd92a383d6ddf29d3270d72157b2f97d77f

**Number of addresses involved on chain polygon**

200

**Transactions executing fund transfer**

https://polygonscan.com/tx/0x367d25cba25a353e028f1b01f33057f299f7dad0864254b72c7a1625fb0a0208



# Observed GCTS

6 common PSDs observed:

Polygon_0xa184998ec58dc1da77a1f9f1e361541257a50cf4_Celo Mainnet_0xe33519c400b8f040e73aeda2f45dfdd4634a7ca0
BNB Chain_0x6694340fc020c5e6b96567843da2df01b2ce1eb6_Metis_0x45f1a95a4d3f3836523f5c83673c797f4d4d263b
Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883_Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944
Avalanche_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944_Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
