export default {
    widgets: [
        {
            type: 'collection-navbar',
            // actions: [
                // {label: 'create', icon: 'glyphicon glyphicon-plus', route: 'eureka.sequence.new'}
            // ],
            secondaryActions: [
                {label: 'chart center', icon: 'glyphicon glyphicon-stats', route: 'eureka.sequence.collection.visualization'}
            ]
        },
        {
            type: 'collection-query',
            queryParam: 'query',
            label: 'advanced query'
        }
    ]
};