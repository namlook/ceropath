
var config = require('../../config/frontend');
config.schemas = require('../schemas');
App = EurekaTest = Eurekapp(config);

/** Add your custom code below **/

App.GeoDatedFactModel = App.Model.extend({
    title: function() {
        var _title = [this.get('subject.title'), this.get('predicate.title'), this.get('object.title')];
        if (this.get('location')) {
            _title.push('(at '+this.get('location.title')+')');
        }
        return _title.join(' ');
    }.property('subject.title', 'predicate.title', 'object.title', 'location.title')
});