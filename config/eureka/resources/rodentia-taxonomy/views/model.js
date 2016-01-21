export default {
    widgets: [
        {
            type: 'model-navbar',
            secondaryActions: [
                {label: 'measurements', icon: 'glyphicon glyphicon-stats', route: 'eureka.rodentia-taxonomy.model.measurements'},
                {label: 'map', icon: 'glyphicon glyphicon-globe', route: 'eureka.rodentia-taxonomy.model.map'},
                {label: 'vouchers', icon: 'glyphicon glyphicon-align-justify', route: 'eureka.rodentia-taxonomy.model.vouchers'},
                {label: 'individuals', icon: 'glyphicon glyphicon-align-justify', route: 'eureka.rodentia-taxonomy.model.individuals'}
            ]
        }
    ]
};
