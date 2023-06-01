#!/usr/bin/env python3
""" File auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class auth"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Function require_auth
            Return: Fase
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
            Function authorization_header
            Return: None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Function current_user
            Return: None
        """
        return None
