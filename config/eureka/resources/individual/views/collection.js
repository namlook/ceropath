export default {
    queryParams: ['query'],
    widgets: [
        {
            type: 'collection-navbar',
            actions: [
                {label: 'measurements', icon: 'glyphicon glyphicon-stats', route: 'eureka.individual.collection.measurements'},
                {label: 'map', icon: 'glyphicon glyphicon-globe', route: 'eureka.individual.collection.map'}
                // {label: 'create', icon: 'glyphicon glyphicon-plus', route: 'eureka.individual.new'}
            ],
            secondaryActions: [
                {label: 'chart center', icon: 'glyphicon glyphicon-stats', route: 'eureka.individual.collection.visualization'}
            ]
        },
        {
            type: 'collection-query',
            queryParam: 'query',
            label: 'advanced query'
        }
    ]
};