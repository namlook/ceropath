FROM node:0.10.35

MAINTAINER Namlook <n.namlook@gmail.com>

ADD ./package.json /app/package.json
ADD ./bower.json /app/bower.json
ADD ./bower_components /app/bower_components
ADD ./Brocfile.js /app/Brocfile.js

ADD ./app /app/app
ADD ./dist /app/dist
ADD ./backend /app/backend
ADD ./config /app/config
ADD ./public /app/public

# add more files here if you need it
ADD ./bin /app/bin

WORKDIR /app

ENV NODE_ENV production

RUN npm install

# RUN npm install -g ember-cli@`grep '"ember-cli"' package.json |cut -d '"' -f 4 |tr -d '^'`
# RUN ember build --env=production

EXPOSE 80

CMD node backend