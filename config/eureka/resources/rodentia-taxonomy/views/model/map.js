
export default {
    widgets: [
        {
            columns: 4,
            type: 'model-embedded-collection-widget',
            resource: 'individual',
            query: {'taxonomyID': '${_id}'},
            widget: {
                type: 'collection-aggregation',
                label: 'number individuals by country',
                aggregator: {
                    x: 'trappingSiteID.country',
                    y: {$count: true}
                },
                options: {sort: 'x'},
                display: {
                    as: 'pie',
                    x: {
                        as: 'x',
                        title: 'country',
                        suffix: 'mm'
                    },
                    y: {
                        as: 'y',
                        title: 'number of individuals'
                        // suffix: 'g'
                    }
                }
            }
        },
        {
            columns: 8,
            type: 'model-embedded-collection-widget',
            resource: 'individual',
            query: {'taxonomyID': '${_id}'},
            widget: {
                type: 'collection-map',
                latitudeProperty: 'trappingSiteID.latitude',
                longitudeProperty: 'trappingSiteID.longitude',
                // mapProvider: 'Esri.WorldImagery',
                aggregation: {
                    id: '_id',
                    title: 'title',
                    latitude: 'trappingSiteID.latitude', // !!required
                    longitude: 'trappingSiteID.longitude' //!!required
                },
                markerTitle: '<a href="/site/{id}" target="_blank">{title}</a>',
                maxZoom: 17,
                height: 450
            }
        }
    ]
};