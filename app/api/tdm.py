from fastapi import APIRouter, HTTPException, status

from app.models.tdm import TdmSendTextMessageRequest, TdmSendTextMessageResponse
from app.services.tdm import tdm_service

router = APIRouter(prefix="/tdm", tags=["tdm"])


@router.post(
    "/messages/send_test_message",
    response_model=TdmSendTextMessageResponse,
    summary="Отправка текстового сообщения в TDM",
    description="Отправляет текстовое сообщение в TDM мессенджер через бота.",
)
async def send_text_message(
    request: TdmSendTextMessageRequest,
) -> TdmSendTextMessageResponse:
    """Отправка текстового сообщения в TDM мессенджер."""
    try:
        return await tdm_service.send_text_message(request)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Ошибка при отправке сообщения в TDM: {exc}",
        ) from exc
