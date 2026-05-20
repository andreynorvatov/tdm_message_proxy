from pydantic import BaseModel, Field


class TdmSendTextMessageRequest(BaseModel):
    """Модель запроса на отправку текстового сообщения в TDM."""

    clientRandomId: int = Field(
        ...,
        description="Уникальный идентификатор сообщения на стороне клиента",
    )
    message: str = Field(
        ...,
        description="Текст сообщения для отправки",
    )


class TdmSendTextMessageResponse(BaseModel):
    """Модель ответа на отправку текстового сообщения в TDM."""

    status: str = Field(
        ...,
        description="Статус ответа (например, 'ok' или 'error')",
    )
    message: str | None = Field(
        default=None,
        description="Дополнительное сообщение от сервера",
    )
