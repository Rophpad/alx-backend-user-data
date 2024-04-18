#!/usr/bin/env python3
""" Session Authentification
"""
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ Class to handle
        Session authentification
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for user_id
        """
        if (not user_id) or (not isinstance(user_id, str)):
            return None
        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)

    def user_id_for_session_id(
            self,
            session_id: str = None
    ) -> str:
        """ Retrieve User ID based on a Session ID
        """
        if (not session_id) or (not isinstance(session_id, str)):
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id
