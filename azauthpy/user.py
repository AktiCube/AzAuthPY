from .role import Role
from datetime import datetime

class User(object):
    """
    An object to represent a user
    """
    def __init__(self, data: dict) -> None:
        self.data = data

    def __str__(self) -> str:
        return self.username
    
    def __repr__(self) -> str:
        return f"User(id={self.id}, username={self.username}, uuid={self.uuid}, email_verified={self.email_verified}, money={self.money}, role={self.role}, banned={self.banned}, created_at={self.created_at})"	

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, User):
            return self.id == __o.id
        return False

    @property
    def id(self) -> int:
        """
        :class:`int`: Returns the id of the user
        """
        return self.data['id']

    @property
    def username(self) -> str:
        """
        :class:`str`: Returns the username of the user
        """
        return self.data['username']

    @property
    def uuid(self) -> str:
        """
        :class:`str`: Returns the uuid of the user
        """
        return self.data['uuid']

    @property
    def email_verified(self) -> bool:
        """
        :class:`bool`: Returns a boolean of whether the user's email is verified
        """
        return self.data['email_verified']

    @property
    def money(self) -> float:
        """
        :class:`float`: Returns the amount of money the user has
        """
        return self.data['money']

    @property
    def role(self) -> Role:
        """
        :class:`Role`: Returns the role of the user
        """
        return Role(self.data['role']['id'], self.data['role']['name'], self.data['role']['color'])

    @property
    def banned(self) -> bool:
        """
        :class:`bool`: Returns a boolean of whether the user is banned
        """
        return self.data['banned']

    @property
    def created_at(self) -> datetime:
        """
        :class:`datetime`: Returns the datetime of when the user was created
        """
        return datetime.fromisoformat(self.data['created_at'])

    @property
    def access_token(self) -> str:
        """
        :class:`bool`: Returns a boolean of whether the user is an admin
        """
        return self.data['access_token']
