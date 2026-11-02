from locust import task, events
from locust.env import Environment

from clients.http.gateway.locust import GatewayHTTPTaskSet
from seeds.scenarios.existing_user_make_purchase_operation import ExistingUserMakePurchaseOperationSeedsScenario
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


# Init hook — called before the load starts
@events.init.add_listener
def init(environment: Environment, **kwargs):
    # Seeding
    seeds_scenario = ExistingUserMakePurchaseOperationSeedsScenario()
    seeds_scenario.build()  # создаём пользователей, счета, карты и операции

    # Loading seeding result from saved json file
    environment.seeds = seeds_scenario.load()


# TaskSet — user scenario. Every virtual user executing these tasks
class MakePurchaseOperationTaskSet(GatewayHTTPTaskSet):
    seed_user: SeedUserResult  # Typed reference to data from seeding

    def on_start(self) -> None:
        super().on_start()
        # Get a random user from the prepared list
        self.seed_user = self.user.environment.seeds.get_random_user()

    @task(1)
    def make_purchase_operation(self):
        # Make purchase operation with the 1st user's card
        self.operations_gateway_client.make_purchase_operation(
            card_id=self.seed_user.credit_card_accounts[0].physical_cards[0].card_id,
            account_id=self.seed_user.credit_card_accounts[0].account_id
        )

    @task(2)
    def get_accounts(self):
        # Get a list of user accounts
        self.accounts_gateway_client.get_accounts(user_id=self.seed_user.user_id)

    @task(2)
    def get_operations(self):
        # Get a list of transactions on an account
        self.operations_gateway_client.get_operations(
            account_id=self.seed_user.credit_card_accounts[0].account_id
        )

    @task(2)
    def get_operations_summary(self):
        # Get statistics on user operations
        self.operations_gateway_client.get_operations_summary(
            account_id=self.seed_user.credit_card_accounts[0].account_id
        )


# A custom class that run TaskSet
class MakePurchaseOperationScenarioUser(LocustBaseUser):
    tasks = [MakePurchaseOperationTaskSet]
