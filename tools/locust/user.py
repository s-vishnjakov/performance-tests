from locust import User, between

from config import settings


class LocustBaseUser(User):
    """
    The base virtual user for Locust, from which all scenarios are inherited.
    Contains general settings that can be overridden if necessary.
    """
    host = "localhost"
    abstract = True
    wait_time = between(
        min_wait=settings.locust_user.wait_time_min,
        max_wait=settings.locust_user.wait_time_max
    )
