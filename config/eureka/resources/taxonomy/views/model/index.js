
var description = {
    type: 'model-display',
    style: 'ceropath-taxonomy-description',
    displayStyle: 'plain',
    fields:['description']
};

var generalInformations = {
    type: 'model-display',
    label: 'General informations',
    displayStyle: 'table',
    fields: [
        'isExtinct',
        'rankLevel',
        'msw3ID'
    ]
};

var taxonomicRanks = {
    type: 'model-display',
    label: 'Taxonomic ranks',
    displayStyle: 'table',
    fields: [
        'kingdomRank',
        'phylumRank',
        'classRank',
        'orderRank',
        'familyRank',
        'genusRank',
        'speciesRank'
    ]
};

var iucnInformations = {
    type: 'model-display',
    label: 'IUCN informations',
    displayStyle: 'table',
    fields: [
        'iucnId',
        'iucnRedListStatus',
        'iucnRedListCriteriaVersion',
        'iucnYearAssessed',
        'iucnTrend',
    ]
};

var relatedPublications = {
    type: 'model-relations-list',
    resource: 'Publication',
    widget: {
        type: 'collection-display',
        label: "Referenced in:"
    },
    query: '{"references.taxonomy._id": "${_id}"}',
    queryOptions: {
        limit: 10
    }
};

export default {
    widgets: [

        {
            type: 'container',
            columns: 8,
            widgets: [description]
        },

        {
            type: 'container',
            columns: 4,
            widgets: [
                generalInformations,
                taxonomicRanks,
                iucnInformations,
                relatedPublications
            ]
        }
    ]
};