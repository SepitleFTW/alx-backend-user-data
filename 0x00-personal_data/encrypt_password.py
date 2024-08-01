#!/usr/bin/env python3
"""encrypting pswds
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hashing pswd using random salt
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """if hash pswd is valid
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
