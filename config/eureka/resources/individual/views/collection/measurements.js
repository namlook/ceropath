
export default {
    widgets: [
        // {
        //     type: 'collection-aggregation',
        //     label: 'avg weight by genders',
        //     aggregator: {
        //         gender: 'gender.title',
        //         avgWeight: {$avg: 'weighMeasurement'}
        //     },
        //     options: {sort: 'gender'},
        //     display: {
        //         as: 'pie',
        //         x: {
        //             as: 'gender'
        //         },
        //         y: {
        //             as: 'avgWeight',
        //             title: 'weight',
        //             suffix: 'g'
        //         }
        //     }
        // },
        // {
        //     type: 'collection-aggregation',
        //     label: 'aggregated weight (g)',
        //     aggregator: {
        //         taxonomy: 'taxonomy.title',
        //         avgWeight: {$avg: 'weighMeasurement'},
        //         maxWeight: {$max: 'weighMeasurement'},
        //         minWeight: {$min: 'weighMeasurement'}
        //     },
        //     options: {limit: 10, sort: '-avgWeight'},
        //     display: {
        //         as: 'bar',
        //         x: {
        //             title: 'weight',
        //             suffix: 'g',
        //             series: [{
        //                 as: 'minWeight',
        //                 name: 'min weight',
        //             }, {
        //                 as: 'avgWeight',
        //                 name: 'average weight',
        //             }, {
        //                 as: 'maxWeight',
        //                 name: 'max weight',
        //             }]
        //         },
        //         y: {
        //             as: 'taxonomy',
        //             title: 'species name'
        //         }
        //     }
        // },
        // {
        //     type: 'collection-aggregation',
        //     label: 'aggregated weight (g)',
        //     aggregator: {
        //         taxonomy: 'taxonomy.title',
        //         avgWeight: {$avg: 'weighMeasurement'},
        //         maxWeight: {$max: 'weighMeasurement'},
        //         minWeight: {$min: 'weighMeasurement'}
        //     },
        //     options: {limit: 10, sort: '-avgWeight'},
        //     display: {
        //         as: 'column',
        //         x: {
        //             as: 'taxonomy',
        //             title: 'species name'
        //         },
        //         y: {
        //             title: 'weight',
        //             suffix: 'g',
        //             series: [{
        //                 as: 'minWeight',
        //                 name: 'min weight',
        //             }, {
        //                 as: 'avgWeight',
        //                 name: 'average weight',
        //             }, {
        //                 as: 'maxWeight',
        //                 name: 'max weight',
        //             }]
        //         }
        //     }
        // },
        // {
        //     type: 'collection-aggregation',
        //     label: 'aggregated weight (g)',
        //     aggregator: {
        //         taxonomy: 'taxonomy.title',
        //         elevation: 'trappingSite.geoWgsAlt',
        //         avgWeight: {$avg: 'weighMeasurement'},
        //         maxWeight: {$max: 'weighMeasurement'},
        //         minWeight: {$min: 'weighMeasurement'}
        //     },
        //     options: {sort: 'elevation', limit: 200},
        //     display: {
        //         as: 'line',
        //         x: {
        //             as: 'elevation',
        //             title: 'elevation',
        //             suffix: 'm'
        //         },
        //         y: {
        //             title: 'weight',
        //             suffix: 'g',
        //             series: [{
        //                 as: 'minWeight',
        //                 name: 'min weight',
        //             }, {
        //                 as: 'avgWeight',
        //                 name: 'average weight',
        //             }, {
        //                 as: 'maxWeight',
        //                 name: 'max weight',
        //             }]
        //         }
        //     }
        // },
        // {
        //     type: 'collection-aggregation',
        //     label: 'weight (g)',
        //     aggregator: {
        //         taxonomy: 'taxonomy.title',
        //         avgWeight: {$avg: 'weighMeasurement'},
        //     },
        //     options: {sort: '-avgWeight'},
        //     display: {
        //         as: 'bar',
        //         title: 'average weight by species',
        //         x: {
        //             as: 'avgWeight',
        //             title: 'average weight',
        //             suffix: 'g',
        //         },
        //         y: 'taxonomy'
        //     }
        // },
        {
            type: 'collection-groupby',
            property: 'taxonomy',
            operator: 'avg',
            target: 'weighMeasurement',
            label: 'weight (g)',
            chart: {
                type: 'bar',
                valueSuffix: 'g',
                valueLegend: 'g'
            }
        },
        {
            type: 'collection-groupby',
            property: 'taxonomy',
            operator: 'avg',
            target: 'headMeasurement',
            label: 'head (mm)',
            chart: {
                type: 'bar',
                valueSuffix: 'mm',
                valueLegend: 'mm'
            }
        },
        {
            type: 'collection-groupby',
            property: 'taxonomy',
            operator: 'avg',
            target: 'tailMeasurement',
            label: 'tail (mm)',
            chart: {
                type: 'bar',
                valueSuffix: 'mm',
                valueLegend: 'mm'
            }
        },
        {
            type: 'collection-groupby',
            property: 'taxonomy',
            operator: 'avg',
            target: 'footMeasurement',
            label: 'foot (mm)',
            chart: {
                type: 'bar',
                valueSuffix: 'mm',
                valueLegend: 'mm'
            }
        },
        {
            type: 'collection-groupby',
            property: 'taxonomy',
            operator: 'avg',
            target: 'earMeasurement',
            label: 'ear (mm)',
            chart: {
                type: 'bar',
                valueSuffix: 'mm',
                valueLegend: 'mm'
            }
        }
    ]
};