/* jshint node: true */

var pkg = require('../package.json');

// var nodemailerStubTransport = require('nodemailer-stub-transport');
var requireDir = require('require-dir');


var internals = {
    port: 8888,
    uploadDirectory: './uploads',
    endpoint: 'http://192.168.99.100:8890/sparql' // virtuoso
    // endpoint: 'http://192.168.99.100:9999/bigdata/sparql'; // blazegraph
};

if (process.env.NODE_ENV === 'production') {
    var dbHost = process.env.DB_PORT_8890_TCP_ADDR; // docker uses this
    var dbPort = process.env.DB_PORT_8890_TCP_PORT;

    if (!dbHost || !dbPort) {
        throw Error('host or port unknown');
    }

    internals.endpoint = 'http://' + dbHost + ':' + dbPort + '/sparql';
    internals.port = 80;
    internals.uploadDirectory = '/app/uploads';
}

var secretInfos = require('../secret.json');

module.exports = {
    name: pkg.name,
    host: '0.0.0.0',
    port: internals.port,
    app: {
        secret: secretInfos.secret,
        email: secretInfos.email,
        clientRootUrl: 'http://rdbsea.ceropath.org',
        apiRootPrefix: '/api/1'
    },
    resources: requireDir('../backend/resources'),
    publicDirectory: 'dist',
    fileUploads: {
        uploadDirectory: internals.uploadDirectory,
        maxBytes: 50 // 50 MB
    },
    log: ['warn'],
    database: {
        config: {
            graphUri: 'http://ceropath.org',
            endpoint: internals.endpoint
            // endpoint: 'http://192.168.99.100:8890/sparql' // virtuoso
            // endpoint: 'http://192.168.99.100:9999/bigdata/sparql' // blazegraph
            // endpoint: 'http://' + dbHost + ':' + dbPort + '/bigdata/sparql' // blazegraph's bigdata
        },
        schemas: requireDir('./schemas')
    }
    // mailer: {
    //     transport: nodemailerStubTransport()
    // }
};

