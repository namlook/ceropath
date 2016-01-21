
module.exports = {
    properties: {
        title: {
            type: 'string'
        },

        descriptionFile: {
            type: 'string',
            meta: {
                eureka: {
                    widget: {
                        type: 'markdown',
                        filePath: {
                            prefix: '/taxonomy_descriptions'
                        }
                    }
                }
            }
        },

        authority: {
            type: 'string'
        },

        iucnID: {
            type: 'string'
        },

        // taxonomic rank
        kingdom: {
            type: 'string',
            label: 'kingdom',
            description: 'kingdom rank'
        },
        phylum: {
            type: 'string',
            label: 'phylum',
            description: 'phylum rank'
        },
        class: {
            type: 'string',
            label: 'class',
            description: 'class rank'
        },
        order: {
            type: 'string',
            label: 'order',
            description: 'order rank'
        },
        family: {
            type: 'string',
            label: 'family',
            description: 'family rank'
        },

        genus: {
            type: 'string',
            label: 'genus',
            description: 'genus rank'
        },
        species: {
            type: 'string',
            label: 'species',
            description: 'species rank'
        },

        // photos
        alivePhotos: {
            type: 'array',
            items: 'File'
        },
        morphologyPhotos: {
            type: 'array',
            items: 'File'
        }
    }
};