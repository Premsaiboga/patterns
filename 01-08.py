import requests

api1 = "https://jsonplaceholder.typicode.com/posts"
request = requests.get(api1)
print(request)
print(request.json())


api2 = "https://jsonplaceholder.typicode.com/photos"
request1 = requests.get(api2)
print(request1)
print(request1.json())


api3 = "https://rapidapi.com"
request3 = requests.get(api3)
print(request3)
print(request3.text)