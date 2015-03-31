export default {
    widgets: [
        {
            type: 'model-form',
            actions: {
                save: {
                    transitionTo: 'eureka.site.model.index'
                },
                cancel: {
                    transitionTo: 'eureka.site.collection.index'
                }
            }

        }
    ]
};