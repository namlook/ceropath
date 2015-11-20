
export default {
    widgets: [
        {
            columns: 12,
            type: 'container',
            widgets: [
                {
                    columns: 3,
                    type: 'model-embedded-collection-widget',
                    resource: 'individual',
                    query: {'taxonomy._id': '${_id}'},
                    widget: {
                        type: 'collection-groupby',
                        label: 'head & body size (mm)',
                        property: 'gender.title',
                        operator: 'avg',
                        target: 'headBodyMeasurement',
                        singleValue: true
                    }
                },
                {
                    columns: 3,
                    type: 'model-embedded-collection-widget',
                    resource: 'individual',
                    query: {'taxonomy._id': '${_id}'},
                    widget: {
                        type: 'collection-groupby',
                        label: 'tail size (mm)',
                        property: 'gender.title',
                        operator: 'avg',
                        target: 'tailMeasurement',
                        singleValue: true
                    }
                },
                {
                    columns: 3,
                    type: 'model-embedded-collection-widget',
                    resource: 'individual',
                    query: {'taxonomy._id': '${_id}'},
                    widget: {
                        type: 'collection-groupby',
                        label: 'foot size (mm)',
                        property: 'gender.title',
                        operator: 'avg',
                        target: 'footMeasurement',
                        singleValue: true
                    }
                },
                {
                    columns: 3,
                    type: 'model-embedded-collection-widget',
                    resource: 'individual',
                    query: {'taxonomy._id': '${_id}'},
                    widget: {
                        type: 'collection-groupby',
                        label: 'ear size (mm)',
                        property: 'gender.title',
                        operator: 'avg',
                        target: 'earMeasurement',
                        singleValue: true
                    }
                }
            ]
        },
        {
            columns: 12,
            type: 'container',
            widgets: [
                {
                    columns: 6,
                    type: 'model-embedded-collection-widget',
                    resource: 'individual',
                    query: {'taxonomy._id': '${_id}'},
                    widget: {
                        type: 'collection-groupby',
                        label: 'countries',
                        property: 'trappingSite.country',
                        chart: {
                            type: 'pie',
                            valueSuffix: ' individuals'
                        }
                    }
                },
                {
                    columns: 6,
                    type: 'model-embedded-collection-widget',
                    resource: 'individual',
                    query: {'taxonomy._id': '${_id}'},
                    queryOptions: {sort: "gender.title"},
                    widget: {
                        type: 'collection-groupby',
                        label: 'weight (g)',
                        property: 'gender.title',
                        operator: 'avg',
                        target: 'weighMeasurement',
                        chart: {
                            type: 'pie',
                            valueSuffix: 'g'
                        }
                    }
                }
            ]
        }
    ]
};