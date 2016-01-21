
export default {
    widgets: [
        {
            type: 'model-embedded-collection-widget',
            resource: 'individual',
            query: {taxonomyID: '${_id}', isVoucherBarcoding: true},
            widget: {
                type: 'collection-display',
                label: 'Related vouchers',
                emptyPlaceholder: 'no vouchers referenced for this species'
            }
        }
    ]
};