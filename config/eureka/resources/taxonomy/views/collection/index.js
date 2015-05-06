export default {
    widgets: [
        {
            columns: 8,
            type: 'collection-display',
            filter: true
        },
        {
            columns: 4,
            type: 'container',
            widgets: [
                {
                    type: 'collection-groupby',
                    property: 'kingdomRank',
                    chart: {
                        type: 'pie'
                    }
                },
                {
                    type: 'collection-groupby',
                    property: 'familyRank',
                    chart: {
                        type: 'bar'
                    }
                }
            ]
        }
    ]
};