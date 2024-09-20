from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://lokesh:lokesh@cluster1.edory.mongodb.net/")
db = client["lokesh"]
db2 = client["lokesh_copy"]

# Collections to compare
collection1 = db["dbWatch"]
collection2 = db2["dbWatch"]

# Function to normalize documents by sorting their items
def normalize_document(doc):
    return tuple(sorted(doc.items()))  

# Fetch all documents from both collections
docs1 = [normalize_document(doc) for doc in collection1.find()]
docs2 = [normalize_document(doc) for doc in collection2.find()]

# Convert the documents to sets for comparison
set1 = set(docs1)
set2 = set(docs2)

# Find differences
only_in_collection1 = set1 - set2
only_in_collection2 = set2 - set1

print("Documents only in collection1:")
for doc in only_in_collection1:
    print(dict(doc))

print("\nDocuments only in collection2:")
for doc in only_in_collection2:
    print(dict(doc))
