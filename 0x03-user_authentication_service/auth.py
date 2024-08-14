#!/usr/bin/env python3
"""
define a hash password method
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    password hashing method
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
