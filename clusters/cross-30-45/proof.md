# Addresses

see address.csv file

# Number of addresses in this cluster

45

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

polygon

**Funder Address**

0x56a9108a50940f3471fabec573dcc4d030421d80

**Number of addresses involved on chain polygon**

35

**Transactions executing fund transfer**

https://polygonscan.com/tx/0x10c3232f3a93c7a52c391887a2dea1968e986c55226ab59e01279eb6fd2b6bb3



---

**Chain**

fantom

**Funder Address**

0x56a9108a50940f3471fabec573dcc4d030421d80

**Number of addresses involved on chain fantom**

45

**Transactions executing fund transfer**

https://ftmscan.com/tx/0x14a6e80ed76e9d8efb94853fd2b07e85ec7defca1132f74971eaca8249bb05d0



# Observed GCTS

23 common PSDs observed:

Core Blockchain Mainnet_0x3701c5897710f16f1f75c6eae258bf11ee189a5d_Polygon_0xffdf4fe05899c4bdb1676e958fa9f21c19ecb9d5
BNB Chain_0x3668c325501322ceb5a624e95b9e16a019cdebe8_Polygon_0xffdf4fe05899c4bdb1676e958fa9f21c19ecb9d5
Polygon_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4_Astar_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4
Optimism_0xd7ba4057f43a7c4d4a34634b2a3151a60bf78f0d_0xb5691e49f86cba649c815ee633679944b044bc43
Polygon_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4_Moonbeam_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4
Celo Mainnet_0xe47b0a5f2444f9b360bd18b744b8d511cfbf98c6_Polygon_0xffdf4fe05899c4bdb1676e958fa9f21c19ecb9d5
BNB Chain_0xf0295a8cad5f287cc52b6f5994fe4aa6fb6e8d4b_Polygon_0x21d89f9d7304813dfc716141d31ec4125685e71e
Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944_Fantom_0x45a01e4e04f14f7a4a6702c74187c5f6222033cd
Fantom_0x45a01e4e04f14f7a4a6702c74187c5f6222033cd_Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944
Polygon_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4_Harmony_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4
Polygon_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4
Polygon_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4_Merit Circle_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4
Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944_BNB Chain_0x6694340fc020c5e6b96567843da2df01b2ce1eb6
Polygon_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4_Moonriver_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4
Polygon_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4_Celo Mainnet_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4
Polygon_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4_Gnosis_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4
Polygon_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4_Klaytn Mainnet Cypress_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4
Polygon_0xffdf4fe05899c4bdb1676e958fa9f21c19ecb9d5_Celo Mainnet_0xe47b0a5f2444f9b360bd18b744b8d511cfbf98c6
Polygon_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4_Fuse Mainnet_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4
Polygon_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4_Kava_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4
Polygon_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4_Viction_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4
BNB Chain_0x3668c325501322ceb5a624e95b9e16a019cdebe8_Mantle_0x5e6d2a7aa45277ca3037feba4a30cbb8f8cad3b9
Polygon_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4_Core Blockchain Mainnet_0xbf94ed69281709958c8f60bc15cd1bb6badcd4a4

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
