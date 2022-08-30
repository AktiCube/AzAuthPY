import requests
from aenum import enum
from .user import User

class LoginState(enum):
    SUCCESS = 0
    NEEDS_SECURE_CODE = 1
    FAILED = 2

class LoginResult(object):
    def __init__(self, state: LoginState, user: User = None) -> None:
        self._state = state
        self._user = user

    @property
    def user(self) -> User:
        return self._user

    @property
    def status(self) -> LoginState:
        return self._state

class AzAuth:
    def __init__(self, url: str) -> None:
        self.baseurl = f"{url}/api/auth"

    def login(self, email: str, password: str, code: int = None) -> LoginResult:
        request = requests.post(self.baseurl + '/authenticate', data={ 'email': email, 'password': password, 'code': code })
        result = request.json()
        if request.status_code == 200:
            return LoginResult(LoginState.SUCCESS, User(result))
        else:
            if result['status'] == 'pending' and result['reason'] == '2fa':
                return LoginResult(LoginState.NEEDS_SECURE_CODE)
            else:
                return LoginResult(LoginState.FAILED)

    def verify(self, access_token: str) -> User:
        request = requests.post(self.baseurl + '/verify', data={ 'access_token': access_token })
        result = request.json()
        if request.status_code == 200:
            return User(result)
        else:
            return None
