export default {
    widgets: [
        {
            type: 'collection-navbar',
            actions: [
                {label: 'map', icon: 'glyphicon glyphicon-globe', route: 'eureka.microparasite.collection.map'}
                // {label: 'create', icon: 'glyphicon glyphicon-plus', route: 'eureka.microparasite.new'}
            ],
            secondaryActions: [
                {label: 'chart center', icon: 'glyphicon glyphicon-stats', route: 'eureka.microparasite.collection.visualization'}
            ]
        },
        {
            type: 'collection-query',
            queryParam: 'query',
            label: 'advanced query'
        }
    ]
};