export default {
    queryParams: ['query'],
    widgets: [
        {
            type: 'collection-navbar',
            actions: [
                {label: 'statistics', icon: 'glyphicon glyphicon-stats', route: 'eureka.individual.collection.stats'},
                {label: 'create', icon: 'glyphicon glyphicon-plus', route: 'eureka.individual.new'}
            ]
        },
        {
            type: 'collection-query',
            queryParam: 'query',
            label: 'advanced query'
        }
    ]
};