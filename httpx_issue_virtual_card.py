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

issue_virtual_card_payload = {
    "userId": create_user_response_data['user']['id'],
    "accountId": open_debit_card_account_response_data['account']['id']
}

issue_virtual_card_response = httpx.post('http://localhost:8003/api/v1/cards/issue-virtual-card',
                                         json=issue_virtual_card_payload)

issue_virtual_card_response_data = issue_virtual_card_response.json()

print('Issue virtual card response:', issue_virtual_card_response_data, sep='\n')
print('issue virtual card status code:', issue_virtual_card_response.status_code)
