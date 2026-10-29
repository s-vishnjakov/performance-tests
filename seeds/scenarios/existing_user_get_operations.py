from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedOperationsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Seeding scenario for obtaining information about credit card transactions.
    """
    @property
    def plan(self) -> SeedsPlan:
        """
        Returns the seeding plan for creating users and their accounts.
        300 users creation, each of whom will receive a credit card account
        with certain operations on it.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    purchase_operations=SeedOperationsPlan(count=5),
                    top_up_operations=SeedOperationsPlan(count=1),
                    cash_withdrawal_operations=SeedOperationsPlan(count=1)
                )
            )
        )

    @property
    def scenario(self) -> str:
        """
        Returns the seeding scenario name.
        This name will be used to save seeding data.
        """
        return "existing_user_get_operations"


if __name__ == '__main__':
    """
    Launch the seeding script manually.
    Create a script object and call the build method to create the data.
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()
