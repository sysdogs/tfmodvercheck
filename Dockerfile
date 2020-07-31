FROM python:3.8.5-alpine3.12

ENV DIRECTORY /tf

VOLUME /tf

COPY entrypoint.sh /entrypoint.sh
COPY main.py /main.py

ENTRYPOINT ["/entrypoint.sh"]