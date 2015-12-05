
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
    ]
};