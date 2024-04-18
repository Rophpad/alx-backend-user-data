#!/usr/bin/env python3
""" API Authentification
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """ Class to manage
        API authentification
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Handle authentification requirements
        """
        # if path and path[-1] != '/':
        #   path = path + '/'
        if (not path) or (not excluded_paths) or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Handle authentification header
        """
        header = request.headers.get('Authorization')
        if (not header):
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current User request ...
        """
        return None

    def session_cookie(self, request=None):
        """ Gets from a request, cookie value
        """
        if not request:
            return None
        return request.cookies.get(os.getenv('SESSION_NAME'))
