"""Module to generate random users"""
from faker import Faker
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / "user.log", level=logging.WARNING)

fake = Faker()


def get_user():
    """Generate a single user

    Returns:
        str: user
    """
    logging.info("Generating user.")
    return fake.name()


def get_users(n):
    """

    Args:
        n (int): Number of user

    Returns:
        list[str]: users
    """
    logging.info(f"Generating a list of {n} user.")
    return [get_user() for _ in range(n)]


if __name__ == "__main__":
    print(get_user())
    print(get_users(10))