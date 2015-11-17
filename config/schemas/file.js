
module.exports = {
    meta: {
        instanceRdfPrefix: 'http://ceropath.org/instances/file'
    },
    properties: {
        title: {
            type: 'string'
        },
        description: {
            type: 'string'
        },
        path: {
            type: 'string',
            meta: {
                eureka: {
                    widget: 'file'
                }
            }
        },
        mime: {
            type: 'string'
        },
        lastModified: {
            type: 'date'
        },
        size: {
            type: 'number',
            validate: ['integer']
        }
        // TODO author
    }
};