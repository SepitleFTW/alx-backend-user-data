#!/usr/bin/env python3
"""
auth tings bruhv
"""
from flask import Flask, request


class Auth:
    """class for authentication
    """

    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """
        auth tings
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

    def authorization_header(self, request=None) -> str:
        """authentication tings mahn
        """
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar(user):
        """
        the current user lmao
        """
        request = Flask(__name__)
        return None
