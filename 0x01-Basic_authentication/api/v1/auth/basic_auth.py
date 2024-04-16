#!/usr/bin/env python3
""" Basic Authentification
"""

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
        """ Get the docoded value of a Base64 string
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
