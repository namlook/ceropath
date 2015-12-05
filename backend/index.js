
var eureka = require('eurekajs');
var config = require('../config/server');
var mimes = require('mime-types');

var _ = require('lodash');
var joi = require('joi');

var eurekaServer = eureka(config);

eurekaServer.beforeRegister = function(_server, next) {
    _server.on('log', function(message) {
        console.log(message.tags, message.data);
    });
    next(null);
};

eurekaServer.start().then(function(server) {

    var uploadSecretKey = config.app.secret;

    server.route({
        path: '/_private/resources',
        method: 'GET',
        config: {
            validate: {
                query: {
                    'persist': joi.string()
                }
            }
        },
        handler: function(request, reply) {
            var persist = request.query.persist;
            return reply.ok({
                resources: Object.keys(request.db.registeredModels)
            });
        }
    }),

    server.route({
        path: '/_private/upload/{resource}',
        method: 'POST',
        config: {
            validate: {
                query: {
                    persist: joi.string(),
                    delimiter: joi.string().default(','),
                    escapeChar: joi.string(),
                    enclosedChar: joi.string()
                }
            },
            payload: {
                output: 'stream',
                parse: true,
                maxBytes: Math.pow(1024, 10),
                allow: 'multipart/form-data'
            }
        },
        handler: function(request, reply) {
            var persist = request.query.persist;
            var csvOptions = {
                delimiter: request.query.delimiter,
                escapeChar: request.query.escapeChar,
                enclosedChar: request.query.enclosedChar
            };
            var resource = request.params.resource;
            var modelName = _.capitalize(_.camelCase(request.params.resource));
            var db = request.db;
            if (!db[modelName]) {
                return reply.badRequest('unknown resource: "' + resource + '"');
            }
            var clearDb;
            if (persist) {
                if (persist !== uploadSecretKey) {
                    return reply.forbidden('not authorized');
                }
                clearDb = db.clearResource(modelName);
            } else {
                clearDb = Promise.resolve();
            }

            var file = request.payload.file;

            if (!file || !file.hapi) {
                return reply.badRequest('file not found');
            }

            var mimeType = mimes.lookup(file.hapi.filename);

            if (mimeType !== 'text/csv') {
                return reply.badRequest('the file should be in csv format');
            }

            clearDb.then(function() {

                var promise = new Promise(function(resolve, reject) {

                    var csvStream = db.csvStreamParse(modelName, file, csvOptions);
                    var writableStream = db.writableStream(modelName, {dryRun: !persist, stripUnknown: true});
                    csvStream.pipe(writableStream);

                    csvStream.on('error', function(err) {
                        // console.error('xxx', err);
                        reject(err);
                    });

                    writableStream.on('error', function(err) {
                        // console.error('---', err);
                        reject(err);
                    });

                    writableStream.on('end', function() {
                        // console.log('finished');
                        resolve();
                    });

                    request.payload.file.on('error', function(err) {
                        // console.error('***', err);
                        reject(err);
                    });
                });

                promise.then(function() {
                    reply.jsonApi({data: {sucess: true}});
                }).catch(function(err) {
                    if (err.message === 'Bad value') {
                        var lineNumber = parseFloat(err.line.count) + 1;
                        return reply.badRequest('error at line ' + lineNumber, err);
                    } else {
                        return reply.badRequest(err.message, err);
                    }

                });

            }).catch(function(err) {
                reply.badImplementation(err);
            });

        }
    });


    server.log('info', 'Server running at: http://' + server.info.address + ':' + server.info.port);
}).catch(function(error) {
    console.log(error);
    console.log(error.stack);
    throw error;
});