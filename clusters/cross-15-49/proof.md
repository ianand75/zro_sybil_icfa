# Addresses

see address.csv file

# Number of addresses in this cluster

49

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

arb

**Funder Address**

0xe75fdb0d99e451bd1ac3ee6f14fdd6457197ec1a

**Number of addresses involved on chain arb**

49

**Transactions executing fund transfer**

https://arbiscan.io/tx/0x89a341921f03aeac3f941d611cc5869c83a074826bfe32abf4e8b8bb16ebb70a



---

**Chain**

op

**Funder Address**

0xe75fdb0d99e451bd1ac3ee6f14fdd6457197ec1a

**Number of addresses involved on chain op**

49

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0xe4a0033c0c91a116c0122b02db4b6cc481bd72e32ad98d21d13529a83551a2a6



---

**Chain**

fantom

**Funder Address**

0xe75fdb0d99e451bd1ac3ee6f14fdd6457197ec1a

**Number of addresses involved on chain fantom**

49

**Transactions executing fund transfer**

https://ftmscan.com/tx/0x82d23b7cb8252ed8ed4c3768ffb0723b2a11573afd80b52b9f001bbbb2671972



---

**Chain**

polygon

**Funder Address**

0xe75fdb0d99e451bd1ac3ee6f14fdd6457197ec1a

**Number of addresses involved on chain polygon**

49

**Transactions executing fund transfer**

https://polygonscan.com/tx/0x06d418514b812d694798fdaca7f451e76d1f424db6913b3ac22898ce345a865d



# Observed GCTS

19 common PSDs observed:

Polygon_0x0e1f20075c90ab31fc2dd91e536e6990262cf76d_Kava_0x4c24ba5177365b4c0ebae62b31945d830a858673
Polygon_0x803305930c1bbae396d03f496a7bf53ad7fd4303_Avalanche_0x803305930c1bbae396d03f496a7bf53ad7fd4303
Gnosis_0xe266eedb13a69af15c1756a241021905b1827f6a_Fuse Mainnet_0x811bcf49225ffe8039989a30cf5c03f60660753d
Moonbeam_0x671861008497782f7108d908d4df18ebf9598b82_Celo Mainnet_0xc20a842e1fc2681920c1a190552a2f13c46e7fcf
Polygon_0x222228060e7efbb1d78bb5d454581910e3922222_Harmony_0x222228060e7efbb1d78bb5d454581910e3922222
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883
Avalanche_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944_Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944
Polygon_0x0e1f20075c90ab31fc2dd91e536e6990262cf76d_DFK_0x457fd60ffa26576e226252092c98921f12e90fbb
Gnosis_0xb58f5110855fbef7a715d325d60543e7d4c18143_Fuse Mainnet_0xffd57b46bd670b0461c7c3ebbaedc4cdb7c4fb80
Polygon_0x0e1f20075c90ab31fc2dd91e536e6990262cf76d_Gnosis_0x556f119c7433b2232294fb3de267747745a1dab4
Polygon_0x0e1f20075c90ab31fc2dd91e536e6990262cf76d_Moonbeam_0x671861008497782f7108d908d4df18ebf9598b82
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944
Polygon_0x523d5581a0bb8bb2bc9f23b5202894e31124ea3e_Celo Mainnet_0x83017335bae4837016311bdb75df5a320b54d636
Polygon_0x0e1f20075c90ab31fc2dd91e536e6990262cf76d_Celo Mainnet_0xc20a842e1fc2681920c1a190552a2f13c46e7fcf
Kava_0x4c24ba5177365b4c0ebae62b31945d830a858673_Arbitrum Nova_0xb6789dacf323d60f650628dc1da344d502bc41e3
Polygon_0xa184998ec58dc1da77a1f9f1e361541257a50cf4_Gnosis_0xb58f5110855fbef7a715d325d60543e7d4c18143
Polygon_0xca0d86afc25c57a6d2acdf331cabd4c9cee05533_Moonriver_0xef2dbdfec54c466f7ff92c9c5c75abb6794f0195
Harmony_0x222228060e7efbb1d78bb5d454581910e3922222_Moonbeam_0x222228060e7efbb1d78bb5d454581910e3922222
Gnosis_0x556f119c7433b2232294fb3de267747745a1dab4_Fuse Mainnet_0xf6b88c4a86965170dd42dbb8b53e790b3490b912

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
