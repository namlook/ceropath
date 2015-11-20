
export default {
    widgets: [
        {
            type: 'model-embedded-collection-widget',
            resource: 'individual',
            query: {'taxonomy._id': '${_id}'},
            widget: {
                type: 'collection-display',
                label: 'Related individuals'
            }
        }
    ]
};