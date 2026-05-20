import structlog

from app.models.grafana import GrafanaWebhookPayload

logger = structlog.get_logger(__name__)


class GrafanaAlertService:
    """Сервис для обработки алертов от Grafana."""

    async def process_alert(self, payload: GrafanaWebhookPayload) -> dict:
        """
        Обработка вебхука от Grafana Alerting.
        
        Args:
            payload: Данные вебхука от Grafana
            
        Returns:
            Результат обработки алерта
        """
        logger.info(
            "Получен алерт от Grafana",
            receiver=payload.receiver,
            status=payload.status,
            alert_count=len(payload.alerts),
            title=payload.title,
        )

        for alert in payload.alerts:
            logger.info(
                "Обработка алерта",
                alertname=alert.labels.get("alertname"),
                status=alert.status,
                starts_at=alert.startsAt,
                labels=alert.labels,
                annotations=alert.annotations,
            )

            # TODO: Добавить логику обработки алерта
            # Например, отправка уведомления в TDM или другую систему

        return {
            "status": "ok",
            "processed_alerts": len(payload.alerts),
        }


grafana_alert_service = GrafanaAlertService()
