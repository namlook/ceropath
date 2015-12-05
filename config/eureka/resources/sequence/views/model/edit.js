export default {
    widgets: [
        {
            type: 'model-form',
            actions: {
                save: {
                    transitionTo: 'eureka.sequence.model.index'
                },
                cancel: {
                    transitionTo: 'eureka.sequence.model.index'
                }
            }

        }
    ]
};