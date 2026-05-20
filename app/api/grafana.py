import structlog
from fastapi import APIRouter, HTTPException, status

from app.models.grafana import GrafanaWebhookPayload
from app.services.grafana import grafana_alert_service

logger = structlog.get_logger(__name__)

router = APIRouter(prefix="/grafana", tags=["grafana"])


@router.post(
    "/webhook",
    status_code=status.HTTP_200_OK,
    summary="Прием алертов от Grafana",
    description="Эндпоинт для получения вебхуков от Grafana Alerting.",
)
async def receive_grafana_alert(
    payload: GrafanaWebhookPayload,
) -> dict:
    """
    Обработка вебхука от Grafana Alerting.
    
    Принимает данные алертов от Grafana и обрабатывает их.
    """
    logger.info(
        "Получен вебхук от Grafana",
        receiver=payload.receiver,
        status=payload.status,
        alert_count=len(payload.alerts),
    )
    try:
        result = await grafana_alert_service.process_alert(payload)
        logger.info(
            "Алерт успешно обработан",
            result=result,
        )
        return result
    except HTTPException:
        raise
    except Exception as exc:
        logger.error(
            "Ошибка при обработке алерта Grafana",
            error=str(exc),
            exc_info=True,
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ошибка при обработке алерта: {exc}",
        ) from exc
