FROM nginx:stable-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/ngix/conf.d

WORKDIR /usr/src/app

EXPOSE 80