from clients.grpc.gateway.users.client import build_users_gateway_grpc_client
from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.operations.client import build_operations_gateway_grpc_client


'''Initializing clients'''
users_gateway_client = build_users_gateway_grpc_client()
accounts_gateway_client = build_accounts_gateway_grpc_client()
make_top_up_operation_client = build_operations_gateway_grpc_client()

"""
The script makes a TOP_UP operation with the following steps:
- user creation;
- debit account opening;
- makes top_up operation.
"""

create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(
    user_id=create_user_response.user.id
)
print('Open debit card account response:', open_debit_card_account_response)

account_top_up_response = make_top_up_operation_client.make_top_up_operation(
    account_id=open_debit_card_account_response.account.id,
    card_id=open_debit_card_account_response.account.cards[0].id
)
print('Make top up operation response:', account_top_up_response)
