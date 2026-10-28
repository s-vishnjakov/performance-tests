from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan


class ExistingUsersGetDocumentsSeedsScenario(SeedsScenario):
    """
    Seedling scenario for an existing user viewing their accounts and documents.
    Create 100 users, each of whom receives a debit and savings account.
    """
    @property
    def plan(self) -> SeedsPlan:
        """
        Returns the seeding plan for creating users and their accounts.
        We're creating 100 users, each of whom will receive a debit and savings account.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=100,
                savings_accounts=SeedAccountsPlan(count=1),
                deposit_accounts=SeedAccountsPlan(count=1)
            )
        )
    
    @property
    def scenario(self):
        """
        Returns the seeding scenario name.
        This name will be used to save seeding data.
        """
        return "existing_user_get_documents"

if __name__ == '__main__':
    """
    Launch the seeding script manually.
    Create a script object and call the build method to create the data.
    """
    seeds_scenario = ExistingUsersGetDocumentsSeedsScenario()
    seeds_scenario.build()
