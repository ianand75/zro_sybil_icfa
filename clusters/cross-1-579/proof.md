# Addresses

see address.csv file

# Number of addresses in this cluster

579

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

fantom

**Funder Address**

0xd01e00c9d42727da5d92968766245d9e0a2d2e0d

**Number of addresses involved on chain fantom**

579

**Transactions executing fund transfer**

https://ftmscan.com/tx/0x20765bb9c7612484340f5c94dd1f3327b8d2d51907e15ebccebd1bcc3e79a96c
https://ftmscan.com/tx/0xf417eb3f7f0ee8252a7323d7762a33bd9a7a6baed8b695da33388763c7a3c3a6
https://ftmscan.com/tx/0x5fbee56e388d8e659fc16829ce53be26eef81ca22c2fd1b6aa07c868e29032be
https://ftmscan.com/tx/0x60ec2de07dd7bd502e8e0c0f957179a101fd4967f9316fba8522c31e1f14dec5



---

**Chain**

op

**Funder Address**

0xa9c1dbbccd8d51ef1de5cc5f86ccfd15b17766bb

**Number of addresses involved on chain op**

579

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0x885e1cff0d5c4a4e84d4eca20a3f61e5b1abd4766350406ecab1a8cfc059a070
https://optimistic.etherscan.io/tx/0x213751583c126c4bab6d05dfd622f5393abb9bd0251325b3611861f69b38a477



---

**Chain**

polygon

**Funder Address**

0x2f47b8b5c581c0f3393352106b07f09215add04f

**Number of addresses involved on chain polygon**

579

**Transactions executing fund transfer**

https://polygonscan.com/tx/0xbc839b303f8de30c47cc8fd309af2f2fdd17a380f6d5d9bafa855aacaab51ad2
https://polygonscan.com/tx/0x20473a65dc984a4d952c72461ef5e1acf2660376c9a44b6ba7782cb1f2ddf6ee



---

**Chain**

arb

**Funder Address**

0x9519e01b9ff301e05d93141b89992de6b2edcdfb

**Number of addresses involved on chain arb**

579

**Transactions executing fund transfer**

https://arbiscan.io/tx/0x3756c50c9f8300b7a07c10d1bd1c0e093341434fbfc8751383cd380db69259ac



# Observed GCTS

1 common PSDs observed:

Polygon_0x803305930c1bbae396d03f496a7bf53ad7fd4303_Avalanche_0x803305930c1bbae396d03f496a7bf53ad7fd4303

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
