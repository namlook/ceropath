export default {
    widgets: [
        {type: 'model-display'},
        {
            type: 'model-embedded-collection-widget',
            resource: 'taxonomy',
            query: {"references.publication._id": "${_id}"},
            queryOptions: {limit: 10},
            widget: {
                type: 'collection-display',
                label: 'Referenced hosts',
                emptyPlaceholder: 'no host referenced in this publication'
            }
        }
    ]
};