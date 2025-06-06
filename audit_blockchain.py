import hashlib
import datetime

class Block:
    """Represents a single block in the blockchain audit trail."""
    def __init__(self, index, timestamp, data, previous_hash):
        """Initialize a new block with audit data and metadata."""
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Generate SHA-256 hash of the block contents."""
        content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(content.encode()).hexdigest()

    def __str__(self):
        return (
            f"Block #{self.index}\n"
            f"Timestamp: {self.timestamp}\n"
            f"Data: {self.data}\n"
            f"Hash: {self.hash[:15]}...\n"
            f"Previous Hash: {self.previous_hash[:15]}...\n"
        )

class Blockchain:
    """Represents the full blockchain ledger for audit simulation."""
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """Create the initial block with default message."""
        return Block(0, datetime.datetime.now(), "Audit Entry Initialized", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        """Add a new block to the chain."""
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), datetime.datetime.now(), data, latest_block.hash)
        self.chain.append(new_block)

    def print_chain(self):
        """Display the blockchain contents."""
        for block in self.chain:
            print(block)

# 🚀 Example Usage
if __name__ == "__main__":
    audit_chain = Blockchain()
    audit_chain.add_block("Journal Entry: JE12345")
    audit_chain.add_block("Approval by CFO")
    audit_chain.add_block("Vendor Payment Authorized")
    audit_chain.print_chain()
