#!/usr/bin/env python3
"""
define a hash password method
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    password hashing method
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

class Auth:
    """Auth class to interact with the authentication database
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        adding new user to the database
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))
