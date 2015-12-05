export default {
    queryParams: ['query'],
    widgets: [
        {
            type: 'collection-navbar',
            actions: [
                // {label: 'create', icon: 'glyphicon glyphicon-plus', route: 'eureka.taxonomy.new'}
            ],
            secondaryActions: [
                {label: 'chart center', icon: 'glyphicon glyphicon-stats', route: 'eureka.taxonomy.collection.visualization'}
            ]
        },
        {
            type: 'collection-query',
            queryParam: 'query'
        }
    ]
};