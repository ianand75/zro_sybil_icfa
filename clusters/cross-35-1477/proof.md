# Addresses

see address.csv file

# Number of addresses in this cluster

1477

# Reasoning

This cluster, funded by **Indirect Common Funder**, employs smart contracts to obscure the from-to relationship of fund transfers. It contains over 20 addresses sourced from the snapshot database, none of which are initially labeled. The funder address originates from a non-CEX source. Notably, batch funding activities on this cluster has been observed across multiple chains, as listed below. These factors strongly suggest the cluster's potential for being a sybil, controlled and financed by a single entity.

---

**Chain**

op

**Funder Address**

0x568d6b6f45f034a6736abbf2f7c3cf15e36f7ae8

**Number of addresses involved on chain op**

1422

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0x05086f2253e744a9ca6dedcce675399525503d7cc18cb98ce57157d17c046adf
https://optimistic.etherscan.io/tx/0x93ee393848657813cbd930836451f23cb98b84ba9cfa60dde28e80792658103e
https://optimistic.etherscan.io/tx/0xef2076b479c46f0915b6df8dc1b42d4fd0145f62f63a822fbc9239daae3890aa
https://optimistic.etherscan.io/tx/0x420b489390fb70b71cea47eea31890747cab55a7ad5471d6b9e46e709ab5f535
https://optimistic.etherscan.io/tx/0x13fd9dfde1df116ed97ef661d7dc98107ce3592bd3d6aad7b3c34d4f3741e8f6

---

**Chain**

arb

**Funder Address**

0x568d6b6f45f034a6736abbf2f7c3cf15e36f7ae8

**Number of addresses involved on chain arb**

1009

**Transactions executing fund transfer**

https://arbiscan.io/tx/0x6b08cc95bb6330078e1d6fa82ab573b15ca9147405abfc755c4023842e911721
https://arbiscan.io/tx/0xe9ad3d72c7ef7f9feea7ef6b2437d2ef0b807cd3538785b0c35c382465adb650
https://arbiscan.io/tx/0x12b3a882c4318a4e2d23a43a36f8c3b42227ff657a7c0c4a83c42187a024d08d

---

**Chain**

polygon

**Funder Address**

0x568d6b6f45f034a6736abbf2f7c3cf15e36f7ae8

**Number of addresses involved on chain polygon**

1211

**Transactions executing fund transfer**

https://polygonscan.com/tx/0xe5ca6028fb78999d759dc2f4b84a1b47d46635f7d5964c8aa43b15034956cfcc
https://polygonscan.com/tx/0x49f92f12b52e75edd625f879db8faee39db297b33636404277ab3c4f2d9b7bc7
https://polygonscan.com/tx/0x8be14ee06172b75bb5bcdbbc6232f9895e6ab7c2622fb87d74b66a0300ae84bd
https://polygonscan.com/tx/0xe0774c342e74221ccb3dcdfded2d4d1f6af6a75ec4e1c145d8876cd200d04674

# Cross-chain activity overlap outline

                       954
          arb(1009) ----------  op(1422)
                \               /
                 \  937        /  1210
                  \           /
                  polygon(1211)


    A node represents cluster found on chain 'xxx' with it's size. An edge and its weight represents number of address overlap between two chains.
