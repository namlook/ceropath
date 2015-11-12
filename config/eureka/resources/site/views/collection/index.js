export default {
    widgets: [
        {
            columns: 8,
            type: 'collection-display',
            sort: {
                by: 'title',
                allowedProperties: '*'
            },
            export: true
        },
        {
            columns: 4,
            type: 'container',
            widgets: [
                {
                    type: 'collection-groupby',
                    property: 'country',
                    considerUnfilled: true,
                    chart: {
                        type: 'bar'
                    }
                },
                {
                    type: 'collection-groupby',
                    property: 'province',
                    considerUnfilled: true,
                    chart: {
                        type: 'bar'
                    }
                }
            ]
        }
    ]
};