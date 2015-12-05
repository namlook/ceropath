export default {
    widgets: [
        {
            type: 'model-form',
            actions: {
                save: {
                    transitionTo: 'eureka.microparasite.model.index'
                },
                cancel: {
                    transitionTo: 'eureka.microparasite.model.index'
                }
            }

        }
    ]
};