# Addresses

see address.csv file

# Number of addresses in this cluster

401

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

0x75da953c58b68d35b0a3bd54b64cce9697e955f1

**Number of addresses involved on chain polygon**

401

**Transactions executing fund transfer**

https://polygonscan.com/tx/0x7733c6e3e2b842540e59efb10f1466d60c87d209c3e15644f1902328305c6d60
https://polygonscan.com/tx/0x4648ced448d2c543b5c6f8b94402aba25d82a235a4619b70a92e15270165cb15
https://polygonscan.com/tx/0x5e3cad448916aceeafc893a623d6669037f1ee6d72c9acf2f5574f6d5bda2e6f



---

**Chain**

moonriver

**Funder Address**

0x1193a4f3acb05876ab96de7468dbc7db91985574

**Number of addresses involved on chain moonriver**

401

**Transactions executing fund transfer**

https://moonriver.moonscan.io/tx/0xc4a47a9850e11ce2ebf9e71eddf5e4d2a8661f4c42601f94a97257199db0e4c4
https://moonriver.moonscan.io/tx/0xdfe1108bad7b695488abf4371c0738a688f0af56f92fd7a871b4c71e83b9cdce
https://moonriver.moonscan.io/tx/0xe838ba3132fba62bb514a20ca368632a7546e2a2e26872dafd5eec98f8c8c27d



---

**Chain**

arb

**Funder Address**

0x75da953c58b68d35b0a3bd54b64cce9697e955f1

**Number of addresses involved on chain arb**

401

**Transactions executing fund transfer**

https://arbiscan.io/tx/0xdcc7aa2a4f94712ba438ba8842631381dfe53f265da3bfb1130ba2c32e1298a0



# Observed GCTS

12 common PSDs observed:

Polygon_0x0c1ebbb61374da1a8c57cb6681bf27178360d36f_Celo Mainnet_0xf1ddcaca7d17f8030ab2eb54f2d9811365efe123
BNB Chain_0x52e75d318cfb31f9a2edfa2dfee26b161255b233_Core Blockchain Mainnet_0xa4218e1f39da4aadac971066458db56e901bcbde
Base_0x6bf98654205b1ac38645880ae20fc00b0bb9ffca_Zora_0x461fccf240ca4884cc5413a5742f1bc56faf7a0c
Polygon_0x6f484eacd997d9880205af22f6a4881ea0e1ccd7_Avalanche_0x6f484eacd997d9880205af22f6a4881ea0e1ccd7
Base_0xfb7ef0bbd8bfb5f129f995fbc34f4d786ccc63cf_Fuse Mainnet_0xfb7ef0bbd8bfb5f129f995fbc34f4d786ccc63cf
Moonriver_0xd379c3d0930d70022b3c6eba8217e4b990705540_Kava_0x4c24ba5177365b4c0ebae62b31945d830a858673
BNB Chain_0x128aedc7f41ffb82131215e1722d8366faad0cd4_Harmony_0x7ffd57563ef54c464f23b5497dd1f54481e4c008
Moonbeam_0x671861008497782f7108d908d4df18ebf9598b82_DFK_0x457fd60ffa26576e226252092c98921f12e90fbb
Polygon_0x0c1ebbb61374da1a8c57cb6681bf27178360d36f_Gnosis_0xfa5ed56a203466cbbc2430a43c66b9d8723528e7
Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944_Avalanche_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944
Fantom_0xc5c01568a3b5d8c203964049615401aaf0783191_Moonriver_0xef2dbdfec54c466f7ff92c9c5c75abb6794f0195
Polygon_0x0e1f20075c90ab31fc2dd91e536e6990262cf76d_DFK_0x457fd60ffa26576e226252092c98921f12e90fbb

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
