export default {
    widgets: [
        {
            type: 'model-form',
            actions: {
                save: {
                    transitionTo: 'eureka.primer.model.index'
                },
                cancel: {
                    transitionTo: 'eureka.primer.collection.index'
                }
            }

        }
    ]
};
