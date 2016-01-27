
var generalInformations = {
    type: 'model-display',
    label: 'General informations',
    fields: [
        'title',
        'taxonomyID',
        'sex',
        'isVoucherBarcoding',
        'inSkullCollection',
        'identificationType',
        'identificationDate',
        'identificationMethod'
    ]
};

var measurements = {
    type: 'model-display',
    label: 'Measurements',
    fields: [
        'headBodyMeasurement',
        'tailMeasurement',
        'hindfootMeasurement',
        'earMeasurement',
        'bodyWeight',
        'headMeasurement',
        'spleenWeight',
        'anusGenitalDistance'
    ]
};


var trappingMap = {
    type: 'model-map',
    style: 'individual-trapping-map',
    label: 'Trapping informations',
    latitudeProperty: 'trappingSiteID.latitude',
    longitudeProperty: 'trappingSiteID.longitude'
};

var trappingInformations = {
    type: 'model-display',
    fields: [
        'trappingSiteID',
        'trappingDate',
        'trappingMethod',
        'trappingAccuracy',
        'trappingLandscapeMediumRes',
        'trappingLandscapeLowRes',
        'isTrappedAlive',
        'isDissected'
    ]
};


var physiologicalFeatures = {
    type: 'model-display',
    label: 'Physiological features',
    fields: [
        'vagina',
        'teats',
        'mammae',
        'embryoLeftSide',
        'embryoRightSide',
        'testes',
        'testesLength',
        'seminalVesicle'
    ]
};

var trappingGallery = {
    type: 'model-embedded-collection-widget',
    resource: 'individual',
    query: {'id': '${_id}'},
    widget: {
        type: 'collection-gallery',
        imageSrc: 'trappingSiteID.photos',
        filePath: {
            prefix: '/trapping_lines'
        },
        label: 'trapping site gallery',
        options: {distinct: true, limit: 20}
    }
};

var morphologyGallery = {
    type: 'model-embedded-collection-widget',
    resource: 'individual',
    query: {'id': '${_id}'},
    widget: {
        type: 'collection-gallery',
        imageSrc: 'morphologyPhotos.path',
        label: 'Morphological views',
        options: {distinct: true, limit: 10}
    }
};

var skullGallery = {
    type: 'model-embedded-collection-widget',
    resource: 'individual',
    query: {'id': '${_id}'},
    widget: {
        type: 'collection-gallery',
        imageSrc: 'skullPhotos.path',
        label: 'Skull measurements',
        options: {distinct: true, limit: 10}
    }
};

var parasites = {
    type: 'model-embedded-collection-widget',
    resource: 'parasite',
    query: {'individualID': '${_id}'},
    widget: {
        type: 'collection-display',
        label: 'Parasites found in this individual'
    }
};

var microparasites = {
    type: 'model-embedded-collection-widget',
    resource: 'microparasite',
    query: {'individualID': '${_id}'},
    widget: {
        type: 'collection-display',
        label: 'Micro-parasites found in this individual'
    }
};

var sequences = {
    type: 'model-embedded-collection-widget',
    resource: 'sequence',
    query: {'individualID': '${_id}'},
    widget: {
        type: 'collection-display',
        label: 'Sequences'
    }
};

export default {
    widgets: [
        {
            type: 'container',
            columns: 9,
            widgets: [
                generalInformations,
                trappingMap,
                trappingInformations,
                {
                    type: 'container',
                    columns: 6,
                    widgets: [measurements]
                },
                {
                    type: 'container',
                    columns: 6,
                    widgets: [physiologicalFeatures]
                },
                {
                    type: 'container',
                    columns: 6,
                    widgets: [parasites]
                },
                {
                    type: 'container',
                    columns: 6,
                    widgets: [microparasites]
                }
            ]
        },
        {
            type: 'container',
            columns: 3,
            widgets: [trappingGallery, morphologyGallery, skullGallery, sequences]
        }
    ]
};
