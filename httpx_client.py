import httpx
from faker import Faker
import time

fake = Faker()
client = httpx.Client(
    base_url="http://localhost:8003",
    timeout=3,
    headers={"authorization": "Bearer ..."}
)

payload = {
    "email": f"user{time.time()}@ms.ru",
    "lastName": f"{fake.last_name()}",
    "firstName": f"{fake.first_name()}",
    "middleName": "",
    "phoneNumber": f"{fake.basic_phone_number()}"
}
response = client.post('/api/v1/users', json=payload)

print(response.text)
print(response.request.headers)


