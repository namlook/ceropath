
export default {
    title: {
        type: 'string'
    },

    description: {
        type: 'string',
        widget: 'markdown'
    },

    comment: {
        type: 'string',
        widget: 'textarea'
    },

    isExtinct: {
        type: 'boolean',
        label: 'extinct ?'
    },

    commonNames: {
        hidden: true, // XXX TODO
        type: 'string',
        i18n: true,
        displayAllLanguages: true
        // in engligh, french, spanish, thai, lao and khmer
    },

    /** IUCN infos **/
    iucnId: { // IUCN ID
        type: 'string',
        label: 'IUCN ID',
        description: 'IUCN ID'
    },
    iucnRedListStatus: {
        type: 'string'
    },
    iucnRedListCriteriaVersion: {
        type: 'string'
    },
    iucnYearAssessed: {
        type: 'string'
    },
    iucnTrend: {
        type: 'string'
    },

    /** discovery infos **/
    discoveryAuthor: {
        type: 'string',
        description: 'author who described the species for the first time'
    },
    discoveryYear: {
        type: 'integer',
        description: 'the year when the species was described for the first time'
    },
    discoveryName: {
        type: 'string',
        description: 'the name given to the species when described for the first time'
    },
    discoveryLocality: {
        type: 'string',
        description: 'the locality where the species has been described for the first time'
    },


    // taxonomic rank
    kingdomRank: {
        type: 'string',
        label: 'kingdom',
        description: 'kingdom rank'
    },
    phylumRank: {
        type: 'string',
        label: 'phylum',
        description: 'phylum rank'
    },
    classRank: {
        type: 'string',
        label: 'class',
        description: 'class rank'
    },
    orderRank: {
        type: 'string',
        label: 'order',
        description: 'order rank'
    },
    suborderRank: {
        hidden: true,
        type: 'string',
        label: 'suborder',
        description: 'suborder rank'
    },
    infraorderRank: {
        hidden: true,
        type: 'string',
        label: 'infraorder',
        description: 'infraorder rank'
    },
    superfamilyRank: {
        hidden: true,
        type: 'string',
        label: 'superfamily',
        description: 'superfamily rank'
    },
    familyRank: {
        type: 'string',
        label: 'family',
        description: 'family rank'
    },
    subfamilyRank: {
        hidden: true,
        type: 'string',
        label: 'subfamily',
        description: 'subfamily rank'
    },
    tribeRank: { // not from MSW3
        hidden: true,
        type: 'string',
        label: 'tribe',
        description: 'tribe rank',
    },
    divisionRank: { // not from MSW3
        hidden: true,
        type: 'string',
        label: 'division',
        description: 'division rank'
    },
    groupsRank: {
        hidden: true,
        type: 'string',
        label: 'groups',
        description: 'groups rank'
    },
    genusRank: {
        type: 'string',
        label: 'genus',
        description: 'genus rank'
    },
    subgenusRank: {
        hidden: true,
        type: 'string',
        label: 'subgenus',
        description: 'subgenus rank'
    },
    speciesRank: {
        type: 'string',
        label: 'species',
        description: 'species rank'
    },
    subspeciesRank: {
        hidden: true,
        type: 'string',
        label: 'subspecies',
        description: 'subspecies rank'
    },

    rankLevel: { // ???
        type: 'string',
        label: 'rank level'
    },

    msw3ID: {
        hidden: true,
        type: 'string',
        label: 'MSW3 reference',
        description: "reference id of Mammals Species of the World 3"
    },
};