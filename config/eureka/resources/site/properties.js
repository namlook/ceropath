
export default {
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
        type: 'integer',
        description: 'order of magnitude of the number of the surrounding houses: 1=10, 2=100 and 3=1000 house'
    },
    averageHousesDistance: {
        type: 'integer',
        description: 'order of magnitude of the distance of the houses: 1=10m, 2=100m and 3=1km'
    },
    geoWgsLat: {
        type: 'float',
        precision: 12,
        label: 'latitude',
        description: "wgs84 latitude (DLL projection)"
    },
    geoWgsLong: {
        type: 'float',
        precision: 12,
        label: 'longitude',
        description: "wgs84 longitude (DLL projection)"
    },
    geoWgsAlt: { // can be calculated from lat and long
        type: 'float',
        precision: 12,
        label: 'elevation',
        description: "wgs84 altitude (DLL projection)"
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
        type: 'File',
        multi: true,
        widget: 'file-attachment'
    },
    comment: {
        type: 'string'
    }
};