FROM python:3.8.13

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD while ! python3 main.py --noinput ; do sleep 1 ; done
# while ! python3 manage.py migrate --noinput ; do sleep 1 ; done && \
