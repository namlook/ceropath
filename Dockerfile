FROM node:0.10.35

MAINTAINER Namlook <n.namlook@gmail.com>

ADD ./package.json /app/package.json
ADD ./bower.json /app/bower.json
ADD ./bower_components /app/bower_components
ADD ./Brocfile.js /app/Brocfile.js

ADD ./app /app/app
ADD ./backend /app/backend
ADD ./config /app/config
ADD ./dist /app/dist
ADD ./public /app/public
ADD ./vendor /app/vendor

# add more files here if you need it
ADD ./bin /app/bin


WORKDIR /app

RUN npm install

ENV NODE_ENV production

RUN ./node_modules/ember-cli/bin/ember build --env=production

EXPOSE 80

CMD node backend