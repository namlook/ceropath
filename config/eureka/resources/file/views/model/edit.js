export default {
    widgets: [
        {
            type: 'model-file-edit',
            actions: {
                save: {
                    transitionTo: 'eureka.file.model.index'
                },
                cancel: {
                    transitionTo: 'eureka.file.model.index'
                }
            }

        }
    ]
};