pass_percentage =55

if pass_percentage>=80:
    print("SSTABLE — Safe to release")
elif pass_percentage>=60:
    print("WARNING — Review before release")
else:
    print("CRITICAL — Do not release")


# and  # both conditions must be true
# or   # at least one condition must be true
# not  # reverses the condition

print("--------------------------------------------------------------")
print ("Using logical operators in if else condition :")
print("--------------------------------------------------------------")
pass_percentile=75
critical_bugs =2

if pass_percentile>=75 or critical_bugs==0:
    print("SSTABLE — Safe to release")
elif pass_percentile>=60 and critical_bugs<=1:
    print("WARNING — Review before release")
else:
    print("CRITICAL — Do not release")

print("--------------------------------------------------------------")
#evaluate_test_run function to evaluate test run :
testcases = [
    {"id": 1, "name": "Test Case 1", "status": "Passed"},
    {"id": 2, "name": "Test Case 2", "status":  "Failed"},
    {"id": 3, "name": "Test Case 3", "status":  "Passed"},
    {"id": 4, "name": "Test Case 4", "status":  "Failed"},
    {"id": 5, "name": "Test Case 5", "status":  "Passed"},
]

def evaluate_test_run(testcases):
    total_testcases =len(testcases) #5
    passed = 0
    failed = 0
    

    for testcase in testcases:
        if testcase["status"]=="Passed":
            passed +=1
        elif testcase["status"]=="Failed":
            failed +=1

    passpercentage=(passed/total_testcases)*100

    if passpercentage>=80 and failed==0:
        final_outout ="GREEN — Ship it"
    elif passpercentage>=75 and failed<=2:
        final_outout ="AMBER — Review required"
    else:
        final_outout ="RED — Do not ship"

    return passed, failed, passpercentage, final_outout,total_testcases

output = evaluate_test_run(testcases)

print("Total Testcases : ", output[4])
print("Passed : ", output[0])
print("Failed : ", output[1])
print("Pass Percentage : ", output[2])
print("Final Output : ", output[3])

print("--------------------------------------------------------------")


print("evaluate_test_run function to evaluate test run using dictionary as return type")
#evaluate_test_run function to evaluate test run using dictionary as return type :
testcases1 = [
    {"id": 1, "name": "Test Case 1", "status": "Passed"},
    {"id": 2, "name": "Test Case 2", "status":  "Failed"},
    {"id": 3, "name": "Test Case 3", "status":  "Passed"},
    {"id": 4, "name": "Test Case 4", "status":  "Passed"},
    {"id": 5, "name": "Test Case 5", "status":  "Passed"},
    {"id": 6, "name": "Test Case 5", "status":  "Passed"},
    {"id": 7, "name": "Test Case 5", "status":  "Passed"},
    {"id": 8, "name": "Test Case 5", "status":  "Passed"},
    {"id": 9, "name": "Test Case 5", "status":  "Passed"},
    {"id": 10, "name": "Test Case 5", "status":  "Passed"}
]

def evaluate_test_run1(testcases1):
    total_testcases =len(testcases1) #5
    passed = 0
    failed = 0
    

    for testcase in testcases1:
        if testcase["status"]=="Passed":
            passed +=1
        elif testcase["status"]=="Failed":
            failed +=1

    passpercentage=(passed/total_testcases)*100

    if passpercentage>=80 and failed==0:
        final_outout ="GREEN — Ship it"
    elif passpercentage>=75 and failed<=2:
        final_outout ="AMBER — Review required"
    else:
        final_outout ="RED — Do not ship"

    return {"Total Testcases" : total_testcases, "Passed" : passed, "Failed" : failed, "Pass Percentage" : passpercentage, "Final Output" : final_outout}

output1 = evaluate_test_run1(testcases1)

print("Total Testcases : ", output1["Total Testcases"])
print("Passed : ", output1["Passed"])
print("Failed : ", output1["Failed"])
print("Pass Percentage : ", output1["Pass Percentage"])
print("Final Output : ", output1["Final Output"])

print("--------------------------------------------------------------")