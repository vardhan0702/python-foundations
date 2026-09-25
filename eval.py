testcases =[
	{"id":"TestCase01", "Title":"Login", "Status":"Passed","Priority":"High"},
	{"id":"TestCase02", "Title":"Logout", "Status":"Failed","Priority":"Low"},
	{"id":"TestCase03", "Title":"Order", "Status":"Passed","Priority":"High"},
	{"id":"TestCase04", "Title":"Payment", "Status":"Failed","Priority":"Low"},
	{"id":"TestCase05", "Title":"Checkout", "Status":"Passed","Priority":"High"},
	
]

def eval_test(testcases):
	Passed =0
	Failed=0
	Total_TestCases = len(testcases)
		
	for testcase in testcases :	
		if(testcase["Status"]=="Passed"):
			Passed+=1
		elif(testcase["Status"]=="Failed"):
			Failed+=1
	
		Percentage = (Passed/Total_TestCases)*100
	return {"Passed" : Passed, "Failed":Failed, "Total":Total_TestCases, "Percentage":Percentage}

eval = eval_test(testcases)
print("Total test cases passed",eval["Passed"])
print("Total test cases failed",eval["Failed"])
print("Percentage test cases passed",eval["Percentage"])