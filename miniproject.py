import json
testcases = [
    {"id":"001","Name":"Login","status":"passed"},
    {"id":"002","Name":"HomePage","status":"failed"},
    {"id":"003","Name":"Order","status":"passed"},
    {"id":"004","Name":"CheckOut","status":"failed"},
    {"id":"005","Name":"Payment","status":"passed"},
    {"id":"006","Name":"Profile","status":"blocked"},
    {"id":"007","Name":"cards","status":"Not Applicable"},
    {"id":"008","Name":"summary","status":"In Progress"},

]

def evaltest(result):
    try:
        passed = 0
        failed = 0
        total = 0
        percentage = 0

        for item in result:
            if item["status"]=="passed":
                passed+=1
            elif item["status"]=="failed":
                failed+=1
            total+=1
        percentage = ((passed+failed)/total)*100
    except ZeroDivisionError:
     print("Cannot divide by zero")

    return {"Passed":passed, "Failed":failed, "Total": total, "Percentage":percentage}

    

eval= evaltest(testcases)
with open("eval_result.json","w") as file:
    json.dump(eval,file)

with open("eval_result.json","r") as file:
    loaded_report = json.load(file)
    
print("Percentage is -- ",loaded_report["Percentage"])
print("Total test cases passed : ", eval["Passed"])
print("Total test cases failed : ", eval["Failed"])
print("Total test cases  : ", eval["Total"])
print("Percentage of test cases are passed : ", eval["Percentage"])

