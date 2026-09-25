import json
eval_report = {
    "run_id": "RUN001",
    "summary": {
        "total": 8,
        "passed": 4,
        "failed": 1
    },
    "test_cases": [
        {"id": "TC001", "status": "Passed"},
        {"id": "TC002", "status": "Failed"}
    ]
}

jString = json.dumps(eval_report)
print(jString)

pyDict=json.loads(jString)

print(pyDict["summary"]["passed"])
print(pyDict["test_cases"][1]["id"])