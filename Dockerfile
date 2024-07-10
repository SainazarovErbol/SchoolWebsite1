FROM python:3.10-alpine

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

COPY entypoint.sh /entypoint.sh

RUN chmod +x /entypoint.sh

ENTRYPOINT ["sh", "/entypoint.sh"]