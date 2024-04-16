#!/usr/bin/env python3
""" Basic Authentification
"""

from typing import TypeVar
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ class for Basic Authentification
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str
    ) -> str:
        """ Get encoded header
        """
        if (not authorization_header)\
           or (not isinstance(authorization_header, str))\
           or (authorization_header[0:6] != "Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
    ) -> str:
        """ Get the decoded value of a Base64 string
        """
        b64_auth = base64_authorization_header
        if (not b64_auth)\
           or (not isinstance(b64_auth, str)):
            return None
        try:
            to_decode = b64_auth.encode('utf-8')
            decoded = base64.b64decode(to_decode)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
    ) -> (str, str):
        """ Gets user credentials
        """
        decoded_b64_auth = decoded_base64_authorization_header
        if (not decoded_b64_auth)\
           or (not isinstance(decoded_b64_auth, str))\
           or (':' not in decoded_b64_auth):
            return (None, None)
        email, password = decoded_b64_auth.split(':')
        return (email, password)

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
    ) -> TypeVar('User'):
        """ Gets User instance based on his email
            and password
        """
        if (not user_email) or (not isinstance(user_email, str))\
           or (not user_pwd) or (not isinstance(user_pwd, str)):
            return None
        try:
            users = User.search({"email": user_email})
            if not users or len(users) == 0:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves User instance for a request
        """
        auth_header = self.authorization_header(request)
        if auth_header is not None:
            token = self.extract_base64_authorization_header(auth_header)
            if token is not None:
                decoded = self.decode_base64_authorization_header(token)
                if decoded is not None:
                    email, password = self.extract_user_credentials(decoded)
                    if email is not None:
                        return self.user_object_from_credentials(
                                email, password)
        return
