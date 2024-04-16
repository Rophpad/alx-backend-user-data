#!/usr/bin/env python3
""" API Authentification
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage
        API authentification
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Handle authentification requirements
        """
        if path and path[-1] != '/':
            path = path + '/'
        if (not path) or (not excluded_paths) or path not in excluded_paths:
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """ Handle authentification header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User request ...
        """
        return None
