export default {
    widgets: [
        {
            type: 'model-file-new',
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