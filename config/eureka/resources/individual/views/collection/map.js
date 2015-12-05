
export default {
    widgets: [
        {
            type: 'collection-map',
            latitudeProperty: 'trappingSiteID.latitude',
            longitudeProperty: 'trappingSiteID.longitude',
            // mapProvider: 'Esri.WorldImagery',
            // query: {fields: 'title,trappingSite', include: 'trappingSite', limit: 2000},
            aggregation: {
                id: '_id',
                title: 'title',
                latitude: 'trappingSiteID.latitude', // !!required
                longitude: 'trappingSiteID.longitude', //!!required
                trappingSiteTitle: 'trappingSiteID.title',
                trappingSiteID: 'trappingSiteID._id'
            },
            markerTitle: '<a href="/individual/{id}" target="_blank">{title}</a> on <a href="/site/{trappingSiteID}" target="_blank">{trappingSiteTitle}</a>',
            maxZoom: 17,
            height: 800
        }
    ]
};