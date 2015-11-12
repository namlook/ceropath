
var generalInformations = {
    type: 'model-form',
    hideControlButtons: true,
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

var gpsInformations = {
    type: 'model-form',
    label: 'GPS informations',
    hideControlButtons: 'true',
    fields: [
        'geoWgsLat',
        'geoWgsLong',
        'geoWgsAlt'
    ]
};

var sitePhotos = {
    hideControlButtons: true,
    type: 'model-form',
    style: 'site-photos',
    fields: ['photos']
};

var cancelSaveButtons = {
    type: 'model-form',
    style: 'ceropath-cancel-save-btn',
    fields: []
};

export default {
    widgets: [
        {
            type: 'container',
            columns: 8,
            widgets: [
                generalInformations
            ]
        },
        {
            type: 'container',
            columns: 4,
            widgets: [
                cancelSaveButtons,
                gpsInformations,
                sitePhotos
            ]
        }
    ]
};