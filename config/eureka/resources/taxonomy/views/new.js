
var description = {
    type: 'model-form',
    hideControlButtons: true,
    style: 'ceropath-taxonomy-description',
    displayStyle: 'plain',
    fields: ['description']
};

var generalInformations = {
    type: 'model-form',
    hideControlButtons: true,
    label: 'General informations',
    fields: [
        'isExtinct',
        'rankLevel',
        'msw3ID'
    ]
};

var taxonomicRanks = {
    type: 'model-form',
    hideControlButtons: true,
    label: 'Taxonomic ranks',
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
    type: 'model-form',
    hideControlButtons: true,
    label: 'IUCN informations',
    fields: [
        'iucnId',
        'iucnRedListStatus',
        'iucnRedListCriteriaVersion',
        'iucnYearAssessed',
        'iucnTrend'
    ]
};

var cancelSaveButtons = {
    type: 'model-form',
    style: 'ceropath-cancel-save-btn',
    fields: []
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
                cancelSaveButtons,
                generalInformations,
                taxonomicRanks,
                iucnInformations
            ]
        }
    ]
};
