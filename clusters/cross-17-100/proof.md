# Addresses

see address.csv file

# Number of addresses in this cluster

100

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

0x06723e75e4c05e7a7b40e3b84c0d2ce95aa2edce

**Number of addresses involved on chain fantom**

100

**Transactions executing fund transfer**

https://ftmscan.com/tx/0x4c26d5f136168663cc60aea4c766828769e751fa926ed00da6eebe705db71343
https://ftmscan.com/tx/0x6732f2ada6264908512408dbdada2744c90f27c6dc6400781ef60288d87aa195



---

**Chain**

arb

**Funder Address**

0x06723e75e4c05e7a7b40e3b84c0d2ce95aa2edce

**Number of addresses involved on chain arb**

100

**Transactions executing fund transfer**

https://arbiscan.io/tx/0xa28bf35a6aaece5cfbf437cf3dd1edf6fd715de843f7d79bfdd5b39383197ea4



---

**Chain**

polygon

**Funder Address**

0x06723e75e4c05e7a7b40e3b84c0d2ce95aa2edce

**Number of addresses involved on chain polygon**

100

**Transactions executing fund transfer**

https://polygonscan.com/tx/0x0fb30fa9b2d2e9f4fc7ba5161bc68e5461d5aa40c1ad530c49adae927cfaa8b9
https://polygonscan.com/tx/0xe2285be9847a747eb9293debfa15adfbdf6eecef9761342c26977333963133e7



---

**Chain**

op

**Funder Address**

0x06723e75e4c05e7a7b40e3b84c0d2ce95aa2edce

**Number of addresses involved on chain op**

100

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0xdbfe88168365864bf878852d3b1ce112ffaf6ee56bb6a90bee43ed2abbc3cb27



# Observed GCTS

19 common PSDs observed:

Polygon_0xe9e30a0ad0d8af5cf2606ea720052e28d6fcbaaf_Avalanche_0xe9e30a0ad0d8af5cf2606ea720052e28d6fcbaaf
BNB Chain_0x128aedc7f41ffb82131215e1722d8366faad0cd4_Harmony_0x7ffd57563ef54c464f23b5497dd1f54481e4c008
Polygon_0x0e1f20075c90ab31fc2dd91e536e6990262cf76d_Kava_0x4c24ba5177365b4c0ebae62b31945d830a858673
Polygon_0x0e1f20075c90ab31fc2dd91e536e6990262cf76d_Moonriver_0xd379c3d0930d70022b3c6eba8217e4b990705540
Arbitrum_0x1bacc2205312534375c8d1801c27d28370656cff_0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa
Moonbeam_0x671861008497782f7108d908d4df18ebf9598b82_Celo Mainnet_0xc20a842e1fc2681920c1a190552a2f13c46e7fcf
Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944_Fantom_0x45a01e4e04f14f7a4a6702c74187c5f6222033cd
Fantom_0x45a01e4e04f14f7a4a6702c74187c5f6222033cd_Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944
Celo Mainnet_0xc20a842e1fc2681920c1a190552a2f13c46e7fcf_Fuse Mainnet_0xf6b88c4a86965170dd42dbb8b53e790b3490b912
Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944_Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883
Polygon_0x0e1f20075c90ab31fc2dd91e536e6990262cf76d_Moonbeam_0x671861008497782f7108d908d4df18ebf9598b82
Metis_0x45f1a95a4d3f3836523f5c83673c797f4d4d263b_BNB Chain_0x6694340fc020c5e6b96567843da2df01b2ce1eb6
Fantom_0x45a01e4e04f14f7a4a6702c74187c5f6222033cd_Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883
Polygon_0x523d5581a0bb8bb2bc9f23b5202894e31124ea3e_Celo Mainnet_0x83017335bae4837016311bdb75df5a320b54d636
Polygon_0x0e1f20075c90ab31fc2dd91e536e6990262cf76d_Celo Mainnet_0xc20a842e1fc2681920c1a190552a2f13c46e7fcf
Kava_0x4c24ba5177365b4c0ebae62b31945d830a858673_Arbitrum Nova_0xb6789dacf323d60f650628dc1da344d502bc41e3
Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883_Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944
Arbitrum_0x2297aebd383787a160dd0d9f71508148769342e3_Optimism_0x2297aebd383787a160dd0d9f71508148769342e3
BNB Chain_0x6694340fc020c5e6b96567843da2df01b2ce1eb6_Metis_0x45f1a95a4d3f3836523f5c83673c797f4d4d263b

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
