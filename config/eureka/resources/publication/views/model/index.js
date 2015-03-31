export default {
    widgets: [
        {type: 'model-display'},
        {
            type: 'model-relations-list',
            resource: 'Taxonomy',
            widget: {
                type: 'collection-display',
                label: "Referenced hosts",
                emptyPlaceholder: 'no host referenced in this publication'
            },
            query: '{"references.publication._id": "${_id}"}',
            queryOptions: {
                limit: 10
            }
        }
    ]
};