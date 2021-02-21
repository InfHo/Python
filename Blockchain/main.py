from Block import Block

#das ist die Blockchain, am Anfang noch leer
blockchain = []

#erster Block
genesis_block = Block("Der Allererste Eintrag",
                      ["Nutzer 1 Sendet 1 BTC  zu Nutzer 2",
                       "Nutzer 3 sendet 2 BTC zu Nutzer 5"])

#fuege den ersten Block zur blockchain hinzu
blockchain.append(genesis_block)
##print(blockchain)

#zweiter Block
second_block = Block(genesis_block.block_hash,
                     ["Nutzer 3 sendet 1 BTC zu Nutzer 2",
                      "Nutzer 1 sendet 5 BTC zu Nutzer 3"])

#fuege den zweiten Block zur blockchain hinzu
blockchain.append(second_block)
##print(blockchain)

#dritter Block
third_block = Block(genesis_block.block_hash,
                     ["Nutzer 1 sendet 3 BTC zu Nutzer 5",
                      "Nutzer 4 sendet 1 BTC zu Nutzer 1"])

#fuege den dritten Block zur blockchain hinzu
blockchain.append(third_block)
##print(blockchain)

print("")

#zeige die Transaktionen und danach die Verschlüsselung (Hash) von Block 1
print(genesis_block.transactions)
print(genesis_block.block_hash)

print("")

#zeige die Transaktionen und danach die Verschlüsselung (Hash) von Block 2
print(second_block.transactions)
print(second_block.block_hash)

print("")

#zeige die Transaktionen und danach die Verschlüsselung (Hash) von Block 3
print(third_block.transactions)
print(third_block.block_hash)

print("")

#zeige die Objekte von Blockchain
print("das sind die Blockobjekte der blockchain:", blockchain)

print("")

#zeige die Transaktionen von jedem Block
for block in blockchain:
    print(block.transactions)

print("")

#zeige die Verschluesselungen von jedem Block
for block in blockchain:
    print(block.block_hash)
