#!/usr/bin/env python3
"""
Auth module for handling authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class for authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine if the given path requires authentication.
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        if path[-1] == '/':
            path = path[:-1]

        for excluded_path in excluded_paths:
            if excluded_path[-1] == '/':
                excluded_path = excluded_path[:-1]

            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False

            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Return the Authorization header from the request if present"""
        if request is None:
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder method for returning the current user.
        """
        return None
