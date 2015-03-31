export default {
    widgets: [
        {
            type: 'model-form',
            actions: {
                save: {
                    transitionTo: 'eureka.gender.model.index'
                },
                cancel: {
                    transitionTo: 'eureka.gender.collection.index'
                }
            }

        }
    ]
};