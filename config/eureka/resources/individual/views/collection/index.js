export default {
    widgets: [
        {
            // columns: 8,
            type: 'collection-display',
            sort: {
                by: 'title',
                allowedProperties: '*'//['title', 'maturity', 'gender']
            },
            export: true
        },
        // {
        //     columns: 4,
        //     type: 'container',
        //     widgets: [
        //         {
        //             type: 'collection-groupby',
        //             property: 'gender',
        //             label: 'Gender dispatch',
        //             chart: {
        //                 type: 'pie'
        //             }
        //         },
        //         {
        //             type: 'collection-groupby',
        //             property: 'maturity',
        //             // considerUnfilled: true,
        //             chart: {
        //                 type: 'column'
        //             }
        //         },
        //         {
        //             type: 'collection-groupby',
        //             property: 'taxonomy',
        //             chart: {
        //                 type: 'bar'
        //             }
        //         }
        //     ]
        // }
    ]
};