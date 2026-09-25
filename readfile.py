import csv

with open("testdata.txt","w",newline="")as file:
	writer =csv.writer(file)
	writer.writerow(["id","name","status"])
	writer.writerow(["TC01","Login","Pass"])
	writer.writerow(["Tc02", "Logout", "failed"])

    