# dia_log

Веб-приложение для контроля за диабетом. Позволяет вести дневник о протекании болезни, наглядно просматривать изменения в самочувствии, которые наглядно отображаются в графиках.

# Запуск проекта

- В `dialog_backend/dialog_backend/` создайте `.env` файл со следующим содержимым:
```dotenv
# django project settings
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=
LANGUAGE_CODE=
TIME_ZONE=

# postgres config
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=

# redis config
REDIS_HOST=
REDIS_PORT=
```
- далее запустите команду `docker compose up`
- готово

### Настройка celery

Для команд создания ежемесячных, ежедневных и еженедельных отчетов нужно в django-админке создать периодические таски, все их связать с каким-либо кроном (в зависимости от того, когда нужно запускать таски)
