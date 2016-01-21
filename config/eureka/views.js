
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
                {label: 'Rodentia taxonomy', route: 'eureka.rodentia-taxonomy.collection.index'},
                {label: 'Microbes taxonomy', route: 'eureka.microbes-taxonomy.collection.index'},
                {label: 'Helminths taxonomy', route: 'eureka.helminths-taxonomy.collection.index'},
                {label: 'Individuals', route: 'eureka.individual.collection.index'},
                {label: 'Sites', route: 'eureka.site.collection.index'},
                // {label: 'Patients', route: 'eureka.patient.collection.index'},
                // {label: 'Surveys', route: 'eureka.survey.collection.index'},

                // {label: 'Sequences', route: 'eureka.sequence.collection.index'},
                {label: 'Parasites', route: 'eureka.parasite.collection.index'},
                {label: 'Microparasites', route: 'eureka.microparasite.collection.index'}
            ]
        },
        {
            columns: 10,
            style: 'main-content',
            type: 'outlet'
        }
    ]
};
