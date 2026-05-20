from pydantic import BaseModel, Field


class GrafanaAlertValues(BaseModel):
    """Значения метрик алерта."""
    B: float | None = Field(None, description="Значение метрики B")
    C: float | None = Field(None, description="Значение метрики C")


class GrafanaAlert(BaseModel):
    """Модель отдельного алерта из Grafana."""
    status: str = Field(..., description="Статус алерта (firing/resolved)")
    labels: dict[str, str] = Field(default_factory=dict, description="Лейблы алерта")
    annotations: dict[str, str] = Field(default_factory=dict, description="Аннотации алерта")
    startsAt: str = Field(..., description="Время начала алерта")
    endsAt: str = Field(..., description="Время окончания алерта")
    generatorURL: str = Field("", description="URL генератора алерта")
    fingerprint: str = Field(..., description="Отпечаток алерта")
    silenceURL: str = Field("", description="URL для тишины")
    dashboardURL: str = Field("", description="URL дашборда")
    panelURL: str = Field("", description="URL панели")
    values: GrafanaAlertValues | None = Field(None, description="Значения метрик")


class GrafanaWebhookPayload(BaseModel):
    """Модель вебхука от Grafana Alerting."""
    receiver: str = Field(..., description="Имя получателя")
    status: str = Field(..., description="Общий статус (firing/resolved)")
    orgId: int = Field(..., description="ID организации")
    alerts: list[GrafanaAlert] = Field(..., description="Список алертов")
    groupLabels: dict[str, str] = Field(default_factory=dict, description="Групповые лейблы")
    commonLabels: dict[str, str] = Field(default_factory=dict, description="Общие лейблы")
    commonAnnotations: dict[str, str] = Field(default_factory=dict, description="Общие аннотации")
    externalURL: str = Field(..., description="Внешний URL Grafana")
    version: str = Field(..., description="Версия формата")
    groupKey: str = Field(..., description="Ключ группы")
    truncatedAlerts: int = Field(0, description="Количество усеченных алертов")
    title: str = Field(..., description="Заголовок группы алертов")
    state: str = Field(..., description="Состояние группы")
    message: str = Field("", description="Сообщение алерта")
