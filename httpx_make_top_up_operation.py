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
create_user_response_data = create_user_response.json()

open_debit_card_account_payload = {
    "userId": create_user_response_data['user']['id']
}
open_debit_card_account_response = httpx.post('http://localhost:8003/api/v1/accounts/open-debit-card-account',
                                              json=open_debit_card_account_payload)
open_debit_card_account_response_data = open_debit_card_account_response.json()

make_top_up_operations_payload = {
  "status": "COMPLETED",
  "amount": 1500,
  "cardId": open_debit_card_account_response_data['account']['cards'][0]['id'],
  "accountId": open_debit_card_account_response_data['account']['id']
}
make_top_up_operations_response = httpx.post("http://localhost:8003/api/v1/operations/make-top-up-operation",
                                             json=make_top_up_operations_payload)

make_top_up_operations_response_data = make_top_up_operations_response.json()

print('Make top up operation response:', make_top_up_operations_response_data)
print('Make top up operation status code:', make_top_up_operations_response.status_code)
