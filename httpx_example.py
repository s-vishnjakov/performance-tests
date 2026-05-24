import httpx

# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
# print(response.status_code)
# print(response.text)
#
#
# data = {
#     "title": "new task",
#     "completed": False,
#     "userId": 1
# }
#
# response = httpx.post("https://jsonplaceholder.typicode.com/todos")
#
# print(response.status_code)
# print(response.json())
#
# head = {"Authorization": "Bearer my_secret_token"}
# response = httpx.get("https://httpbin.org/get", headers=head)
#
# print(response.status_code)
# print(response.json())

# parameters = {"userId": 1, "age": 30}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=parameters)
#
# print(response.request.url, response.request.url.query)
# print(response.status_code)
# print(response.json())
#
# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=files)
#
# print(response.status_code)
# print(response.text)


# with httpx.Client() as client:
#     resp1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     resp2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
# print(resp1.json())
# print(resp2.json())


# responce = httpx.get("https://jsonplaceholder.typicode.com/todos/1", timeout=None)
# responce.raise_for_status()
# print(responce.status_code)

# try:
#     responce = httpx.get("https://httpbin.org/delay/5", timeout=2)
# except httpx.ReadTimeout as e:
#     print("ЗАпрос превысил лимит времени")

with httpx.Client() as client:
    for _ in range(10):
        response = client.get("https://jsonplaceholder.typicode.com/todos/1")
        print(response)