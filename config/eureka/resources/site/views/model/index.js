
var siteMap = {
    type: 'model-map',
    style: 'site-map',
    latitudeProperty: 'latitude',
    longitudeProperty: 'longitude'
};

var gpsInformations = {
    type: 'model-display',
    fields: [
        'latitude',
        'longitude',
        'elevation'
    ]
};

var generalInformations = {
    type: 'model-display',
    displayStyle: 'table',
    fields: [
        'title',
        'country',
        'province'
    ]
};

// var sitePhotos = {
//     type: 'model-display',
//     label: 'Photos of the land',
//     style: 'site-photos',
//     hideLabels: true,
//     fields: ['photos']
// };


var gallery = {
    type: 'model-embedded-collection-widget',
    resource: 'site',
    query: {id: '${_id}'},
    widget: {
        type: 'collection-gallery',
        imageSrc: 'photos',
        imageTitle: 'title',
        label: 'trapping site gallery',
        filePath: {
            prefix: '/trapping_lines'
        },
        options: {distinct: true, limit: 20}
    }
    // aggregation: {
        // photos: {$concat: photos}
    // },
    // options: {distinct: true}
}


var trappedInvidividuals = {
    type: 'model-embedded-collection-widget',
    resource: 'individual',
    query: {'trappingSiteID._id': '${_id}'},
    queryOptions: {limit: 10},
    widget: {
        type: 'collection-display',
        label: 'Trapped individuals',
        emptyPlaceholder: 'no individual trapped in this site'
    }
};


export default {
    widgets: [
        {
            type: 'container',
            columns: 8,
            widgets: [
                gallery
            ]
        },
        {
            type: 'container',
            columns: 4,
            widgets: [
                siteMap,
                gpsInformations,
                generalInformations,
                trappedInvidividuals
            ]
        }


    ]
};