# Addresses

See address.csv

# Number of addresses in this cluster

34

# Reasoning

This cluster is funded by an Indirect Common Funder who uses a smart contract to transfer funds to this cluster to obscure the from-to relationship.

- The number of addresses in this cluster is larger than 20.
- Each address is from the snapshot database and not already labeled.
- The funder address is not from a centralized exchange (CEX).
- cluster addresses are behaviorally not independent.

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

# Chain

Polygon Mainnet

# Funder address

0x4111e3e3a2c668b6975934525a59d7b5895f07a2

# Transactions that executed the fund transfer

https://polygonscan.com/tx/0x01f2d9a2e41223ce2b15163a8556792303ff5e6a644e7ccc2e3762415373b479

# Observed GCTS

13 common PSDs observed:

BNB Chain_0xe4587891fe7547efc26a7f1f124c0d7db4c9ad9b_Arbitrum_0xe4587891fe7547efc26a7f1f124c0d7db4c9ad9b
Avalanche_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944_Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_BNB Chain_0x6694340fc020c5e6b96567843da2df01b2ce1eb6
Arbitrum_0x6694340fc020c5e6b96567843da2df01b2ce1eb6_BNB Chain_0xb0d502e938ed5f4df2e681fe6e419ff29631d62b
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Avalanche_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883
BNB Chain_0x6694340fc020c5e6b96567843da2df01b2ce1eb6_Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd
Arbitrum_0x3082cc23568ea640225c2467653db90e9250aaa0_BNB Chain_0xf7de7e8a6bd59ed41a4b5fe50278b3b7f31384df
Fantom_0x45a01e4e04f14f7a4a6702c74187c5f6222033cd_Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944
Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883_Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd
Arbitrum_0x1bacc2205312534375c8d1801c27d28370656cff_0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa
BNB Chain_0xf7de7e8a6bd59ed41a4b5fe50278b3b7f31384df_Arbitrum_0x3082cc23568ea640225c2467653db90e9250aaa0

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
