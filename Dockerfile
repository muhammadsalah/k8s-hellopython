FROM python:2.7.15-alpine3.8

WORKDIR /app

ADD index.py /app

CMD ["python","index.py"]
