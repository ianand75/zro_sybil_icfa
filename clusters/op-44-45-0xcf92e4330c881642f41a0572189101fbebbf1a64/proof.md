# Addresses

See address.csv

# Number of addresses in this cluster

45

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

OP Mainnet

# Funder address

0xcf92e4330c881642f41a0572189101fbebbf1a64

# Transactions that executed the fund transfer

https://optimistic.etherscan.io/tx/0x6daaead39daf90b80337236700e3b2cb1188d759047a91de59ce094597c121ea

# Observed GCTS

17 common PSDs observed:

Polygon_0x6f484eacd997d9880205af22f6a4881ea0e1ccd7_Avalanche_0x6f484eacd997d9880205af22f6a4881ea0e1ccd7
Base_0x7969414aa6958a44e276e9c3c5f28c5bc42e0271_Zora_0x7969414aa6958a44e276e9c3c5f28c5bc42e0271
Avalanche_0xb3a66127ccb143bfb01d3aecd3ce9d17381b130d_Optimism_0x48686c24697fe9042531b64d792304e514e74339
Arbitrum_0x173b47edbeca665125edc24c509bfe545cda60a9_Orderly Mainnet_0x173b47edbeca665125edc24c509bfe545cda60a9
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883
Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883_Base_0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398
Polygon_0x0067b3aff7f3c593f4d9ef9d4fcfd2cf993ccbab_Core Blockchain Mainnet_0x3bf50892727b110a88dfc3a7d7e4fc036ef9f8ff
Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883_Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd
Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883_Linea_0x45f1a95a4d3f3836523f5c83673c797f4d4d263b
Optimism_0xdd69db25f6d620a7bad3023c5d32761d353d3de9_Goerli_0x4f7a67464b5976d7547c860109e4432d50afb38e
Zora_0x7969414aa6958a44e276e9c3c5f28c5bc42e0271_Base_0x7969414aa6958a44e276e9c3c5f28c5bc42e0271
Optimism_0x6f484eacd997d9880205af22f6a4881ea0e1ccd7_Polygon_0x6f484eacd997d9880205af22f6a4881ea0e1ccd7
Avalanche_0x2297aebd383787a160dd0d9f71508148769342e3_Polygon_0x2297aebd383787a160dd0d9f71508148769342e3
Polygon_0x777c19834a1a2ff6353a1e9cfb7c799ed7943a11_Avalanche_0x777c19834a1a2ff6353a1e9cfb7c799ed7943a11
BNB Chain_0x52e75d318cfb31f9a2edfa2dfee26b161255b233_Core Blockchain Mainnet_0xa4218e1f39da4aadac971066458db56e901bcbde
Polygon_0x8163a9b0901f63c27471b4d051b7250ecddd362d_Arbitrum Nova_0x3757b9a237ca89aac36029879cf3ace298b3ba65
Polygon_0x803305930c1bbae396d03f496a7bf53ad7fd4303_Avalanche_0x803305930c1bbae396d03f496a7bf53ad7fd4303

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
