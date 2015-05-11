
var generalInformations = {
    type: 'model-form',
    hideControlButtons: true,
    label: 'General informations',
    fields: [
        'title',
        'taxonomy',
        'gender',
        'maturity',
        'isVoucherBarcoding',
        'inSkullCollection',
        'dissectionDate',
        'comment'
    ]
};

var measurements = {
    type: 'model-form',
    hideControlButtons: true,
    label: 'Measurements',
    fields: [
        'headBodyMeasurement',
        'tailMeasurement',
        'footMeasurement',
        'earMeasurement',
        'weighMeasurement',
        'headMeasurement',
        'breadthOfRostrumMeasurement',
        'lengthOfRostrumMeasurement',
        'occipitoNasalLengthMeasurement',
        'interorbitalBreadthMeasurement',
        'breathOfBrainCaseMeasurement',
        'zygomaticBreadthMeasurement',
        'breadthOfIncisiveForaminaMeasurement',
        'breadthOfFirstUpperMolarMeasurement',
        'lengthOfDiastemaMeasurement',
        'lenghtOfIncisiveForaminaMeasurement',
        'lenghtOfBonyPalateMeasurement',
        'postPalatalLengthMeasurement',
        'lengthOfAuditoryBullaMeasurement',
        'breadthOfMesopterygoidFossaMeasurement',
        'breadthOfBonyPalateAtfirstMeasurement',
        'crownLengthOfMaxillaryMolarMeasurement',
        'breathOfZygomaticPlateMeasurement',
        'heightOfBraincaseMeasurement',
        'spleenWeightMeasurement',
        'agpdMeasurement',
        'molecularIdentification'
    ]
};


var trappingMap = {
    type: 'model-map',
    label: 'Trapping informations',
    latitudeProperty: 'trappingSite.geoWgsLat',
    longitudeProperty: 'trappingSite.geoWgsLong'
};

var trappingInformations = {
    type: 'model-form',
    hideControlButtons: true,
    label: 'Trapping informations',
    fields: [
        'trappingMethod',
        'isTrappedAlive',
        'trappingAccuracy',
        'trappingSite',
        'trappingLandscapeHightResolution',
        'trappingLandscapeMediumResolution',
        'trappingLandscapeLowResolution'
    ]
};


var physiologicalFeatures = {
    type: 'model-form',
    hideControlButtons: true,
    label: 'Physiological features',
    fields: [
        'vagina',
        'teats',
        'mammaeDistribution',
        'leftSideEmbryosNumber',
        'rightSideEmbryosNumber',
        'testesOutput',
        'testesLength',
        'seminalVesicule',
        'sexualMaturity',
        'm3Development'
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
            widgets: [generalInformations, measurements]
        },
        {
            type: 'container',
            columns: 4,
            widgets: [cancelSaveButtons, trappingInformations, physiologicalFeatures]
        }
    ]
};