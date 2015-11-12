
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
                {label: 'Individual', route: 'eureka.individual.collection.index'},
                {label: 'Site', route: 'eureka.site.collection.index'},
                {label: 'Publication', route: 'eureka.publication.collection.index'}
            ]
        },
        {
            columns: 10,
            style: 'main-content',
            type: 'outlet'
        }
    ]
};