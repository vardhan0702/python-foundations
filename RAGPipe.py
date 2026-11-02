import chromadb

client = chromadb.Client()
collection = client.create_collection(name ="testcases")

collection.add(
    documents=["Test case 1: Verify login functionality with valid credentials.",
               "Test case 2: Verify login functionality with invalid credentials.",
               "Test case 3: Verify password reset functionality.",
               "Test case 4: Verify account lockout after multiple failed login attempts.",
               "Test case 5: Verify login page UI elements and responsiveness."
               ],
    ids=["TC01", "TC02", "TC03", "TC04", "TC05"]
)

print("Collection created and test cases added successfully.")
print("Total documents in the collection:", collection.count())  # Print the total number of documents in the collection
print("Documents in the collection:", collection.get())  # Print the documents in the collection

results= collection.query(
    query_texts=["What happens if someone enters the wrong password?"],
    n_results=2
)

print("Query results:", results)