export default {
    widgets: [
        {
            type: 'model-navbar',
            actions: [
                {label: 'vouchers', route: 'eureka.taxonomy.model.vouchers'},
                {label: 'individuals', route: 'eureka.taxonomy.model.individuals'}
            ]
            // secondaryActions: [
            //     {label: 'edit', icon: 'glyphicon glyphicon-pencil', route: 'eureka.taxonomy.model.edit'},
            //     {name: 'delete', label: 'delete', icon: 'glyphicon glyphicon-trash'}
            // ]
        }
    ]
};