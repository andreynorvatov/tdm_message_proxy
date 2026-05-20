import httpx
import structlog

from app.config import settings
from app.models.tdm import TdmSendTextMessageRequest, TdmSendTextMessageResponse

logger = structlog.get_logger(__name__)


class TdmService:
    """Сервис для взаимодействия с TDM API."""

    def __init__(self) -> None:
        self._base_url = settings.TDM_API_URL.rstrip("/")
        self._bot_id = settings.NT_BOT_TDM_ID
        self._chat_id = settings.NT_BOT_TDM_CHAT_ID
        self._auth_token = settings.NT_BOT_TDM_AUTH_TOKEN

    def _get_headers(self) -> dict[str, str]:
        return {
            "Authorization": self._auth_token,
            "Content-Type": "application/json",
        }

    def _get_send_text_message_url(self) -> str:
        return f"{self._base_url}/{self._bot_id}/{self._chat_id}"

    async def send_text_message(
        self, request: TdmSendTextMessageRequest
    ) -> TdmSendTextMessageResponse:
        """Отправка текстового сообщения в TDM мессенджер.

        Args:
            request: Модель запроса с clientRandomId и текстом сообщения.

        Returns:
            Модель ответа от TDM API.

        Raises:
            httpx.HTTPStatusError: При получении ошибочного HTTP-статуса.
            httpx.RequestError: При ошибке сети.
        """
        url = self._get_send_text_message_url()
        headers = self._get_headers()
        payload = request.model_dump()

        logger.info(
            "Sending text message to TDM",
            url=url,
            client_random_id=request.clientRandomId,
        )

        async with httpx.AsyncClient() as client:
            response = await client.post(
                url,
                json=payload,
                headers=headers,
                timeout=30.0,
            )
            response.raise_for_status()

        response_data = response.json()
        logger.info(
            "TDM message sent successfully",
            status=response_data.get("status"),
        )

        return TdmSendTextMessageResponse(**response_data)


tdm_service = TdmService()
