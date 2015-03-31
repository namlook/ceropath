
export default {
    widgets: [
        {
            type: 'model-relations-list',
            resource: 'Individual',
            widget: {
                type: 'collection-display',
                label: "Related vouchers",
                emptyPlaceholder: 'no vouchers referenced for this species'
            },
            query: '{"taxonomy._id": "${_id}", "isVoucherBarcoding": true}'
        }
    ]
};