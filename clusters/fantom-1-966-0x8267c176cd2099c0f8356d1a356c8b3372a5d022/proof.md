# Addresses

See address.csv

# Number of addresses in this cluster

966

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

Fantom

# Funder address

0x8267c176cd2099c0f8356d1a356c8b3372a5d022

# Transactions that executed the fund transfer

https://ftmscan.com/tx/0xec22f50022647150b58a8967b03b2159d89a9690d0caf95cf03b18824e9e5166
https://ftmscan.com/tx/0xed63ae960c9a062b743a5936c3aaa3b6787b88d3b389bd643f6ee887abb32f3e
https://ftmscan.com/tx/0x0961733d89b813ac3dec077db13a34e8ee1d78cc08391b0bc23dcd953f946995

# Observed GCTS

14 common PSDs observed:

Polygon_0x70ea00ab512d13dac5001c968f8d2263d179e2d2_Core Blockchain Mainnet_0xc7cc66a88e2f121fb104344eacb7ba7bcae79dfa
BNB Chain_0xb0d502e938ed5f4df2e681fe6e419ff29631d62b_Avalanche_0x2f6f07cdcf3588944bf4c42ac74ff24bf56e7590
Polygon_0x70ea00ab512d13dac5001c968f8d2263d179e2d2_Mantle_0x5f45cd59ba7f2f6bcd935663f68ee1debe3b8a10
Polygon_0x70ea00ab512d13dac5001c968f8d2263d179e2d2_Kava_0x921b486cc33580af7d8208df1619383470d5dcbe
Polygon_0x70ea00ab512d13dac5001c968f8d2263d179e2d2_Tenet_0x021b4878be1ce222e5d1625ed7dbcb7cd80cf245
Polygon_0x70ea00ab512d13dac5001c968f8d2263d179e2d2_Meter Mainnet_0x1aaac4484402c026b30d3d4272e99679664a18fc
Avalanche_0x2f6f07cdcf3588944bf4c42ac74ff24bf56e7590_BNB Chain_0xb0d502e938ed5f4df2e681fe6e419ff29631d62b
Celo Mainnet_0xf1ddcaca7d17f8030ab2eb54f2d9811365efe123_Gnosis_0xfa5ed56a203466cbbc2430a43c66b9d8723528e7
Fantom_0xa07f2e99eaa338acf66337baf99551bdcfd3ab00_DFK_0xdb3bb6d5a8eeeafc64c66c176900e6b82b23dd5f
Gnosis_0xfa5ed56a203466cbbc2430a43c66b9d8723528e7_Celo Mainnet_0xf1ddcaca7d17f8030ab2eb54f2d9811365efe123
Polygon_0x70ea00ab512d13dac5001c968f8d2263d179e2d2_Arbitrum Nova_0x148caf6ffbaba15f35dee7e2813d1f4c6da288f3
Polygon_0x70ea00ab512d13dac5001c968f8d2263d179e2d2_Canto_0x0e2cfd13566578ead8296e8b1813619c4fbc5edc
Fantom_0xa07f2e99eaa338acf66337baf99551bdcfd3ab00_Arbitrum Nova_0x148caf6ffbaba15f35dee7e2813d1f4c6da288f3
Polygon_0x70ea00ab512d13dac5001c968f8d2263d179e2d2_Moonriver_0x8582a8f68faf6c2c5b5f4a1eb28122acf09fefee

Therefore this cluster is highly suspected of being a sybil, as it is funded and controlled by a single entity.
