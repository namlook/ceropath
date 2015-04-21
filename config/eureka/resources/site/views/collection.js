export default {
    queryParams: ['query'],
    widgets: [
        {
            type: 'collection-navbar',
            actions: [
                {label: 'create', icon: 'glyphicon glyphicon-plus', route: 'eureka.site.new'}
            ]
        },
        {
            type: 'collection-query',
            queryParam: 'query'
        }
    ]
};