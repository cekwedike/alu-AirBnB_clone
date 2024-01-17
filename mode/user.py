"""Defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    def __init__(self, *, email, password, first_name, last_name):
        """Initialize a new instance of the User class."""
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
