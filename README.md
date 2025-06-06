# Can Blockchain Improve Internal Audit Integrity?

A Python-Based Simulation and Real-World Audit Perspective  
**By Mayank Agarwal | Ex-EY | MSc FinTech – University of Liverpool**

---

## 📌 Executive Summary

This project explores how blockchain technology can be applied to internal auditing to reduce fraud, increase transparency, and improve trust in financial systems. Drawing from my audit experience at Ernst & Young (EY), I simulate a Python-based blockchain ledger to demonstrate how immutable, timestamped entries can create fraud-resistant audit trails.

---

## 🧠 Background

In many audit engagements, internal control failures—such as undocumented journal entries or backdated adjustments—increase the risk of misstatements or fraud. Traditional ERPs allow overwriting or deletion of entries, making audits vulnerable.

**This project asks:**  
Can blockchain create tamper-proof audit trails that eliminate audit override risks?

---

## 🔗 How Blockchain Helps

Blockchain is:
- **Immutable**: Data cannot be changed once recorded
- **Transparent**: New entries are visible to all nodes
- **Secure**: Tampering with one block alters all others

This is ideal for financial records, journal entries, and internal control environments.

---

## 💻 Python Simulation

We use a simple blockchain prototype in Python. Each block includes:
- Entry ID
- Timestamp
- Data (e.g., journal entry or approval)
- Previous hash
- Self-generated hash

### 🔸 Sample Code
```python
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
        content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(content.encode()).hexdigest()
```

---

## 🧾 Key Takeaways

- 🔐 **Tamper Detection**: Any change breaks the hash chain
- 🕒 **Timestamped Entries**: Entries can't be backdated or altered
- ✅ **Audit Transparency**: No need for ERP export logs
- 🤝 **External Validation**: Auditors can verify hashes externally

---

## 📁 Files

- `audit_blockchain.py`: Python code for simulation
- `Blockchain_Audit_Project_Mayank_Agarwal.docx`: Full project report

---

## 🧠 Reflection

This project allowed me to merge my audit background with FinTech skills. Blockchain has strong potential in internal audit, especially in:
- High-risk sectors (e.g., banking, insurance)
- AI-driven decisions (e.g., automated lending)

---

## 📌 CV Description Line

> Developed a blockchain-based Python simulation to demonstrate tamper-proof audit trails, integrating fraud risks observed during EY audit engagements.

---

## 📜 License

MIT License © Mayank Agarwal  
Free to use with attribution.
