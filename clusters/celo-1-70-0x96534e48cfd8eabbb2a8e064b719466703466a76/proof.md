# Addresses

See address.csv

# Number of addresses in this cluster

70

# Reasoning

This cluster is funded by an Indirect Common Funder who uses a smart contract to transfer funds to this cluster to obscure the from-to relationship.

- The number of addresses in this cluster is larger than 20.
- Each address is from the snapshot database and not already labeled.
- The funder address is not from a centralized exchange (CEX).
- cluster addresses are behaviorally not independent.

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

# Chain

Celo Mainnet

# Funder address

0x96534e48cfd8eabbb2a8e064b719466703466a76

# Transactions that executed the fund transfer

https://celoscan.io/tx/0x80c2cdb9f4a3c9a8ef1ff1f5e8724b845edf00e09bdd7cf68319b83449ae6831

# Observed GCTS

12 common PSDs observed:

BNB Chain_0xe9f183fc656656f1f17af1f2b0df79b8ff9ad8ed_Gnosis_0xfa5ed56a203466cbbc2430a43c66b9d8723528e7
BNB Chain_0xe9f183fc656656f1f17af1f2b0df79b8ff9ad8ed_Celo Mainnet_0xf1ddcaca7d17f8030ab2eb54f2d9811365efe123
Celo Mainnet_0xf1ddcaca7d17f8030ab2eb54f2d9811365efe123_Gnosis_0xfa5ed56a203466cbbc2430a43c66b9d8723528e7
Arbitrum_0x1bacc2205312534375c8d1801c27d28370656cff_0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa
BNB Chain_0x3668c325501322ceb5a624e95b9e16a019cdebe8_Mantle_0x5e6d2a7aa45277ca3037feba4a30cbb8f8cad3b9
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Base_0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398
BNB Chain_0x6694340fc020c5e6b96567843da2df01b2ce1eb6_Metis_0x45f1a95a4d3f3836523f5c83673c797f4d4d263b
BNB Chain_0x52e75d318cfb31f9a2edfa2dfee26b161255b233_Core Blockchain Mainnet_0xa4218e1f39da4aadac971066458db56e901bcbde
BNB Chain_0x6694340fc020c5e6b96567843da2df01b2ce1eb6_Fantom_0x45a01e4e04f14f7a4a6702c74187c5f6222033cd
Core Blockchain Mainnet_0xa4218e1f39da4aadac971066458db56e901bcbde_BNB Chain_0x52e75d318cfb31f9a2edfa2dfee26b161255b233
BNB Chain_0x6694340fc020c5e6b96567843da2df01b2ce1eb6_Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
