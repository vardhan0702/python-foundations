import json
testcases ={"id": 1, "name": "John", "age": 30, "city": "New York"}
jsonString = json.dumps(testcases)
print(jsonString)
print(type(jsonString))


python_dict = json.loads(jsonString)
print(python_dict)
print(type(python_dict))    