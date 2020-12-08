FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY python-flask-server/requirements.txt /usr/src/app/

RUN pip install --no-cache-dir nltk requests html2text numpy

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

WORKDIR /usr/src/app/python-flask-server/
ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]

