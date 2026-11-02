#Day 23 tomorrow — Evaluation Concepts: Precision, Recall, F1
def calculate_precision_recall(predicted, actual):
    true_positive = 0
    false_positive = 0
    false_negative = 0

    for item in predicted:
        if item in actual:
            true_positive += 1
        else:
            false_positive += 1

    for item in actual:
        if item not in predicted:
            false_negative += 1

    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)
    f1_score = 2 * (precision * recall) / (precision + recall)


    return {"precision": precision, "recall": recall, "tp": true_positive, "fp": false_positive, "fn": false_negative, "f1_score": f1_score}


predicted_bugs = ["BUG-101", "BUG-102", "BUG-103"]
actual_critical_bugs = ["BUG-101", "BUG-102", "BUG-104","BUG-105","BUG-106","BUG-106"]

result = calculate_precision_recall(predicted_bugs, actual_critical_bugs)
print(result)