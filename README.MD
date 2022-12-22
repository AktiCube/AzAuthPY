# AzAuthPY
A Python implementation of the Azuriom Auth API.

## Installation
```bash
pip install git+https://github.com/AktiCube/AzAuthPY.git
```

## Uninstallation
```bash
pip uninstall azauthpy
```

## Usage
```python
from azauthpy import AzAuth, LoginState, User

def login(email: str, password: str) -> User:
    client = AzAuth('https://www.akticube.fr')

    result = client.login(email, password)

    if result.status == LoginState.NEEDS_SECURE_CODE:
        code = input('Please enter your 2FA Code: ')
        result = client.login(email, password, code)

    if result.status == LoginState.SUCCESS:
        print(f"Welcome {result.user.username}!")
        return result.user
    elif result.status == LoginState.USER_BANNED:
        print('You are banned!')
        return None
    else:
        print("Login failed!")
        return None
```
