# Addresses

See address.csv

# Number of addresses in this cluster

58

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

0x702b3101c34fe690fe94891a15cf2668b726013f

# Transactions that executed the fund transfer

https://polygonscan.com/tx/0x4584ab2796f527017afd3d39dacaa65e29b7bfa1209778c4570936cc2fa9aa52

# Observed GCTS

14 common PSDs observed:

BNB Chain_0x128aedc7f41ffb82131215e1722d8366faad0cd4_Harmony_0x7ffd57563ef54c464f23b5497dd1f54481e4c008
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883
Gnosis_0x556f119c7433b2232294fb3de267747745a1dab4_Fuse Mainnet_0xf6b88c4a86965170dd42dbb8b53e790b3490b912
Polygon_0x0e1f20075c90ab31fc2dd91e536e6990262cf76d_Celo Mainnet_0xc20a842e1fc2681920c1a190552a2f13c46e7fcf
Polygon_0x222228060e7efbb1d78bb5d454581910e3922222_Celo Mainnet_0x222228060e7efbb1d78bb5d454581910e3922222
Polygon_0x523d5581a0bb8bb2bc9f23b5202894e31124ea3e_Celo Mainnet_0x83017335bae4837016311bdb75df5a320b54d636
Gnosis_0xb58f5110855fbef7a715d325d60543e7d4c18143_Fuse Mainnet_0xffd57b46bd670b0461c7c3ebbaedc4cdb7c4fb80
Celo Mainnet_0xc20a842e1fc2681920c1a190552a2f13c46e7fcf_Fuse Mainnet_0xf6b88c4a86965170dd42dbb8b53e790b3490b912
Polygon_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944_Avalanche_0x9d1b1669c73b033dfe47ae5a0164ab96df25b944
Gnosis_0xe266eedb13a69af15c1756a241021905b1827f6a_Fuse Mainnet_0x811bcf49225ffe8039989a30cf5c03f60660753d
Optimism_0x777c19834a1a2ff6353a1e9cfb7c799ed7943a11_Polygon_0x777c19834a1a2ff6353a1e9cfb7c799ed7943a11
Celo Mainnet_0x83017335bae4837016311bdb75df5a320b54d636_Fuse Mainnet_0x811bcf49225ffe8039989a30cf5c03f60660753d
Polygon_0xa184998ec58dc1da77a1f9f1e361541257a50cf4_Gnosis_0xb58f5110855fbef7a715d325d60543e7d4c18143
Celo Mainnet_0xe33519c400b8f040e73aeda2f45dfdd4634a7ca0_Fuse Mainnet_0xffd57b46bd670b0461c7c3ebbaedc4cdb7c4fb80

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
