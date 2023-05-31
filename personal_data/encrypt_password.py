#!/usr/bin/env python3
"""
    Encript password
"""


import bcrypt

def hash_password(password):
    """ hash password """
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
