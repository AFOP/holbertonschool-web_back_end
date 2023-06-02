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
            Return: False
        """
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path is not None:
            if path[len(path) - 1] != '/':
                path += '/'
        if path is None:
            return True
        for excluded_path in excluded_paths:
            asterisk = excluded_path.find("*")
            if asterisk != -1 and len(path) >= len(excluded_path):
                pathcpy = path[: asterisk]
                if pathcpy == excluded_path[: asterisk]:
                    return False
            if path == excluded_path:
                return False
        return True

    def authorization_header(self, request) -> str:
        """
            Function authorization_header
            Return: None
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request) -> TypeVar('User'):
        """
            Function current_user
            Return: None
        """
        return None
