import time

from pydantic import BaseModel, Field, model_validator


def _generate_client_random_id() -> int:
    """Генерация уникального идентификатора на основе временной метки."""
    return int(time.time())


class TdmSendTextMessageRequest(BaseModel):
    """Модель запроса на отправку текстового сообщения в TDM."""

    clientRandomId: int = Field(
        default=0,
        description="Уникальный идентификатор сообщения на стороне клиента",
    )

    @model_validator(mode="after")
    def set_client_random_id(self) -> "TdmSendTextMessageRequest":
        """Устанавливает clientRandomId, если он не был передан (равен 0)."""
        if self.clientRandomId == 0:
            self.clientRandomId = _generate_client_random_id()
        return self
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
