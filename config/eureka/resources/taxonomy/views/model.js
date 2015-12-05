export default {
    widgets: [
        {
            type: 'model-navbar',
            actions: [
                {label: 'measurements', icon: 'glyphicon glyphicon-stats', route: 'eureka.taxonomy.model.measurements'},
                {label: 'map', icon: 'glyphicon glyphicon-globe', route: 'eureka.taxonomy.model.map'},
                {label: 'vouchers', icon: 'glyphicon glyphicon-align-justify', route: 'eureka.taxonomy.model.vouchers'},
                {label: 'individuals', icon: 'glyphicon glyphicon-align-justify', route: 'eureka.taxonomy.model.individuals'}
            ]
            // secondaryActions: [
            //     {label: 'edit', icon: 'glyphicon glyphicon-pencil', route: 'eureka.taxonomy.model.edit'},
            //     {name: 'delete', label: 'delete', icon: 'glyphicon glyphicon-trash'}
            // ]
        }
    ]
};