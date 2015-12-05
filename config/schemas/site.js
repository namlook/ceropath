
module.exports = {
    properties: {
        title: {
            type: 'string'
        },
        latitude: {
            type: 'number'
        },
        longitude: {
            type: 'number'
        },
        elevation: {
            type: 'number'
        },
        country: {
            type: 'string'
        },
        province: {
            type: 'string'
        },
        photos: {
            type: 'array',
            items: 'string'
        },
        comment: {
            type: 'string'
        }
    }
};