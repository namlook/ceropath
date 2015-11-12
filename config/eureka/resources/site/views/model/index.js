
var siteMap = {
    type: 'model-map',
    style: 'site-map',
    latitudeProperty: 'geoWgsLat',
    longitudeProperty: 'geoWgsLong'
};

var gpsInformations = {
    type: 'model-display',
    fields: [
        'geoWgsLat',
        'geoWgsLong',
        'geoWgsAlt'
    ]
};

var generalInformations = {
    type: 'model-display',
    displayStyle: 'table',
    fields: [
        'title',
        'region',
        'country',
        'province',
        'district',
        'village',
        'isCeropathSite',
        'averageHousesNumber',
        'averageHousesDistance',
        'surroundingLandscapeHighResolution',
        'surroundingLandscapeMediumResolution',
        'surroundingLandscapeLowResolution'
    ]
};

var sitePhotos = {
    type: 'model-display',
    label: 'Photos of the land',
    style: 'site-photos',
    hideLabels: true,
    fields: ['photos']
};


var trappedInvidividuals = {
    type: 'model-relations-list',
    resource: 'Individual',
    widget: {
        type: 'collection-display',
        label: 'Trapped individuals',
        emptyPlaceholder: 'no individual trapped in this site'
    },
    query: '{"trappingSite._id": "${_id}"}',
    queryOptions: {
        limit: 10
    }
};


export default {
    widgets: [
        {
            type: 'container',
            columns: 8,
            widgets: [
                generalInformations,
                trappedInvidividuals
            ]
        },
        {
            type: 'container',
            columns: 4,
            widgets: [
                siteMap,
                gpsInformations,
                sitePhotos
            ]
        }


    ]
};