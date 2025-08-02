# DiaLog

_Версия: **1.0**_

В этом репозитории вы можете ознакомиться с кодом веб-приложения для людей с сахарным диабетом

## Основные функции

Ниже перечислены основные функции, которые предоставляет проект

- контроль за диабетом
- ведение дневника заболевания
- составление отчетов 
- удобный просмотр внесенных данных в удобном визуальном формате (графики, диаграммы, таблицы)
- выгрузка отчетов в различные форматы (pdf, excel)

## Преимущества

- полностью бесплатное
- без рекламы
- не нужно качать лишних приложений на телефон: веб-приложение доступно из браузера с любого устройства
- возможность заносить множество различных данных о состоянии организма
- наглядное представление внесенных данных в удобном для восприятия формате
- возможность показать свои данные врачу

## Запуск проекта

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

# jwt
AUTH_COOKIE_SECURE=
```
- запустить сборку docker-контейнеров `docker compose build`
- далее запустите команду `docker compose up`
- готово

### Запуск nginx
- в `/etc/hosts` добавить:
```text
<IP-адрес> dialog.com
```
- в отдельном контейнере необходимо создать файлы `site.conf` (скопировать туда содержимое файла из этого репозитория) и файл `docker-compose.yaml` со следующим содержимым:

```yaml
services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./site.conf:/etc/nginx/conf.d/site.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    extra_hosts:
      - "dialog.com:host-gateway"
    networks:
      - dialog_network

networks:
  dialog_network:
    external: true
```

- В папке с конфигурацией nginx создать папку `ssl/`
- Сгенерировать сертификат, например, следующей командой (на Windows):
```bash
mkcert -cert-file ssl/dialog.crt -key-file ssl/dialog.key dialog.com
```

Предварительно надо установить `mkcert` следующим образом:
- В PowerShell от имени администратора установить `Chocolatey`
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
- Установить сам `mkcert`
```powershell
choco install mkcert 
```

### Особенности проекта

Серверная часть (backend) написана на **Python/Django**, API реализован с помощью **Django REST Framework**  
На данный момент полноценной frontend-части нет, сейчас используются **Django Templates**, часть данных отправляются клиенту асинхронно через **AJAX** с помощью fetch-запросов  
На данный момент используется стандартная аутентификация django - **SessionAuthentication**, со временем она будет перенесена на **JWT**, часть логики уже перенесена на нее  
**Redis** - для кеширования  
**RabbitMQ** - брокер сообщений  
**Celery Beat** - планировщик задач
Используемая СУБД - **PostgreSQL**

### Настройка celery

По умолчанию, все должно работать из коробки.

Для команд создания ежемесячных, ежедневных и еженедельных отчетов нужно в django-админке создать периодические таски, все их связать с каким-либо кроном (в зависимости от того, когда нужно запускать таски)

Flower будет доступен по локальному адресу `http://127.0.0.1:5555`
RabbitMQ будет доступен в по локальному адресу `http://127.0.0.1:15672` с логином и паролем - guest
