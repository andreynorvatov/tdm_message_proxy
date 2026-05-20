import time

from pydantic import BaseModel, Field


def _generate_client_random_id() -> int:
    """Генерация уникального идентификатора на основе временной метки."""
    return int(time.time())


class TdmSendTextMessageRequest(BaseModel):
    """Модель запроса на отправку текстового сообщения в TDM."""

    clientRandomId: int = Field(
        default_factory=_generate_client_random_id,
        description="Уникальный идентификатор сообщения на стороне клиента",
    )
    message: str = Field(
        ...,
        description="Текст сообщения для отправки",
    )


class TdmSendTextMessageResponse(BaseModel):
    """Модель ответа на отправку текстового сообщения в TDM."""

    messageId: int = Field(
        ...,
        description="ID отправленного сообщения в TDM",
    )
