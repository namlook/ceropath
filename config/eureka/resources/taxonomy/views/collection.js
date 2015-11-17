export default {
    queryParams: ['query'],
    widgets: [
        // {
        //     type: 'collection-navbar',
        //     actions: [
        //         {label: 'create', icon: 'glyphicon glyphicon-plus', route: 'eureka.taxonomy.new'}
        //     ]
        // },
        {
            type: 'collection-query',
            queryParam: 'query'
        }
    ]
};