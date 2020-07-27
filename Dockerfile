FROM python:3.7-buster

ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y gcc python3-dev libsasl2-dev libffi-dev libpq-dev git && rm -rf /var/lib/apt/lists/*
RUN mkdir /src
WORKDIR /src
COPY . nacmis/
RUN pip install -r nacmis/requirements.txt

EXPOSE 8000
CMD ["python", "nacmis/manage.py", "runserver", "0.0.0.0:8000"]

