# before building this, do:
#
#   $ npm shrinkwrap
#   $ ./node_modules/ember-cli/bin/ember build --env=production
#   $ node backend
#
# and check that everything is ok
FROM node:0.10.35

MAINTAINER Namlook <n.namlook@gmail.com>

ADD ./Brocfile.js /app/Brocfile.js
ADD ./app /app/app
ADD ./backend /app/backend
ADD ./bin /app/bin
ADD ./bower.json /app/bower.json
ADD ./bower_components /app/bower_components
ADD ./config /app/config
ADD ./dist /app/dist
ADD ./package.json /app/package.json
ADD ./public /app/public
ADD ./vendor /app/vendor

ADD ./npm-shrinkwrap.json /app/npm-shrinkwrap.json

WORKDIR /app

RUN npm install

EXPOSE 4000

ENV NODE_ENV production

CMD node backend