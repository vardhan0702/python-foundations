from  transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("I love using Hugging Face's transformers library!")
print("result : - ", result)
print("-------------------------------------------------------------")
print(result[0]['label'])

result1 = classifier("I hate waiting in long lines at the grocery store.")
print("result1 : - ", result1)
print("-------------------------------------------------------------")
print(result1[0]['label'])