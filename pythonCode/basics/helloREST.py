import requests

url = "https://jsonplaceholder.typicode.com/posts/10"
response = requests.get(url)
print("HEADER:")
print(response.headers["content-type"])
print("RESPONSE:")
print(response.json())