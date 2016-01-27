
module.exports = {
    properties: {
        title: {
            type: 'string'
        },
        individualID: {
            type: 'Individual',
            label: 'individual'
        },
        gene: {
            type: 'string'
        },
        operator: {
            type: 'string'
        },
        forwardPrimer: {
            type: 'Primer'
        },
        reversePrimer: {
            type: 'Primer'
        },
        sequence: {
            type: 'string'
        }
    }
};
