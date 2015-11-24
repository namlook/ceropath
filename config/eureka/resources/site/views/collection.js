export default {
    queryParams: ['query'],
    widgets: [
        {
            type: 'collection-navbar',
            actions: [
                {label: 'map', icon: 'glyphicon glyphicon-globe', route: 'eureka.site.collection.map'}
                // {label: 'create', icon: 'glyphicon glyphicon-plus', route: 'eureka.site.new'}
            ],
            secondaryActions: [
                {label: 'chart center', icon: 'glyphicon glyphicon-stats', route: 'eureka.site.collection.visualization'}
            ]
        },
        {
            type: 'collection-query',
            queryParam: 'query',
            label: 'advanced query'

        }
    ]
};