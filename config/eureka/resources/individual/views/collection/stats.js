
export default {
    widgets: [
        {
            columns: 6,
            type: 'collection-groupby',
            property: 'gender',
            // label: 'Gender dispatch',
            chart: {
                type: 'pie'
            }
        },
        {
            columns: 6,
            type: 'collection-groupby',
            property: 'maturity',
            // considerUnfilled: true,
            chart: {
                type: 'column'
            }
        },
        {
            type: 'collection-groupby',
            property: 'taxonomy',
            chart: {
                type: 'bar'
            }
        },
        {
            columns: 6,
            type: 'collection-groupby',
            property: 'trappingSite.country',
            chart: {
                type: 'column'
            }
        },
        {
            columns: 6,
            type: 'collection-groupby',
            property: 'trappingSite.province',
            // considerUnfilled: true,
            chart: {
                type: 'column'
            }
        },
    ]
};