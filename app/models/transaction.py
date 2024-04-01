from datetime import datetime
from enum import Enum

class TransactionType(Enum):
    CREDIT = 'credit'
    DEBIT = 'debit'

class Transaction:
    def __init__(self, transaction_id: int, user_id: int, amount: float, transaction_type: TransactionType, timestamp: datetime):
        self._transaction_id = transaction_id
        self._user_id = user_id
        self._amount = amount
        self._transaction_type = transaction_type
        self._timestamp = timestamp

    def get_transaction_id(self) -> int:
        return self._transaction_id

    def get_user_id(self) -> int:
        return self._user_id

    def get_amount(self) -> float:
        return self._amount

    def get_transaction_type(self) -> TransactionType:
        return self._transaction_type

    def get_timestamp(self) -> datetime:
        return self._timestamp