testcases = {
    "name": "Govardhan",
    "age": 35,
    "city": "Bangalore",
    "job": "QA Engineer",
    "experience": 10,
    "is_employed": True,
}
testcases["salary"] = 99785.65
del testcases["job"]

#print(testcases)
#print(testcases["name"])
#print(testcases["age"])
#print(testcases["city"])
#print(testcases["experience"])
#print(testcases["is_employed"])

#loop through key only
print("Loop through key only")
print("--------------------")
for key in testcases:
    print(key)

print("--------------------")
#loop through value only
print("Loop through value only")
print("--------------------")
for value in testcases.values():
    print(value)

print("--------------------")
#loop both key and value :
print("Loop both key and value :")
print("--------------------")
for key, value in testcases.items():
    print(key, ":", value)