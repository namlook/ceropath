/* jshint node: true */

var pkg = require('../package.json');

// var nodemailerStubTransport = require('nodemailer-stub-transport');
var requireDir = require('require-dir');

// var dbHost = process.env.DB_PORT_8890_TCP_ADDR; // docker uses this
// var dbPort = process.env.DB_PORT_8890_TCP_PORT;

// if (!dbHost || !dbPort) {
    // throw Error('host or port unknown');
// }

// if (!process.env.EUREKA_SERVER_PORT) {
    // throw Error('EUREKA_SERVER_PORT not set');
// }

module.exports = {
    name: pkg.name,
    host: '0.0.0.0',
    port: 8888, //process.env.EUREKA_SERVER_PORT || 80,
    app: {
        secret: 'thisisthesecretthing',
        email: 'contact@project.com',
        clientRootUrl: 'http://www.project.com',
        apiRootPrefix: '/api/1'
    },
    // enableCORS: true,
    resources: requireDir('../backend/resources'),
    // publicDirectory: 'dist',
    fileUploads: {
        uploadDirectory: './uploads',
        maxBytes: 50 // 50 MB
    },
    log: ['warn'],
    database: {
        config: {
            graphUri: 'http://ceropath.org',
            endpoint: 'http://192.168.99.100:8890/sparql' // virtuoso
            // endpoint: 'http://192.168.99.100:9999/bigdata/sparql' // blazegraph
            // endpoint: 'http://' + dbHost + ':' + dbPort + '/bigdata/sparql' // blazegraph's bigdata
        },
        schemas: requireDir('./schemas')
    }
    // mailer: {
    //     transport: nodemailerStubTransport()
    // }
};

