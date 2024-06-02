# Addresses

See address.csv

# Number of addresses in this cluster

37

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

Gnosis

# Funder address

0x335f9316c940b8b9fbcc0817eed36183d49a8cdd

# Transactions that executed the fund transfer

https://gnosisscan.io/tx/0x252ef502e22ec88134947d3b6605b569a8f6412099fd9c03042b00646452e316

# Observed GCTS

11 common PSDs observed:

Avalanche_0x2297aebd383787a160dd0d9f71508148769342e3_Optimism_0x2297aebd383787a160dd0d9f71508148769342e3
Optimism_0xd12999440402d30f69e282d45081999412013844_Moonbeam_0x892476d79090fa77c6b9b79f68d21f62b46bedd2
Gnosis_0xfa5ed56a203466cbbc2430a43c66b9d8723528e7_Celo Mainnet_0xf1ddcaca7d17f8030ab2eb54f2d9811365efe123
Celo Mainnet_0xf1ddcaca7d17f8030ab2eb54f2d9811365efe123_Gnosis_0xfa5ed56a203466cbbc2430a43c66b9d8723528e7
Base_0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398_Linea_0x45f1a95a4d3f3836523f5c83673c797f4d4d263b
BNB Chain_0x52e75d318cfb31f9a2edfa2dfee26b161255b233_Core Blockchain Mainnet_0xa4218e1f39da4aadac971066458db56e901bcbde
Optimism_0xd12999440402d30f69e282d45081999412013844_Gnosis_0x402a928dd8342f5604a9a416d00997105c76bfa2
Linea_0x45f1a95a4d3f3836523f5c83673c797f4d4d263b_Base_0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398
Core Blockchain Mainnet_0xa4218e1f39da4aadac971066458db56e901bcbde_BNB Chain_0x52e75d318cfb31f9a2edfa2dfee26b161255b233
Optimism_0xd12999440402d30f69e282d45081999412013844_Arbitrum Nova_0x402a928dd8342f5604a9a416d00997105c76bfa2
Optimism_0x2297aebd383787a160dd0d9f71508148769342e3_Avalanche_0x2297aebd383787a160dd0d9f71508148769342e3

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
