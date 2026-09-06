import time

from faker import Faker
from faker.providers.python import TEnum


class Fake:
    """
    Random test data generator built on top of the Faker library.
    """
    def __init__(self, faker: Faker):
        """
        :param faker: The Faker instance used to generate the data.
        """
        self.faker = faker

    def enum(self, value: type[TEnum]) -> TEnum:
        """
        Picks a random member of the given enum type.

        :param value: The enum class to pick a value from.
        :return: A random member of the enumeration.
        """
        return self.faker.enum(value)

    def email(self) -> str:
        """
        Generates a random email address.

        A random domain is used unless another one is specified.
        :return: A random email address.
        """
        return f"{time.time()}.{self.faker.email()}"

    def category(self) -> str:
        """
        Generates a random purchase category from a predefined list.

        Used to simulate spending types in systems that model user
        transactions or payment behaviour for goods and services.

        :return: A random category (for example, 'gas', 'taxi', 'supermarkets').
        """
        return self.faker.random_element([
            "gas",
            "taxi",
            "tolls",
            "water",
            "beauty",
            "mobile",
            "travel",
            "parking",
            "catalog",
            "internet",
            "satellite",
            "education",
            "government",
            "healthcare",
            "restaurants",
            "electricity",
            "supermarkets"
        ])

    def last_name(self) -> str:
        """
        Generates a random last name.

        :return: A random last name.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Generates a random first name.

        :return: A random first name.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Generates a random middle name.

        :return: A random middle name.
        """
        return self.faker.first_name_male()

    def phone_number(self) -> str:
        """
        Generates a random phone number.

        :return: A random phone number.
        """
        return self.faker.phone_number()

    def float(self, start: int = 1, end: int = 100) -> float:
        """
        Generates a random floating point number within the given range.

        :param start: The lower bound of the range (inclusive).
        :param end: The upper bound of the range (inclusive).
        :return: A random floating point number.
        """
        return self.faker.pyfloat(min_value=start, max_value=end, right_digits=2)

    def amount(self) -> float:
        """
        Generates a random money amount.

        :return: An amount between 1 and 1000.
        """
        return self.float(1, 1000)

# Create an instance of the Fake class backed by Faker
fake = Fake(faker=Faker())
