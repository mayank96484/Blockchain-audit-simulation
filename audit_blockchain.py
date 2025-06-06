import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(value.encode()).hexdigest()

    def __str__(self):
        return f"Block #{self.index} | Time: {self.timestamp} | Data: {self.data} | Hash: {self.hash[:10]}..."

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Audit Entry Initialized", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), datetime.datetime.now(), data, latest_block.hash)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(block)

# Example usage
if __name__ == "__main__":
    audit_chain = Blockchain()
    audit_chain.add_block("Journal Entry: JE12345")
    audit_chain.add_block("Approval by CFO")
    audit_chain.add_block("Vendor Payment Authorized")
    audit_chain.print_chain()
