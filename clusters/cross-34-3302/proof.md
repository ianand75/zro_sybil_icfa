# Addresses

see address.csv file

# Number of addresses in this cluster

3302

# Reasoning

This cluster, funded by **Indirect Common Funder**, employs smart contracts to obscure the from-to relationship of fund transfers. It contains over 20 addresses sourced from the snapshot database, none of which are initially labeled. The funder address originates from a non-CEX source. Notably, batch funding activities on this cluster has been observed across multiple chains, as listed below. These factors strongly suggest the cluster's potential for being a sybil, controlled and financed by a single entity.

---

**Chain**

bsc

**Funder Address**

0x770edb43ecc5bcbe6f7088e1049fc42b2d1b195c

**Number of addresses involved on chain bsc**

127

**Transactions executing fund transfer**

https://bscscan.com/tx/0xf1ee7e87010dd4d33d168c83294e9c619bcd8b03473d5e0189b3bd52b68979d7
https://bscscan.com/tx/0x1e2ac9ffe6ed72decd65bd864e41f1bc1ed77f08f878fc09789713fdbd448c15
https://bscscan.com/tx/0x8fa394d8dfa758d9eb057ef57110df09ad91a94d0b81d082dfbc3c83012a16bc

---

**Chain**

polygon

**Funder Address**

0x770edb43ecc5bcbe6f7088e1049fc42b2d1b195c

**Number of addresses involved on chain polygon**

2821

**Transactions executing fund transfer**

https://polygonscan.com/tx/0x1f2a33e8d43660bae9a97116a9a022f181fbf475258e293e7f6b690f065e54b7
https://polygonscan.com/tx/0x7d1a46511d9777fbf9392af60dd8b5d85cd454109cd9ae17a4f520761732d11e
https://polygonscan.com/tx/0xb0ce2bc65feb644a9ba2081afe782fe5384905cf6f82f952e5cbb972c9efc986
https://polygonscan.com/tx/0x98389ffdb94aa35f2df8f8c779beb8ffeb84977ff227c05fc84d3f2ad81e66d1
https://polygonscan.com/tx/0x0831f4410c400574fe08203e42e59d430e301f17434b31c97746934de4bdffbb
https://polygonscan.com/tx/0x27edf90674bbff530665491f0cf27387693e27688963a2551d2e221f6cd5370e
https://polygonscan.com/tx/0xdca9390794166c9d7499b995d2c9dc212e421398a7620593b272c781f4b0afea
https://polygonscan.com/tx/0x003bcb8d85f662353da3506954b52cac4257c43be89f946367aee5db84fca340
https://polygonscan.com/tx/0x714e0bf6c7b443797f837b53c84607acd3b6704d2609329080f9dcdbec7877ff
https://polygonscan.com/tx/0xda0cf65d23e5152dd1e1aa16d3776184777af9179c6e7569475b46f73582ae16

---

**Chain**

arb

**Funder Address**

0x770edb43ecc5bcbe6f7088e1049fc42b2d1b195c

**Number of addresses involved on chain arb**

1584

**Transactions executing fund transfer**

https://arbiscan.io/tx/0x5b06aaacece5489e305bbd685c0dd9ea5374d2fb7a470cb4674e6761ad2ae4a2
https://arbiscan.io/tx/0xde715da84d0909d2f98b58da8f8540b31ec83a62bf6fd45117c549106cb93dda
https://arbiscan.io/tx/0x21acc7c95055c80be04692c4bf33e8e382044865038d11dcbd546860f96f9c99
https://arbiscan.io/tx/0x8b34ed0231aa37f58ab19afdfbffdeb00091aa11b9692b8e4c9444fe5f5efbfe
https://arbiscan.io/tx/0xbc715fa05303dd46cba8640ef910ca4301acf89ab44a4a2ead075525ee0af308
https://arbiscan.io/tx/0xc3a4c90f5b9bb3db5d386cded1fee3e03103284468b4485b5c1a0c9ec56afa07
https://arbiscan.io/tx/0xe028ef665e7fc7b0fe26265826f0bbf16a256aa83aff0f88d4640771dbca1ad0
https://arbiscan.io/tx/0x83fce035904109698b1eccbe0eb31c6c690fecf829fd47c91d92e0178e968494
https://arbiscan.io/tx/0x44b614317d58ccf5b320570e17e1e090e3653f56fdb339fc4764c81a52f11292
https://arbiscan.io/tx/0x76f9ef277b8441d59fca1d0b7a44544c1d8e9df3d35a0d65b132fc890f4722f0
https://arbiscan.io/tx/0xe0b4ce1f06e9cc49f38d525016391a7093f3ae6cf6561a8c50ea432d531e576c
https://arbiscan.io/tx/0x345cf85a171aa8c78259973fade7c64b7d4adcc90e7a599efd70f7f172a12637

---

**Chain**

op

**Funder Address**

0x770edb43ecc5bcbe6f7088e1049fc42b2d1b195c

**Number of addresses involved on chain op**

1174

**Transactions executing fund transfer**

https://optimistic.etherscan.io/tx/0xd65a6df2891f80dabf8042bfd2974c76df74b9c22d74b78fb044f56b752bd320
https://optimistic.etherscan.io/tx/0xbf8d1e3b5eff153d296e2188c9881dfe36b78b57c7e12b47e86f3faab527997c
https://optimistic.etherscan.io/tx/0x2f175c55a3aefdfc8ab2ce107fcfb43004f524cf42fd55d6ce949d0679818631
https://optimistic.etherscan.io/tx/0x40344be41b15e065b30dc349e2c73d547349faf243180104338fe2a2799dde19
https://optimistic.etherscan.io/tx/0x725de9e4d56ba5a1b5ccba4a1090fbb39c36951d61c0e47a4c557a7de8bc1cce
https://optimistic.etherscan.io/tx/0x94cef81645335ced4fbb5053be36e9d27a068b80692a73dd1b47b38aebf70ae9

# Cross-chain activity overlap outline

                       1123
          arb(1584) ----------  op(1174)
           /      \                /
          / 2       \  1135       /  1135
         /            \          /
     bsc(127) --------  polygon(2821)
                117

A node represents cluster found on chain 'xxx' with it's size. An edge and its weight represents number of address overlap between two chains.
