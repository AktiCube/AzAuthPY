import requests
from aenum import enum
from .user import User

class LoginState(enum):
    """
    An enum to represent the current login state
    """
    SUCCESS = 0
    NEEDS_SECURE_CODE = 1
    FAILED = 2
    USER_BANNED = 3

class LoginResult(object):
    """
    An object to represent the result of a login attempt
    """
    def __init__(self, state: LoginState, user: User = None) -> None:
        self._state = state
        self._user = user

    @property
    def user(self) -> User:
        """
        :class:`User`: Returns the User object representing the user that logged in
        """
        return self._user

    @property
    def status(self) -> LoginState:
        """
        :class:`LoginState`: Returns the current login state
        """
        return self._state

class AzAuth:
    """
    The main class of this library
    It is used to login, verify and logout users
    """
    def __init__(self, url: str) -> None:
        self.baseurl = f"{url}/api/auth"

    def login(self, email: str, password: str, code: int = None) -> LoginResult:
        """
        :class:`LoginResult`: Logs in a user
        """
        request = requests.post(self.baseurl + '/authenticate', data={ 'email': email, 'password': password, 'code': code })
        result = request.json()
        if request.status_code == 200:
            return LoginResult(LoginState.SUCCESS, User(result))
        else:
            if result['status'] == 'pending' and result['reason'] == '2fa':
                return LoginResult(LoginState.NEEDS_SECURE_CODE)
            elif result['status'] == 'error' and result['reason'] == 'user_banned':
                return LoginResult(LoginState.USER_BANNED)
            else:
                return LoginResult(LoginState.FAILED)

    def verify(self, access_token: str) -> User:
        """
        :class:`User`: Returns the User object of the user with the given access token
        """
        request = requests.post(self.baseurl + '/verify', data={ 'access_token': access_token })
        result = request.json()
        if request.status_code == 200:
            return User(result)
        else:
            return None

    def logout(self, access_token: str) -> bool:
        """
        :class:`bool`: Returns a boolean of whether the logout was successful with the given access token
        """
        request = requests.post(self.baseurl + '/logout', data={ 'access_token': access_token })
        return request.status_code == 200
