# Addresses

see address.csv file

# Number of addresses in this cluster

49

# Reasoning

This cluster, funded by **Indirect Common Funder**, employs smart contracts to obscure the from-to relationship of fund transfers. It contains over 20 addresses sourced from the snapshot database, none of which are initially labeled. The funder address originates from a non-CEX source. Notably, batch funding activities on this cluster has been observed across multiple chains, as listed below. These factors strongly suggest the cluster's potential for being a sybil, controlled and financed by a single entity.

Also, We do behavioral verfication on this cluster to show this cluster is not only funded by single entity but they are not independent in performing activities.

# Behavioral verification


We create a unique identifier (PSD) for a transaction by concatenating the following attributes together.

$$
\text{PSD} = \text{concat}( \text{SOURCE\_CHAIN}, \text{SOURCE\_CONTRACT}, \text{DESTINATION\_CHAIN}, \text{DESTINATION\_CONTRACT})
$$

From the snapshot database, we calculate the PSD frequencies.

$$ p_i = \text{freq}(PSD_i) $$

There are more than 63000 different transactions in total and the most called transaction is

$$
p_{max} = p(Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Optimism_0x701a95707a0) =  0.031870928992508665
$$


The Greatest Common Transaction Set (GCTS) is a set of unique transaction patterns shared among users within a cluster. The presence of a GCTS suggests that users within the group are engaging in similar transactions or following common strategies.

$$
\text{GCTS} = \{ \text{PSD}_1, \text{PSD}_2, \ldots, \text{PSD}_k \}
$$


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


$P(\text{group is not independent} | \text{GCTS} > 0) \rightarrow 1$ for group of users larger than 20.

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

Given ​$P(\text{GCTS} > 0 | \text{group is independent}) \rightarrow 0$, plug into

$$
P(\text{group is not independent } | \text{GCTS} > 0) = \frac{P(\text{GCTS} > 0 | \text{group is not independent}) \cdot 0.5}{0 \cdot 0.5 + P(\text{GCTS} > 0 | \text{group is not independent}) \cdot 0.5}
\rightarrow 1
$$


---

**Chain**

polygon

**Funder Address**

0x97467988714430d6605ea1ea4d717d9d804b975e

**Number of addresses involved on chain polygon**

48

**Transactions executing fund transfer**

https://polygonscan.com/tx/0x093c561ce987a3376f77a689662d241a17135a9b3199ef8de34284b10c2c1bd4



---

**Chain**

op

**Funder Address**

0x1706dc8fe5b1402a8b120df2d593b15011c9379e

**Number of addresses involved on chain op**

49

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0xccb194b0fb7a9e76a4182db22f7e43fba0efa04bc9652989b19cd51b9995594e



---

**Chain**

arb

**Funder Address**

0x8da0dbec8dd4ad6c6f698000b44f03842056c271

**Number of addresses involved on chain arb**

48

**Transactions executing fund transfer**

https://arbiscan.io/tx/0x174e4382800ff693b7773e14478450809cc98a4198701f9fb93e57b61865c6c4



# Observed GCTS

17 common PSDs observed:

Arbitrum_0x2297aebd383787a160dd0d9f71508148769342e3_Optimism_0x2297aebd383787a160dd0d9f71508148769342e3
Polygon_0xa184998ec58dc1da77a1f9f1e361541257a50cf4_Celo Mainnet_0xe33519c400b8f040e73aeda2f45dfdd4634a7ca0
Polygon_0x0e1f20075c90ab31fc2dd91e536e6990262cf76d_Celo Mainnet_0xc20a842e1fc2681920c1a190552a2f13c46e7fcf
Polygon_0x523d5581a0bb8bb2bc9f23b5202894e31124ea3e_Celo Mainnet_0x83017335bae4837016311bdb75df5a320b54d636
Polygon_0xa184998ec58dc1da77a1f9f1e361541257a50cf4_Moonriver_0x97337a9710beb17b8d77ca9175defba5e9afe62e
Gnosis_0xb58f5110855fbef7a715d325d60543e7d4c18143_Fuse Mainnet_0xffd57b46bd670b0461c7c3ebbaedc4cdb7c4fb80
Optimism_0x2297aebd383787a160dd0d9f71508148769342e3_Arbitrum_0x2297aebd383787a160dd0d9f71508148769342e3
Celo Mainnet_0xe33519c400b8f040e73aeda2f45dfdd4634a7ca0_Fuse Mainnet_0xffd57b46bd670b0461c7c3ebbaedc4cdb7c4fb80
Celo Mainnet_0x83017335bae4837016311bdb75df5a320b54d636_Fuse Mainnet_0x811bcf49225ffe8039989a30cf5c03f60660753d
BNB Chain_0x128aedc7f41ffb82131215e1722d8366faad0cd4_Harmony_0x7ffd57563ef54c464f23b5497dd1f54481e4c008
Moonriver_0x97337a9710beb17b8d77ca9175defba5e9afe62e_Kava_0x04866796aabb6b58e6bc4d91a2ae99105b2c58ae
Harmony_0x222228060e7efbb1d78bb5d454581910e3922222_Moonbeam_0x222228060e7efbb1d78bb5d454581910e3922222
Polygon_0x222228060e7efbb1d78bb5d454581910e3922222_Celo Mainnet_0x222228060e7efbb1d78bb5d454581910e3922222
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944
Polygon_0x222228060e7efbb1d78bb5d454581910e3922222_Harmony_0x222228060e7efbb1d78bb5d454581910e3922222
Celo Mainnet_0xc20a842e1fc2681920c1a190552a2f13c46e7fcf_Fuse Mainnet_0xf6b88c4a86965170dd42dbb8b53e790b3490b912
Polygon_0xa184998ec58dc1da77a1f9f1e361541257a50cf4_Gnosis_0xb58f5110855fbef7a715d325d60543e7d4c18143

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
