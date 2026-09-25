import csv

def readcsvfile(filename):
    with open(filename,"r") as file :
        reader = csv.DictReader(file)
        Passed=0
        Failed=0
        Total=0
        
        for row in reader:
            if row["status"]=="Passed":
                Passed+=1
            elif row["status"]=="Failed":
                Failed+=1
            Total+=1
        Percentage = (Passed/Total)*100
    return {"Passed" : Passed, "Failed":Failed, "Total":Total, "Percentage":Percentage}

eval = readcsvfile("testdata.txt")
print("Total test cases passed",eval["Passed"])
print("Total test cases failed",eval["Failed"])
print("Percentage test cases passed",eval["Percentage"])
