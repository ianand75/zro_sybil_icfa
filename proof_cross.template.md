# Addresses

see address.csv file

# Number of addresses in this cluster

${count}

# Reasoning

This cluster, funded by **Indirect Common Funder**, employs smart contracts to obscure the from-to relationship of fund transfers. It contains over 20 addresses sourced from the snapshot database, none of which are initially labeled. The funder address originates from a non-CEX source. Notably, batch funding activities on this cluster has been observed across multiple chains, as listed below. These factors strongly suggest the cluster's potential for being a sybil, controlled and financed by a single entity.

% for p in proofs:

---

**Chain**

${p["chain"]}

**Funder Address**

${p["funder"]}

**Number of addresses involved on chain ${p["chain"]}**

${p["count"]}

**Transactions executing fund transfer**
${p["tx"]}

% endfor
