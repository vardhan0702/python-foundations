#Day 26 Mini Eval Project (Phase 1 Capstone)
from dotenv import load_dotenv
import os
import anthropic
import json
load_dotenv()

api_key =  os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

qa_questions = [
{"question" : "In software testing,what is a bug ?","reference_answer" : "A bug is deviation from expected and actual behvaior of the system"},
{"question" : "In software testing, what is a defect ?","reference_answer" : "When bug reported by tester and accepted by development team"},
{"question" : "In software testing, what is a error ?","reference_answer" : "An error is the logical mistke made by developer in the program"},
{"question" : "In software testing, what is a failure ?","reference_answer" : "When bug is missed and identified in the final system then it is called failure"},
{"question" : "In software testing, what is a CR ?","reference_answer" : "CR is change request usuallay made by clients when its underlying structure requires change and sent for approval once it is approved then dev will implement it"}
]

def evaluate_response(qa):
        reference_words = qa["reference_answer"].lower().split()
        generated_words = qa["claude_response"].lower().split()
        generated = set(generated_words)
        reference = set(reference_words)
        overlap = generated.intersection(reference)
        precision_like_bleu = len(overlap) / len(generated)
        recall_like_rouge = len(overlap) / len(reference)
        return {"overlap_words": overlap, "precision": precision_like_bleu, "recall": recall_like_rouge}

for qa in qa_questions:
    question = qa["question"]
    
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=800,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )
    
    generated_answer = response.content[0].text
    qa["claude_response"]=generated_answer
    #print(f"Question: {question}")
    #print(f"Generated Answer: {generated_answer}")
    #print("-" * 50)

for item in qa_questions:
        evaluation_result = evaluate_response(item)
        item["evaluation_result"] = evaluation_result

with open("eval_scorecard.json", "w") as file:
       json.dump(qa_questions, file, indent=4,default=list)
print("Scorecard saved to eval_scorecard.json")
