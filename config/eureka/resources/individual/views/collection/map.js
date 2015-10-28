
export default {
    widgets: [
        {
            type: 'collection-map',
            latitudeProperty: 'trappingSite.geoWgsLat',
            longitudeProperty: 'trappingSite.geoWgsLong',
            // mapProvider: 'Esri.WorldImagery',
            query: {fields: 'title,trappingSite', include: 'trappingSite', limit: 2000},
            markerTitle: '<a href="/individual/{_id}" target="_blank">{title}</a> on <a href="/site/{trappingSite._id}" target="_blank">{trappingSite.title}</a>',
            maxZoom: 17,
            height: 800
        }
    ]
};