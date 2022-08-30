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

    """
    :class:`int`: Returns the id of the user
    """
    @property
    def id(self) -> int:
        return self.data['id']

    """
    :class:`str`: Returns the username of the user
    """
    @property
    def username(self) -> str:
        return self.data['username']

    """
    :class:`str`: Returns the uuid of the user
    """
    @property
    def uuid(self) -> str:
        return self.data['uuid']

    """
    :class:`bool`: Returns a boolean of whether the user's email is verified
    """
    @property
    def email_verified(self) -> bool:
        return self.data['email_verified']

    """
    :class:`float`: Returns the amount of money the user has
    """
    @property
    def money(self) -> float:
        return self.data['money']

    """
    :class:`Role`: Returns the role of the user
    """
    @property
    def role(self) -> Role:
        return Role(self.data['role']['id'], self.data['role']['name'], self.data['role']['color'])

    """
    :class:`bool`: Returns a boolean of whether the user is banned
    """
    @property
    def banned(self) -> bool:
        return self.data['banned']

    """
    :class:`datetime`: Returns the datetime of when the user was created
    """
    @property
    def created_at(self) -> datetime:
        return datetime.fromisoformat(self.data['created_at'])

    """
    :class:`bool`: Returns a boolean of whether the user is an admin
    """
    @property
    def access_token(self) -> str:
        return self.data['access_token']
