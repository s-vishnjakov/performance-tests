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

open_credit_card_account_payload = {
    "userId": create_user_response_data['user']['id']
}
open_credit_card_account_response = httpx.post('http://localhost:8003/api/v1/accounts/open-credit-card-account',
                                               json=open_credit_card_account_payload)

open_credit_card_account_data = open_credit_card_account_response.json()

make_purchase_operation_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "cardId": open_credit_card_account_data['account']['cards'][0]['id'],
    "accountId": open_credit_card_account_data['account']['id'],
    "category": "taxi"
}
make_purchase_operation_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation",
                                              json=make_purchase_operation_payload)

credit_card_operation_data = make_purchase_operation_response.json()

get_operation_receipt = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/"
                                  f"{credit_card_operation_data['operation']['id']}")

print(get_operation_receipt.json())
