from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedCardsPlan


class ExistingUserMakePurchaseOperationSeedsScenario(SeedsScenario):
    """
    Seedling script for an existing user who makes a purchase.
    Creates 300 users, opens a credit account, and issues cards.
    """
    @property
    def plan(self) -> SeedsPlan:
        """
        A seeding plan that describes how many users need to be created
        and what data to generate for them.
        In this case, we're creating 300 users, each with a credit account and card.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    physical_cards=SeedCardsPlan(count=1)
                )
            )
        )

    @property
    def scenario(self) -> str:
        """
        The name of the seeding script that will be used to save data.
        """
        return "existing_user_make_purchase_operation"

if __name__ == '__main__':
    # If the file is run directly, create a script object and run it.
    seeds_scenario = ExistingUserMakePurchaseOperationSeedsScenario()
    seeds_scenario.build()  # Start the seeding process
