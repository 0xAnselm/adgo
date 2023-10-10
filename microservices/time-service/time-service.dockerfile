# build a tiny docker image
FROM alpine:latest

RUN mkdir /app

COPY timeApp /app

CMD [ "/app/timeApp" ]