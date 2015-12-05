
export default {
    widgets: [
        {
            type: 'application-navbar',
            brand: 'Ceropath'
        },
        {
            columns: 2,
            type: 'application-menu',
            items: [
                {label: 'Pipeline', route: 'eureka.index'},
                {label: 'Taxonomy', route: 'eureka.taxonomy.collection.index'},
                {label: 'Individuals', route: 'eureka.individual.collection.index'},
                // {label: 'Sites', route: 'eureka.site.collection.index'},
                // {label: 'Sequences', route: 'eureka.sequence.collection.index'},
                // {label: 'Parasites', route: 'eureka.parasite.collection.index'},
                // {label: 'Microparasites', route: 'eureka.microparasite.collection.index'}
            ]
        },
        {
            columns: 10,
            style: 'main-content',
            type: 'outlet'
        }
    ]
};