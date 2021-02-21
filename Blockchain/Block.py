import hashlib

class Block:
    """ erstelle ein Blockobjekt mit Transaktionen, Verschluesselung (hash)
    aus aktuellem hash und vorherigem hash"""
    def __init__(self,
                 previous_hash,
                 transactions):
        self.transactions = transactions
        self.previous_hash = previous_hash
        string_to_hash = "".join(transactions) + previous_hash
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()
