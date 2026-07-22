import requests

response = requests.get("https://dummyjson.com/recipes")
print(response.json())
