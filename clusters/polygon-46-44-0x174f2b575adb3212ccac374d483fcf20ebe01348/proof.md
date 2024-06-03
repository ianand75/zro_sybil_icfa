# Addresses

See address.csv

# Number of addresses in this cluster

44

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

Polygon Mainnet

# Funder address

0x174f2b575adb3212ccac374d483fcf20ebe01348

# Transactions that executed the fund transfer

https://polygonscan.com/tx/0xd06531317cbd05fb937e1c26002d2c988ba4328c0c91cd7add8eae7f69a5e9ef

# Observed GCTS

8 common PSDs observed:

Gnosis_0x222228060e7efbb1d78bb5d454581910e3922222_Celo Mainnet_0x222228060e7efbb1d78bb5d454581910e3922222
Polygon_0x222228060e7efbb1d78bb5d454581910e3922222_Arbitrum Nova_0x222228060e7efbb1d78bb5d454581910e3922222
Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944_Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944
Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883_BNB Chain_0x6694340fc020c5e6b96567843da2df01b2ce1eb6
Avalanche_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944_Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd
Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944_Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd
Arbitrum_0x2297aebd383787a160dd0d9f71508148769342e3_Avalanche_0x2297aebd383787a160dd0d9f71508148769342e3

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
