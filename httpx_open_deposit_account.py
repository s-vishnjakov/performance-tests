import httpx
from faker import Faker
import time

fake = Faker()

create_user_payload = {
    "email": f"user{time.time()}@ms.ru",
    "lastName": f"{fake.last_name()}",
    "firstName": f"{fake.first_name()}",
    "middleName": "",
    "phoneNumber": f"{fake.basic_phone_number()}"
}

create_user_response = httpx.post('http://localhost:8003/api/v1/users', json=create_user_payload)
created_user_id = create_user_response.json()["user"]["id"]

open_deposit_account_payload = {'userId': created_user_id}

open_deposit_account = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account",
                                  json=open_deposit_account_payload)
open_deposit_account_data = open_deposit_account.json()

print(f'Deposit creation data:', open_deposit_account_data, sep='\n')
print(f'Deposit creation status code:', open_deposit_account.status_code)
