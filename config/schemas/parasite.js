
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
            type: 'HelminthsTaxonomy'
        },
        abundance: {
            type: 'number'
        }
    }
};