
export default {
    widgets: [
        {
            type: 'collection-map',
            latitudeProperty: 'individualID.trappingSiteID.latitude',
            longitudeProperty: 'individualID.trappingSiteID.longitude',
            // mapProvider: 'Esri.WorldImagery',
            // query: {fields: 'title,trappingSite', include: 'trappingSite', limit: 2000},
            aggregation: {
                id: '_id',
                title: 'title',
                latitude: 'individualID.trappingSiteID.latitude', // !!required
                longitude: 'individualID.trappingSiteID.longitude', //!!required
                trappingSiteTitle: 'individualID.trappingSiteID.title',
                trappingSiteID: 'individualID.trappingSiteID._id'
            },
            markerTitle: '<a href="/individual/{id}" target="_blank">{title}</a> on <a href="/site/{trappingSiteID}" target="_blank">{trappingSiteTitle}</a>',
            maxZoom: 17,
            height: 800
        }
    ]
};