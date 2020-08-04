FROM python:3.7-buster

ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y gcc python3-dev libsasl2-dev libffi-dev libpq-dev git && rm -rf /var/lib/apt/lists/*
RUN mkdir /src
WORKDIR /src
COPY . nacmis/
WORKDIR /src/nacmis
ENV PYTHONPATH="/:$PYTHONPATH"
RUN pip install --no-cache-dir -r requirements.txt
ENV DJANGO_SETTINGS_MODULE=nacmis_online.settings

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

