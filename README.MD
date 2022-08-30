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
from azauthpy import AzAuth

auth = AzAuth("https://example.com", "username", "password")

if auth.login():
    print("Logged in!")
else:
    print("Failed to login!")
```