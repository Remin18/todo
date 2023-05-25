FROM python:3.12.0b1-buster as builder
ENV PYTHONUNBUFFERED=1
RUN mkdir app
WORKDIR /app
RUN mkdir src
COPY . /app/src/

RUN pip install --upgrade pip
RUN pip install -r ./src/requirements.txt

FROM python:3.12.0b1-slim-buster
ENV PYTHONUNBUFFERED=1
RUN mkdir app
WORKDIR /app
RUN mkdir -p tmp/sockets

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get -y install mariadb-client sqlite3

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /app /app
