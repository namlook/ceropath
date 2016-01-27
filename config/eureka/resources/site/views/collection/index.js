export default {
    widgets: [
        {
            type: 'collection-map',
            latitudeProperty: 'latitude',
            longitudeProperty: 'longitude',
            // mapProvider: 'Esri.WorldImagery',
            aggregation: {
                id: '_id',
                title: 'title',
                latitude: 'latitude', // !!required
                longitude: 'longitude' //!!required
            },
            markerTitle: '<a href="/site/{id}" target="_blank">{title}</a>',
            maxZoom: 17,
            height: 800
        }
        // {
        //     columns: 8,
        //     type: 'collection-display',
        //     sort: {
        //         by: 'title',
        //         allowedProperties: '*'
        //     },
        //     export: true
        // },
        // {
        //     columns: 4,
        //     type: 'container',
        //     widgets: [
        //         {
        //             type: 'collection-groupby',
        //             property: 'country',
        //             considerUnfilled: true,
        //             chart: {
        //                 type: 'bar'
        //             }
        //         },
        //         {
        //             type: 'collection-groupby',
        //             property: 'province',
        //             considerUnfilled: true,
        //             chart: {
        //                 type: 'bar'
        //             }
        //         }
        //     ]
        // }
    ]
};
