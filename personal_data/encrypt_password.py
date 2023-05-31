#!/usr/bin/env python3
"""
    Encript password
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """ hash password """
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Check if the provided password matches the hashed password """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
