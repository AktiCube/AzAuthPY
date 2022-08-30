from . import Role
from datetime import datetime

class User:
    def __init__(self, data: dict) -> None:
        self.data = data

    def __str__(self) -> str:
        return self.username
    
    def __repr__(self) -> str:
        return f"User(id={self.id}, username={self.username}, uuid={self.uuid}, email_verified={self.email_verified}, money={self.money}, role={self.role}, banned={self.banned}, created_at={self.created_at}"	

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, User):
            return self.id == __o.id
        return False

    @property
    def id(self) -> int:
        return self.data['id']

    @property
    def username(self) -> str:
        return self.data['username']
    
    @property
    def uuid(self) -> str:
        return self.data['uuid']
    
    @property
    def email_verified(self) -> bool:
        return self.data['email_verified']
    
    @property
    def money(self) -> float:
        return self.data['money']

    @property
    def role(self) -> Role:
        return Role(self.data['role']['id'], self.data['role']['name'], self.data['role']['color'])
    
    @property
    def banned(self) -> bool:
        return self.data['banned']
    
    @property
    def created_at(self) -> datetime:
        return datetime.fromisoformat(self.data['created_at'])

    @property
    def access_token(self) -> str:
        return self.data['access_token']
