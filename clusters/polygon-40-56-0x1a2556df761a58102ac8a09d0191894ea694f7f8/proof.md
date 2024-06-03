# Addresses

See address.csv

# Number of addresses in this cluster

56

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

0x1a2556df761a58102ac8a09d0191894ea694f7f8

# Transactions that executed the fund transfer

https://polygonscan.com/tx/0xc08db40ed3529f32d6297adb259df212d6e1a8c8dd789361916b052119cf1625

# Observed GCTS

8 common PSDs observed:

BNB Chain_0x3668c325501322ceb5a624e95b9e16a019cdebe8_Celo Mainnet_0xe47b0a5f2444f9b360bd18b744b8d511cfbf98c6
Polygon_0x92529365fadd3994cdba8da3c8119a30cae14d2c_Arbitrum Nova_0x38eb79184b11f9464b0baa7681d03775c1c63981
Polygon_0xffdf4fe05899c4bdb1676e958fa9f21c19ecb9d5_Mantle_0x5e6d2a7aa45277ca3037feba4a30cbb8f8cad3b9
Celo Mainnet_0xe47b0a5f2444f9b360bd18b744b8d511cfbf98c6_Polygon_0xffdf4fe05899c4bdb1676e958fa9f21c19ecb9d5
BNB Chain_0x3668c325501322ceb5a624e95b9e16a019cdebe8_Polygon_0xffdf4fe05899c4bdb1676e958fa9f21c19ecb9d5
Core Blockchain Mainnet_0x3701c5897710f16f1f75c6eae258bf11ee189a5d_Polygon_0xffdf4fe05899c4bdb1676e958fa9f21c19ecb9d5
Polygon_0xffdf4fe05899c4bdb1676e958fa9f21c19ecb9d5_Core Blockchain Mainnet_0x3701c5897710f16f1f75c6eae258bf11ee189a5d
Polygon_0xffdf4fe05899c4bdb1676e958fa9f21c19ecb9d5_Celo Mainnet_0xe47b0a5f2444f9b360bd18b744b8d511cfbf98c6

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
