import requests

response = requests.get("https://api.github.com")
print(response.status_code)
JsonResp = response.json()
print(JsonResp["emojis_url"])

