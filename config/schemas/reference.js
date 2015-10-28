
module.exports = {
    meta: {
        instanceRdfPrefix: 'http://ceropath.org/instances/reference',
    },
    properties: {
        name: {
            type: 'string'
        },
        publication: {
            type: 'Publication'
        },
        taxonomy: {
            type: 'Taxonomy'
        }
    }
};