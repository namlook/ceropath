var config = require('./server');

config.port = 7357;
config.enableCORS = true;
config.database.config.graphURI = 'http://testceropath.org';

module.exports = config;