from transformers import pipeline

user_comments = [
    {"comment": "The search results page is not displaying any message when there are no results found. This can confuse users."},
    {"comment": "The loading spinner is surprisingly fast."},
    {"comment": "The error message for invalid input is very helpful."},
    {"comment": "The pagination controls are intuitive to use but may be confusing for some users."},
    {"comment": "The filter options are not clearly labeled."}
]

def analyze_comments(comments):
    classifier = pipeline("sentiment-analysis")
    for comment in comments:
        result = classifier(comment["comment"])
        print(comment["comment"], ": - ", result)

analyze_comments(user_comments)
        