#
# Don't forget to build ember for production before building this image:
#
#    ember build --env=production
#
FROM node:0.12.2

MAINTAINER Namlook <n.namlook@gmail.com>

RUN apt-get update -y && apt-get upgrade -y && apt-get install graphicsmagick phylip libc6-i386 r-base r-base-dev -y && apt-get clean
RUN wget https://cran.r-project.org/src/contrib/ape_3.3.tar.gz
RUN wget https://cran.r-project.org/src/contrib/RSvgDevice_0.6.4.4.tar.gz
RUN R CMD INSTALL ape_3.3.tar.gz
RUN R CMD INSTALL RSvgDevice_0.6.4.4.tar.gz
RUN npm install -g bower

ADD ./package.json /app/package.json
ADD ./bower.json /app/bower.json
# ADD ./bower_components /app/bower_components
ADD ./ember-cli-build.js /app/ember-cli-build.js

ADD ./app /app/app
ADD ./dist /app/dist
ADD ./backend /app/backend
ADD ./config /app/config
ADD ./public /app/public

# add more files here if you need it
ADD ./bin /app/bin
ADD ./secret.json /app/secret.json

WORKDIR /app

ENV NODE_ENV production

# RUN npm install -g ember-cli@`grep '"ember-cli"' package.json |cut -d '"' -f 4 |tr -d '^'`
# RUN ember install
RUN npm install
RUN bower --allow-root install

EXPOSE 80

CMD node backend