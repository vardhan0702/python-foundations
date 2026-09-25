import requests
url = "https://httpbin.org/post"
data = {"id":"O0041","name":"Govardhana","Role":"Senior AI Model Evaluator"}

response = requests.post(url, json=data)#json=data, we are telling the system that we are sending the data which is json foramt, the one we are using in "data" is python dictionary
print(response.status_code)

result =response.json()
print(result["json"]["name"]) #here we are converting the plain json string back to the pythin dictionary

