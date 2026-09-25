testcasetracker = {
    "test1": {"id": "TC001", "name": "Login ", "status": "Pending", "priority": "High"},
    "test2": {"id": "TC002", "name": "Logout ", "status": "Pending", "priority": "Medium"},
    "test3": {"id": "TC003", "name": "Add to Cart", "status": "Pending", "priority": "Low"},
    "test4": {"id": "TC004", "name": "ORDER", "status": "Pending", "priority": "High"},
    "test5": {"id": "TC005", "name": "PAYMENT", "status": "Pending", "priority": "Medium"},
}

for key, value in testcasetracker.items():
    print(value["id"], "|", value["name"], "|", value["status"], "|", value["priority"])
    print("---------------------------------")

for key, value in testcasetracker.items():
    print(key, ":", value["id"], "|", key, ":", value["name"], "|", key, ":", value["status"], "|", key, ":", value["priority"])
    print("---------------------------------")


#using list of dictionaries now :
print("Using list of dictionaries now :")
testcases = [
    {"id": "TC001", "name": "Login ", "status": "Pending", "priority": "High"},
    {"id": "TC002", "name": "Logout ", "status": "Pending", "priority": "Medium"},
    {"id": "TC003", "name": "Add to Cart", "status": "Pending", "priority": "Low"},
    {"id": "TC004", "name": "ORDER", "status": "Pending", "priority": "High"},
    {"id": "TC005", "name": "PAYMENT", "status": "Pending", "priority": "Medium"}
]

for testcase in testcases:
    print(testcase["id"], "|", testcase["name"], "|", testcase["status"], "|", testcase["priority"])
    print("---------------------------------")

print("printing list of dictionaries using just index of the list :")
print(testcases[0])
print(testcases[1])

print("------------------------------")
for index, testcase in enumerate(testcases):
    print(index," | ", testcase)

for testcase in testcases:
    print(testcase)
    
for testcase in testcases:
    print(testcase["id"])