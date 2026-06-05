import httpx
import time

create_user_payload = {
  "email": f"user.{time.time()}@example.com",
  "lastName": "Nolik",
  "firstName": "Tolik",
  "middleName": "Petrovich",
  "phoneNumber": "7778877788"
}

create_user_response = httpx.post('http://localhost:8003/api/v1/users', json=create_user_payload)
create_user_response_data = create_user_response.json()

print('Create user response:', create_user_response_data)
print('Status code:', create_user_response.status_code)

get_user_response = httpx.get(f"http://localhost:8003/api/v1/users/{create_user_response_data['user']['id']}")
get_user_response_data = get_user_response.json()

print('Get user response:', get_user_response_data)
print("Status code:", get_user_response.status_code)
