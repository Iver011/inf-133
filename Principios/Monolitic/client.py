import requests

url='http://localhost:8000'

response= requests.get(f"{url}/posts")
print(response.text)


response= requests.get(f"{url}/post/2")
print(response.text)


new_post_data = {
    "title": "Mi experiencia como dev",
    "content": "Es complicado",}


response = requests.post(f"{url}/posts", json=new_post_data)
print(response.text)

response= requests.delete(f"{url}/post/2")
print(response.text)

response= requests.get(f"{url}/posts")
print(response.text)



