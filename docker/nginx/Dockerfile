FROM nginx:latest
LABEL MAINTAINER='Weslley Costa' 

RUN apk --update add nginx \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && mkdir /etc/nginx/sites-enabled/ \
    && mkdir -p /run/nginx \
    && rm -rf /etc/nginx/conf.d/default.conf \
    && rm -rf /var/cache/apk/*

    
COPY docker/nginx/app.conf /etc/nginx/conf.d/app.conf

# CMD ['nginx', '-g', 'daemon off;']