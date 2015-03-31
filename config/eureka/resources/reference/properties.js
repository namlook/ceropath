
export default {
    name: {
        type: 'string'
    },
    publication: {
        type: 'Publication',
        inverse: 'references'
    },
    taxonomy: {
        type: 'Taxonomy',
        inverse: 'references'
    }
};