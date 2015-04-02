/* jshint node: true */

var pkg = require('../package.json');

var eurekaStructureBuilder = require('eurekajs/structure-builder');
var eurekaConfigPath = require('path').resolve('.') + '/config/eureka';
var resources = eurekaStructureBuilder(eurekaConfigPath).resources;

module.exports = {
    name: pkg.name,
    version: 1,
    host: '0.0.0.0',
    port: process.env.EUREKA_SERVER_PORT || 80,
    enableCORS: true,
    schemas: resources,
    publicDirectory: 'dist',
    uploadDirectory: 'uploads',
    logLevel: 'info',
    database: {
        adapter: 'rdf',
        config: {
            store: 'virtuoso',
            host: process.env.DB_PORT_8890_TCP_ADDR, // docker uses this
            port: process.env.DB_PORT_8890_TCP_PORT,
            graphURI: 'http://ceropath.org'
        }
    }
};