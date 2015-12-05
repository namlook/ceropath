export default {
    widgets: [
        {
            type: 'model-form',
            actions: {
                save: {
                    transitionTo: 'eureka.file.model.index'
                },
                cancel: {
                    transitionTo: 'eureka.file.collection.index'
                }
            }

        }
    ]
};