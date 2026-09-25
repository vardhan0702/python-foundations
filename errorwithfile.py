import csv

def readcsvfile(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            passed=0
            failed=0
            percentage=0
            total=0
            for row in reader:
                if row["status"]=="Passed":
                    passed+=1
                elif row["status"]=="Failed":
                    failed+=1
                total+=1
                percentage= (passed/total)*100
        return {"FileFound": "True","Passed" : passed, "Failed":failed, "Total":total, "Percentage":percentage}
    except FileNotFoundError:
        print("Error: The file does not exist.")
        return {"FileFound": "False","Passed" : 0, "Failed":0, "Total":0, "Percentage":0}  

eval= readcsvfile("testdata.txt")
print("File Found:", eval["FileFound"])
print("Total test cases passed",eval["Passed"])
print("Total test cases failed",eval["Failed"])
print("Percentage test cases passed",eval["Percentage"])  

    
    
