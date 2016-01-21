export default {
    widgets: [
        {
            type: 'model-form',
            actions: {
                save: {
                    transitionTo: 'eureka.rodentia-taxonomy.model.index'
                },
                cancel: {
                    transitionTo: 'eureka.rodentia-taxonomy.collection.index'
                }
            }

        }
    ]
};