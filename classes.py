class testCases:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def mark_as_blocked(self):
        self.status = "Blocked"

    def show(self):
        print("Test Case ID: ","--",self.id, "Test Case Name: ","--",self.name, "Test Case Status: ","--",self.status)

tc1=testCases(1,"Login ","Passed")
tc2=testCases(2,"Logout ","Failed")

tc1.mark_as_blocked()
tc1.show()
tc2.show()