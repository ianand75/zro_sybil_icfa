# Addresses

see address.csv file

# Number of addresses in this cluster

1477

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

0x568d6b6f45f034a6736abbf2f7c3cf15e36f7ae8

**Number of addresses involved on chain polygon**

1211

**Transactions executing fund transfer**

https://polygonscan.com/tx/0xe5ca6028fb78999d759dc2f4b84a1b47d46635f7d5964c8aa43b15034956cfcc
https://polygonscan.com/tx/0x49f92f12b52e75edd625f879db8faee39db297b33636404277ab3c4f2d9b7bc7
https://polygonscan.com/tx/0x8be14ee06172b75bb5bcdbbc6232f9895e6ab7c2622fb87d74b66a0300ae84bd
https://polygonscan.com/tx/0xe0774c342e74221ccb3dcdfded2d4d1f6af6a75ec4e1c145d8876cd200d04674

---

**Chain**

op

**Funder Address**

0x568d6b6f45f034a6736abbf2f7c3cf15e36f7ae8

**Number of addresses involved on chain op**

1422

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0x05086f2253e744a9ca6dedcce675399525503d7cc18cb98ce57157d17c046adf
https://optimistic.etherscan.io/tx/0x93ee393848657813cbd930836451f23cb98b84ba9cfa60dde28e80792658103e
https://optimistic.etherscan.io/tx/0xef2076b479c46f0915b6df8dc1b42d4fd0145f62f63a822fbc9239daae3890aa
https://optimistic.etherscan.io/tx/0x420b489390fb70b71cea47eea31890747cab55a7ad5471d6b9e46e709ab5f535
https://optimistic.etherscan.io/tx/0x13fd9dfde1df116ed97ef661d7dc98107ce3592bd3d6aad7b3c34d4f3741e8f6

---

**Chain**

arb

**Funder Address**

0x568d6b6f45f034a6736abbf2f7c3cf15e36f7ae8

**Number of addresses involved on chain arb**

1009

**Transactions executing fund transfer**

https://arbiscan.io/tx/0x6b08cc95bb6330078e1d6fa82ab573b15ca9147405abfc755c4023842e911721
https://arbiscan.io/tx/0xe9ad3d72c7ef7f9feea7ef6b2437d2ef0b807cd3538785b0c35c382465adb650
https://arbiscan.io/tx/0x12b3a882c4318a4e2d23a43a36f8c3b42227ff657a7c0c4a83c42187a024d08d

# Cross-chain activity overlap outline

                       954
          arb(1009) ----------  op(1422)
                \               /
                 \  937        /  1210
                  \           /
                  polygon(1211)


    A node represents cluster found on chain 'xxx' with it's size. An edge and its weight represents number of address overlap between two chains.

# Observed GCTS

1 common PSDs observed:

Arbitrum_0x1bacc2205312534375c8d1801c27d28370656cff_0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
