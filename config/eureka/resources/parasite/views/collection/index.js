export default {
    widgets: [
        {
            type: 'collection-display',
            sort: {
                by: 'title',
                allowedProperties: '*'//['title', 'maturity', 'gender']
            },
            export: true
        }
    ]
};