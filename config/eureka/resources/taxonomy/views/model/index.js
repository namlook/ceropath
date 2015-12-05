
var description = {
    type: 'model-display',
    style: 'ceropath-taxonomy-description',
    hideLabels: true,
    fields: ['descriptionFile']
};

// var generalInformations = {
//     type: 'model-display',
//     label: 'General informations',
//     displayStyle: 'table',
//     fields: [
//         'isExtinct',
//         'rankLevel',
//         'msw3ID'
//     ]
// };

var taxonomicRanks = {
    type: 'model-display',
    label: 'Taxonomic ranks',
    displayStyle: 'table',
    fields: [
        'kingdom',
        'phylum',
        'class',
        'order',
        'family',
        'genus',
        'species'
    ]
};

// var iucnInformations = {
//     type: 'model-display',
//     label: 'IUCN informations',
//     displayStyle: 'table',
//     fields: [
//         'iucnId',
//         'iucnRedListStatus',
//         'iucnRedListCriteriaVersion',
//         'iucnYearAssessed',
//         'iucnTrend'
//     ]
// };

// var relatedPublications = {
//     type: 'model-embedded-collection-widget',
//     resource: 'publication',
//     query: {"references.taxonomy._id": "${_id}"},
//     queryOptions: {limit: 10},
//     widget: {
//         type: 'collection-display',
//         label: 'Referenced in:'
//     }
// };

var aliveGallery = {
    type: 'model-embedded-collection-widget',
    resource: 'Taxonomy',
    query: {id: '${_id}'},
    style: 'alive-animal-photo',
    widget: {
        type: 'collection-gallery',
        imageSrc: 'alivePhotos.path',
        // imageTitle: 'alivePhotos.title',
        options: {distinct: true, limit: 1}
    }
    // aggregation: {
        // photos: {$concat: photos}
    // },
    // options: {distinct: true}
};

var morphologyGallery = {
    type: 'model-embedded-collection-widget',
    resource: 'individual',
    query: {'taxonomyID': '${_id}'},
    widget: {
        type: 'collection-gallery',
        imageSrc: 'morphologyPhotos.path',
        imageTitle: 'morphologyPhotos.title',
        label: 'Morphological views',
        options: {distinct: true, limit: 5}
    }
};

var trappingGallery = {
    type: 'model-embedded-collection-widget',
    resource: 'individual',
    query: {'taxonomyID': '${_id}'},
    widget: {
        type: 'collection-gallery',
        imageSrc: 'trappingSiteID.photos',
        label: 'trapping site gallery',
        filePath: {
            prefix: '/trapping_lines'
        },
        options: {distinct: true, limit: 5}
    }
};

export default {
    widgets: [
        {
            type: 'container',
            columns: 6,
            widgets: [aliveGallery]
        },
        {
            type: 'container',
            columns: 6,
            widgets: [taxonomicRanks]
        },
        description,
        {
            type: 'container',
            columns: 6,
            widgets: [morphologyGallery]
        },
        {
            type: 'container',
            columns: 6,
            widgets: [trappingGallery]
        }
    ]
};