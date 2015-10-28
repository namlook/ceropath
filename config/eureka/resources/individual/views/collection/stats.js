
export default {
    widgets: [
        {
            columns: 6,
            type: 'collection-groupby',
            property: 'gender',
            // label: 'Gender dispatch',
            chart: {
                type: 'pie'
            }
        },
        {
            columns: 6,
            type: 'collection-groupby',
            property: 'maturity',
            // considerUnfilled: true,
            chart: {
                type: 'column'
            }
        },
        {
            type: 'collection-groupby',
            property: 'taxonomy',
            chart: {
                type: 'bar'
            }
        },
        {
            columns: 6,
            type: 'collection-groupby',
            property: 'trappingSite.country',
            chart: {
                type: 'column'
            }
        },
        {
            columns: 6,
            type: 'collection-groupby',
            property: 'trappingSite.province',
            // considerUnfilled: true,
            chart: {
                type: 'column'
            }
        }
        // {
        //     type: 'collection-map',
        //     latitudeProperty: 'trappingSite.geoWgsLat',
        //     longitudeProperty: 'trappingSite.geoWgsLong',
        //     query: {fields: 'title,trappingSite', include: 'trappingSite', limit: 1000},
        //     markerTitle: '<a href="/individual/{_id}" target="_blank">{title}</a> on <a href="/site/{trappingSite._id}" target="_blank">{trappingSite.title}</a>',
        //     // mapProvider: 'Esri.WorldImagery',
        //     maxZoom: 17,
        //     height: 500
        // }
    ]
};