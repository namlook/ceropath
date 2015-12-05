export default {
    widgets: [
        {
            type: 'collection-navbar',
            actions: [
                {label: 'map', icon: 'glyphicon glyphicon-globe', route: 'eureka.parasite.collection.map'}
                // {label: 'create', icon: 'glyphicon glyphicon-plus', route: 'eureka.parasite.new'}
            ],
            secondaryActions: [
                {label: 'chart center', icon: 'glyphicon glyphicon-stats', route: 'eureka.parasite.collection.visualization'}
            ]
        },
        {
            type: 'collection-query',
            queryParam: 'query',
            label: 'advanced query'
        }
    ]
};