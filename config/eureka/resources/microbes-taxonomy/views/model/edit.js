export default {
    widgets: [
        {
            type: 'model-form',
            actions: {
                save: {
                    transitionTo: 'eureka.microbes-taxonomy.model.index'
                },
                cancel: {
                    transitionTo: 'eureka.microbes-taxonomy.model.index'
                }
            }

        }
    ]
};