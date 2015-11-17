#
# Don't forget to build ember for production before building this image:
#
#    ember build --env=production
#
FROM node:0.12.2

MAINTAINER Namlook <n.namlook@gmail.com>

RUN apt-get update && apt-get install -y \
        graphicsmagick \
        phylip \
        libc6-i386 \
        r-base \
        r-base-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://cran.r-project.org/src/contrib/ape_3.3.tar.gz \
 && wget https://cran.r-project.org/src/contrib/RSvgDevice_0.6.4.4.tar.gz \
 && R CMD INSTALL ape_3.3.tar.gz \
 && R CMD INSTALL RSvgDevice_0.6.4.4.tar.gz

ADD ./package.json /app/package.json
ADD ./bower.json /app/bower.json
ADD ./ember-cli-build.js /app/ember-cli-build.js
ADD ./app /app/app
ADD ./dist /app/dist
ADD ./backend /app/backend
ADD ./config /app/config
ADD ./public /app/public

# add more files here if you need it
ADD ./bin /app/bin
ADD ./config/secret.json /app/config/secret.json

WORKDIR /app

ENV NODE_ENV production

RUN npm install && npm install -g bower && bower --allow-root install

EXPOSE 80

CMD ["node", "backend"]
