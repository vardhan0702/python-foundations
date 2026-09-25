testcases =["Govardhana", 37, 99699.58, True]
for a in testcases:
    print("Item in the list :", a)

test_cases = ["Login", "Logout", "Search", "Add to Cart", "Payment"]
for item in test_cases:
    print(test_cases.index(item)+1,". ", item)

print ("#using enumerate function")
for number, item in enumerate(test_cases):
    print(str(number),". ", item)

print ("#using enumerate function with start of the index")
for number, item in enumerate(test_cases,1):
    print(str(number),". ", item)
