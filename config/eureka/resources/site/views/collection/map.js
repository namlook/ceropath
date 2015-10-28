
export default {
    widgets: [
        {
            type: 'collection-map',
            latitudeProperty: 'geoWgsLat',
            longitudeProperty: 'geoWgsLong',
            // mapProvider: 'Esri.WorldImagery',
            markerTitle: '<a href="/site/{_id}" target="_blank">{title}</a> <br /> <ul><li>{surroundingLandscapeLowResolution}</li><li>{surroundingLandscapeMediumResolution}</li><li>{surroundingLandscapeHighResolution}</li></ul>',

            maxZoom: 17,
            height: 800
        }
    ]
};