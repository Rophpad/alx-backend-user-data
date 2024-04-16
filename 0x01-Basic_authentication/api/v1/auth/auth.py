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
        return False

    def authorization_header(self, request=None) -> str:
        """ Handle authentification header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User request ...
        """
        return None
