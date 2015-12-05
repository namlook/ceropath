export default {
    widgets: [
        {
            type: 'model-form',
            actions: {
                save: {
                    transitionTo: 'eureka.parasite.model.index'
                },
                cancel: {
                    transitionTo: 'eureka.parasite.collection.index'
                }
            }

        }
    ]
};