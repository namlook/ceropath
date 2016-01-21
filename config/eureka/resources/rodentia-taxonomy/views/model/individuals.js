
export default {
    widgets: [
        {
            type: 'model-embedded-collection-widget',
            resource: 'individual',
            query: {'taxonomyID': '${_id}'},
            widget: {
                type: 'collection-display',
                label: 'Related individuals'
            }
        }
    ]
};