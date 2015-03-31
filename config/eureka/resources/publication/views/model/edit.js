export default {
    widgets: [
        {
            type: 'model-form',
            actions: {
                save: {
                    transitionTo: 'eureka.publication.model.index'
                },
                cancel: {
                    transitionTo: 'eureka.publication.model.index'
                }
            }

        }
    ]
};