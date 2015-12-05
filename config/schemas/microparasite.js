
module.exports = {
    properties: {
        title: {
            type: 'string'
        },
        individualID: {
            label: 'individual',
            type: 'Individual'
        },
        taxonomyID: {
            label: 'taxonomy',
            type: 'Taxonomy'
        },
        detectionMethod: {
            type: 'string'
        },
        isPositive: {
            type: 'boolean'
        }
    }
};