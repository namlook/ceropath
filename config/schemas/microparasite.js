
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
            type: 'MicrobesTaxonomy'
        },
        detectionMethod: {
            type: 'string'
        },
        isPositive: {
            type: 'boolean'
        }
    }
};