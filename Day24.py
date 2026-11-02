#Day 24 tomorrow — BLEU & ROUGE: Text Quality Metrics.
def calculate_bleu(generated, reference):
    generated_words = reference.lower().split()
    reference_words = generated.lower().split()

    generated_set = set(generated_words)
    reference_set = set(reference_words)
    overlap = generated_set.intersection(reference_set)

    precision_like_bleu = len(overlap) / len(generated_set)
    recall_like_rouge = len(overlap) / len(reference_set)

    return {"overlap_words": overlap, "precision": precision_like_bleu, "recall": recall_like_rouge}

result = calculate_bleu("The cat sat on the mat", "The cat is on the mat")
print(result)