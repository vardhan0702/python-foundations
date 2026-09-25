listest_cases =["login", "logout", "search", "Add to Cart", "Payment"]
status = ["Passed", "Failed", "Passed", "Failed", "Passed"]
for index, (item, result) in enumerate(zip(listest_cases, status),2):
    print(index, ". ", item, "-->", result)