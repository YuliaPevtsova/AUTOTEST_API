import httpx
'''
response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)
print(response.json())

data = {
    "title":"Новая задача",
    "completed": False,
    "userId":1
}

response = httpx.post(url="https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)
# print(response.request.headers)
print(response.json())

data1= {"username": "test_user", "password": "123456"}

response1 = httpx.post("https://httpbin.org/post", data=data1)

print(response1.status_code)
# print(response1.request.headers)
print(response1.json())

headers = {
    "Authorization": "Bearer my_secret_token"
}
response2 =httpx.get(url="https://httpbin.org/get", headers=headers)

print(response2.request.headers)
print(response2.json())

#Работа с qwery параметрами
params = {"userId":1}
response3 = httpx.get(url="https://jsonplaceholder.typicode.com/todos", params=params)

print(response3.url)
print(response3.json())

#Передача файлов
file = open("example.txt", "rb")
files = {"file":("example.txt", open(file)}
response4 = httpx.post("https://httpbin.org/post", files=files)
file.close()
print(response4.json())
# with open("example.txt", "rb") as file:
#     files = {"file": ("example.txt", file)}
#     response4 = httpx.post("https://httpbin.org/post", files=files)
#     print(response4.json())
# # файл автоматически закрывается здесь
#работа с сессиями

with httpx.Client() as client:
    resp1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    resp2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(resp1.json())
print(resp2.json())

client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response5 = client.get(url="https://httpbin.org/get")

print(response5.json())
'''
# Работа с ошибками в httpx
try:
    response =httpx.get(url="https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()
    print(response.status_code)
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")

try:
    response = httpx.get(url="https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")





