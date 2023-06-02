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
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path.endswith('/'):
            path = path[:-1]
        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                excluded_path = excluded_path[:-1]
            if path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
            Function authorization_header
            Return: None
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Function current_user
            Return: None
        """
        return None
