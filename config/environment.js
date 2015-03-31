/* jshint node: true */

var eurekaStructure = require('ember-eureka/config/structure');
var serverConfig = require('./server');

module.exports = function(environment) {
  var ENV = {
    modulePrefix: 'ceropath',
    environment: environment,
    baseURL: '/',
    locationType: 'auto',
    EmberENV: {
      FEATURES: {
        // Here you can enable experimental features on an ember canary build
        // e.g. 'with-controller': true
      }
    },

    APP: {
      // Here you can pass flags/options to your application instance
      // when it is created
      eureka: eurekaStructure
    }
  };

  if (environment === 'development') {
    // ENV.APP.LOG_RESOLVER = true;
    // ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    // ENV.APP.LOG_VIEW_LOOKUPS = true;

    ENV.APP.backendUrl = 'http://'+serverConfig.host+':'+serverConfig.port;
    ENV.APP.apiEndpoint = ENV.APP.backendUrl+'/api/1';

    ENV.contentSecurityPolicy = {
      'default-src': "'none'",
      'script-src': "'self'",
      'font-src': "'self'",
      'connect-src': "'self' "+ENV.APP.backendUrl,
      'img-src': "'self' data: http://*.mqcdn.com "+ENV.APP.backendUrl,
      'style-src': "'self' 'unsafe-inline'",
      'media-src': "'self'"
    };

  }

  if (environment === 'test') {
    // Testem prefers this...
    ENV.baseURL = '/';
    ENV.locationType = 'none';

    // keep test console output quieter
    ENV.APP.LOG_ACTIVE_GENERATION = false;
    ENV.APP.LOG_VIEW_LOOKUPS = false;

    ENV.APP.rootElement = '#ember-testing';
  }

  if (environment === 'production') {
    ENV.APP.apiEndpoint = '/api/1';

     ENV.contentSecurityPolicy = {
      'default-src': "'none'",
      'script-src': "'self'",
      'font-src': "'self'",
      'connect-src': "'self'",
      'img-src': "'self' data: http://*.mqcdn.com",
      'style-src': "'self' 'unsafe-inline'",
      'media-src': "'self'"
    };

  }

  return ENV;
};