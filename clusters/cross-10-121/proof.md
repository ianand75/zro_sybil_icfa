# Addresses

see address.csv file

# Number of addresses in this cluster

121

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

arb

**Funder Address**

0x6c0e771c9cfbbd3fb7436306bdefe5ba348fb3f1

**Number of addresses involved on chain arb**

49

**Transactions executing fund transfer**

https://arbiscan.io/tx/0x82e1eac5b29920db86c646fe61ad0bb1896a77dee9e3a3041d736f25b7e51200



---

**Chain**

polygon

**Funder Address**

0x6c0e771c9cfbbd3fb7436306bdefe5ba348fb3f1

**Number of addresses involved on chain polygon**

49

**Transactions executing fund transfer**

https://polygonscan.com/tx/0x2895b2703d0b0e0844ce2de4ddecab2a8689b2ce20bbfe95178175851b23bfe4



---

**Chain**

op

**Funder Address**

0x6c0e771c9cfbbd3fb7436306bdefe5ba348fb3f1

**Number of addresses involved on chain op**

49

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0xdaabe4a1c8adda441b9d1b9f9b4f59838a7ff4f9e2495ebbc2a37ef6674ffd89



---

**Chain**

fantom

**Funder Address**

0x2c46af079cf42552339be6e6cc4e7c871ac49afa

**Number of addresses involved on chain fantom**

45

**Transactions executing fund transfer**

https://ftmscan.com/tx/0xb0107b6b1eb7362c937851cb3a4117d35b00d95151bd0adf256f7b6b66cc394c
https://ftmscan.com/tx/0x45c252197b0b815811b8a59c555ec78611feb12ed8d9b9c26a385c996c6aa0f5



---

**Chain**

polygon

**Funder Address**

0x2c46af079cf42552339be6e6cc4e7c871ac49afa

**Number of addresses involved on chain polygon**

72

**Transactions executing fund transfer**

https://polygonscan.com/tx/0xd8f845ad843cc3e509146d11b63efc4935d1cff223fb3dcccc4b822c8e864fd7



---

**Chain**

arb

**Funder Address**

0x3807a4fd8ed467d21c577a833868c4ad03dc21c2

**Number of addresses involved on chain arb**

121

**Transactions executing fund transfer**

https://arbiscan.io/tx/0x30e3ce626d7a4867a4d2f299a08498e46a9ba5e222403961e893ba2a27ab5dbb



---

**Chain**

arb

**Funder Address**

0x183bffe026d50515516a8f873162396068143425

**Number of addresses involved on chain arb**

51

**Transactions executing fund transfer**

https://arbiscan.io/tx/0x175b5e3a643d6f961d5dca42517c3a6662cac8ad991da35dc07ee034deb267aa



---

**Chain**

op

**Funder Address**

0x3a0e1e04aec0c8ded8e7820952e78c680f0ff2c6

**Number of addresses involved on chain op**

71

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0xc6d539886f65ead238a2d6d71f7f31ccbc43f97b8482016b7af02f74c4986f0a



---

**Chain**

op

**Funder Address**

0x970e24aa00befcdf0ad09178312ff450016caf66

**Number of addresses involved on chain op**

49

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0x6d7e5a6b426d44a6bd2d06227840e1d20d091ce11a379a3e5bb361c9ebbaa421



---

**Chain**

fantom

**Funder Address**

0x6c0e771c9cfbbd3fb7436306bdefe5ba348fb3f1

**Number of addresses involved on chain fantom**

49

**Transactions executing fund transfer**

https://ftmscan.com/tx/0x5ccc731d1f1a7d11ea56d6e6b228e71ed9ce95f4b09756b86826130245d408fc
https://ftmscan.com/tx/0xe127e6c4ca013245f71bb35aadabac59f5b919de130d729c5b255d536bb41c02



# Observed GCTS

6 common PSDs observed:

Polygon_0xa184998ec58dc1da77a1f9f1e361541257a50cf4_Celo Mainnet_0xe33519c400b8f040e73aeda2f45dfdd4634a7ca0
Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883_Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd
BNB Chain_0x6694340fc020c5e6b96567843da2df01b2ce1eb6_Metis_0x45f1a95a4d3f3836523f5c83673c797f4d4d263b
BNB Chain_0x128aedc7f41ffb82131215e1722d8366faad0cd4_Harmony_0x7ffd57563ef54c464f23b5497dd1f54481e4c008
Polygon_0x0e1f20075c90ab31fc2dd91e536e6990262cf76d_Gnosis_0x556f119c7433b2232294fb3de267747745a1dab4
Arbitrum_0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd_Optimism_0x701a95707a0290ac8b90b3719e8ee5b210360883

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
