import structlog
from fastapi import APIRouter, HTTPException, status

from app.models.tdm import TdmSendTextMessageRequest, TdmSendTextMessageResponse
from app.services.tdm import tdm_service

logger = structlog.get_logger(__name__)

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
    logger.info(
        "Получен запрос на отправку сообщения",
        client_random_id=request.clientRandomId,
    )
    try:
        result = await tdm_service.send_text_message(request)
        logger.info(
            "Сообщение успешно отправлено",
            client_random_id=request.clientRandomId,
        )
        return result
    except HTTPException:
        raise
    except Exception as exc:
        logger.error(
            "Ошибка при отправке сообщения в TDM",
            client_random_id=request.clientRandomId,
            error=str(exc),
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Ошибка при отправке сообщения в TDM: {exc}",
        ) from exc
