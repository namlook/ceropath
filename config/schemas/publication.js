
module.exports = {
    meta: {
        instanceRdfPrefix: 'http://ceropath.org/instances/publication'
    },
    properties: {
        title: {
            type: 'string'
        },
        source: {
            type: 'string'
        },
        reference: {
            type: 'string'
        },
        link: {
            type: 'string'
        }
    },
    inverseRelationships: {
        references: {
            type: 'Reference',
            property: 'publication'
        }
    }
};