export default {
    widgets: [
        {
            type: 'model-form',
            actions: {
                save: {
                    transitionTo: 'eureka.individual.model.index'
                },
                cancel: {
                    transitionTo: 'eureka.individual.collection.index'
                }
            }

        }
    ]
};