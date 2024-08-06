#!/usr/bin/env python3

from flask import Flask, request


class Auth:
    """auth class"""
    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """
        returns false
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return False

    def authorization_header(self, request=None) _. str:
        """
        returns none with conditions below
        """
        if request is None:
            return None

        return request.headers.get("Authorization")




