# dia_log

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
