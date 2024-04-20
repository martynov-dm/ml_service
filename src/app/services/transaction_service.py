from ast import List
from app.models.transaction import Transaction, TransactionType


class TransactionService:
    def __init__(self, transaction_repository):
        self._transaction_repository = transaction_repository

    def create_transaction(self, user_id: int, amount: float, transaction_type: TransactionType) -> Transaction:
        # Логика создания новой транзакции
        pass

    def get_transactions_by_user_id(self, user_id: int) -> List[Transaction]:
        # Логика получения списка транзакций пользователя
        pass