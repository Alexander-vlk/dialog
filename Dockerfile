FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

WORKDIR /app 

COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir
COPY /dialog_backend/ /app 

CMD ["gunicorn", "dialog_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
