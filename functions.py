def greet_user(name):
    print("Hello", name, "Welcome to AI Testing World!")

greet_user("Govardhan")
greet_user("John")
greet_user("Alice")

print("======================================")
#using return statement in function :
print("Using return statement in function :")
def add_number(a,b):
    return a+b

total = add_number(100,28.5)
print("Total is : ", total)
print("======================================")

#using return statement in function :
print("Using without return statement in function :")
def add_number(a,b):
    result= a+b

total = add_number(100,28.5)
print("Total is : ", total)
print("======================================")


print("Pass Percentage Calculation using function :")
def calculate_pass_percentage(passed, total):
    percentage = (passed/total)*100
    return percentage

pass_percentage = calculate_pass_percentage(45, 50)
print("Pass Percentage is : ", pass_percentage)
print("======================================")

pass_percentage = calculate_pass_percentage(25, 50)
print("Pass Percentage is : ", pass_percentage)
print("======================================")

pass_percentage = calculate_pass_percentage(12.5,50)
print("Pass Percentage is : ", pass_percentage)
print("======================================")


print("evaluate_test_run function to evaluate test run :")
def evaluate_test_run(testcases):
    Total = len(testcases)
    Passed = 0
    Failed = 0

    for testcase in testcases:
        if testcase["status"]=="Passed":
            Passed +=1
        elif testcase["status"]=="Failed":
            Failed +=1
            
    return {"Total" : Total, "Passed" : Passed, "Failed" : Failed}




eval = evaluate_test_run([
    {"id": "TC001", "name": "Login ", "status": "Passed", "priority": "High"},
    {"id": "TC002", "name": "Logout", "status": "Failed", "priority": "Medium"},
    {"id": "TC003", "name": "Change Password", "status": "Failed", "priority": "Low"},
    {"id": "TC004", "name": "Payment", "status": "Passed", "priority": "Low"},
    {"id": "TC005", "name": "Order", "status": "Passed", "priority": "Low"}
])

print("Total Testcases : ", eval["Total"])
print("Total Passed Testcases : ", eval["Passed"])
print("Total Failed Testcases : ", eval["Failed"])