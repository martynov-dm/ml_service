from app.external.video_api_client import VideoAPIClient
from app.models.transaction import TransactionType
from app.services.transaction_service import TransactionService


class InsufficientBalanceError(Exception):
    """
    Исключение, указывающее на недостаточный баланс пользователя для выполнения операции.
    """
    def __init__(self, message: str, user_id: int, balance: float, required_balance: float):
        self.message = message
        self.user_id = user_id
        self.balance = balance
        self.required_balance = required_balance
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: User ID - {self.user_id}, Balance - {self.balance}, Required Balance - {self.required_balance}"

class VideoService:
    def __init__(self, video_api_client: VideoAPIClient, transaction_service: TransactionService):
        self._video_api_client = video_api_client
        self._transaction_service = transaction_service

    def generate_video(self, user_id: int, prompt: str) -> str:
        user = self._user_repository.get_user_by_id(user_id)
        balance = user.get_balance()
        required_balance = 1

        if balance >= required_balance:
            video_url = self._video_api_client.generate_video(prompt)
            self._transaction_service.create_transaction(user_id, required_balance, TransactionType.DEBIT)
            return video_url
        else:
            raise InsufficientBalanceError("Insufficient balance to generate video", user_id, balance, required_balance)