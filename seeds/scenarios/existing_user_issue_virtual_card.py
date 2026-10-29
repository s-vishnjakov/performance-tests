from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan


class ExistingUserIssueVirtualCardSeedsScenario(SeedsScenario):
    """
    Seeding scenario for an existing user issuing a virtual card.
    Creates users, each of whom receives a debit card account.
    """
    @property
    def plan(self) -> SeedsPlan:
        """
        Returns the seeding plan for creating users and their accounts.
        We're creating users, each of whom will receive a debit card account.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,
                debit_card_accounts=SeedAccountsPlan(count=1)
            )
        )

    @property
    def scenario(self) -> str:
        """
        Returns the seeding scenario name.
        This name will be used to save seeding data.
        """
        return "existing_user_issue_virtual_card"


if __name__ == '__main__':
    """
    Launch the seeding script manually.
    Create a script object and call the build method to create the data.
    """
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build()
