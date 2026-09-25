api_response = {
    "id": "12345",
    "content" :[
        {"id": "1", "name": "John", "age": 30, "city": "New York"},
    ],
    "usage" : {"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30}
}

print(api_response)
print(api_response["content"][0]["name"])  # Accessing the name of the first content item
print(api_response["usage"]["total_tokens"])  # Accessing the total tokens used
print(api_response["id"])  # Accessing the id of the API response