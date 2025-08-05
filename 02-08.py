#  Create a json server and 2 endpoints and apply CRUD operations on both of them
import requests
import json

#geting the information from the URL or API
url = "http://localhost:3000/users"
req = requests.get(url)
print(req)
print(req.json())

url2 = "http://localhost:3000/posts"
data = requests.get(url2)
print(data)
print(data.json())

# post the information
posting = requests.post(url,json={"id":"3","name":"Parasad","age": "32"})

#deleteing the information
deleteing = requests.delete("http://localhost:3000/users/ed6d")

# updating the information:
updateing = requests.put("http://localhost:3000/users/2",json={"id":"2","name":"renuka","age":"25"})

updateing = requests.patch("http://localhost:3000/users/2",json={"name": "pavan"})

