
export default {
    widgets: [
        {
            type: 'model-relations-list',
            resource: 'Individual',
            widget: {
                type: 'collection-display',
                label: "Related individuals"
            },
            query: '{"taxonomy._id": "${_id}"}'
        }
    ]
};