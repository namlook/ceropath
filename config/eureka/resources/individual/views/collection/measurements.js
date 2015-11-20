
export default {
    widgets: [
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