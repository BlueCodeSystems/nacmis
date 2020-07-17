FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
        apt-get install -yq python3-dev \
        libsasl2-dev \
        && apt-get clean
RUN mkdir /src
WORKDIR /src
COPY . nacmis/
RUN pip install -r nacmis/requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

