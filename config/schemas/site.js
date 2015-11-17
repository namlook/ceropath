
module.exports = {
    meta: {
        instanceRdfPrefix: 'http://ceropath.org/instances/site'
    },
    properties: {
        title: {
            type: 'string'
        },
        region: {
            type: 'string',
            description: 'Asian region (ex: South East Asia)'
        },
        country: {
            type: 'string'
        },
        province: {
            type: 'string'
        },
        district: {
            type: 'string'
        },
        village: {
            type: 'string'
        },
        isCeropathSite: {
            type: 'boolean'
        },
        averageHousesNumber: {
            type: 'number',
            validate: ['integer'],
            description: 'order of magnitude of the number of the surrounding houses: 1=10, 2=100 and 3=1000 house'
        },
        averageHousesDistance: {
            type: 'number',
            validate: ['integer'],
            description: 'order of magnitude of the distance of the houses: 1=10m, 2=100m and 3=1km'
        },
        geoWgsLat: {
            type: 'number',
            validate: [{precision: 12}],
            label: 'latitude',
            description: 'wgs84 latitude (DLL projection)'
        },
        geoWgsLong: {
            type: 'number',
            validate: [{precision: 12}],
            label: 'longitude',
            description: 'wgs84 longitude (DLL projection)'
        },
        geoWgsAlt: { // can be calculated from lat and long
            type: 'number',
            validate: [{precision: 12}],
            label: 'elevation',
            description: 'wgs84 altitude (DLL projection)'
        },
        surroundingLandscapeHighResolution: {
            type: 'string' // 'LandscapeType'
        },
        surroundingLandscapeMediumResolution: {
            type: 'string' // 'LandscapeType'
        },
        surroundingLandscapeLowResolution: {
            type: 'string' // 'LandscapeType'
        },
        photos: {
            type: 'array',
            items: 'File',
            meta: {
                eureka: {
                    widget: 'file-attachment'
                }
            }
        },
        // photos: {
        //     type: 'string',
        //     meta: {
        //         eureka: {
        //             widget: 'file'
        //         }
        //     }
        // },
        comment: {
            type: 'string'
        }
    },
    inverseRelationships: {
        trappedIndividuals: {
            type: 'Individual',
            property: 'trappingSite'
        }

    }
};