# Addresses

see address.csv file

# Number of addresses in this cluster

488

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

0x0a80673947327cdcc9807681323a003db8addaa5

**Number of addresses involved on chain arb**

199

**Transactions executing fund transfer**

https://arbiscan.io/tx/0x8a39c2f8d34a054c5d56d677609b4f4b735c36d2c4d10fefb4cf95cc3688d3d7



---

**Chain**

arb

**Funder Address**

0x8e2c205ef5335d3f8b05ba81ebf9b1148d89dab6

**Number of addresses involved on chain arb**

488

**Transactions executing fund transfer**

https://arbiscan.io/tx/0x2bec4a998cf48ca9826adaa681f44de1616c23e62e5183c7dd9cf13e25581710



---

**Chain**

op

**Funder Address**

0xf3a65f971ef962952fb0bd3a1141f16bfac6b5ac

**Number of addresses involved on chain op**

67

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0xba30ebdad193faa1fe2d2fa490632d4fa618197086ac0b062cd57a5eff608f6e



---

**Chain**

op

**Funder Address**

0x8e2c205ef5335d3f8b05ba81ebf9b1148d89dab6

**Number of addresses involved on chain op**

99

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0x6cc3dc69aa951eec4f75d3d91f177f3931e1e9b807f8d77ee83d34b41dfd8e96



# Observed GCTS

1 common PSDs observed:

Arbitrum_0xdd69db25f6d620a7bad3023c5d32761d353d3de9_Goerli_0x4f7a67464b5976d7547c860109e4432d50afb38e

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
