export default {
    widgets: [
        {
            type: 'model-form',
            actions: {
                save: {
                    transitionTo: 'eureka.taxonomy.model.index'
                },
                cancel: {
                    transitionTo: 'eureka.taxonomy.collection.index'
                }
            }

        }
    ]
};