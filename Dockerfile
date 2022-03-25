# UpMarket
# Version: 1.0
FROM python:3.10.3

RUN mkdir -p /upmarket

COPY ./back/ /upmarket/

WORKDIR /up_market

RUN  pip3 install -r requirements.txt

RUN ["chmod", "+x", "/opt/upmarket/docker-entrypoint.sh"]

ENTRYPOINT ["/opt/upmarket/docker-entrypoint-dev.sh"]
