export default {
    widgets: [
        {
            type: 'model-form',
            actions: {
                save: {
                    transitionTo: 'eureka.reference.model.index'
                },
                cancel: {
                    transitionTo: 'eureka.reference.collection.index'
                }
            }

        }
    ]
};