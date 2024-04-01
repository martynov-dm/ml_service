class User:
    def __init__(self, user_id: int, username: str, email: str, password: str, balance: float, api_key: str = None):
        self._user_id = user_id
        self._username = username
        self._email = email
        self._password = password
        self._balance = balance
        self._api_key = api_key

    def get_user_id(self) -> int:
        return self._user_id

    def get_username(self) -> str:
        return self._username

    def get_email(self) -> str:
        return self._email

    def get_balance(self) -> float:
        return self._balance

    def set_balance(self, balance: float):
        self._balance = balance

    def get_api_key(self) -> str:
        return self._api_key

    def set_api_key(self, api_key: str):
        self._api_key = api_key