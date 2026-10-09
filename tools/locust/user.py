from locust import User, between

class LocustBaseUser(User):
    """
    The base virtual user for Locust, from which all scenarios are inherited.
    Contains general settings that can be overridden if necessary.
    """
    host = "localhost"
    abstract = True
    wait_time = between(1, 3)