
var generalInformations = {
    type: 'model-display',
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
    type: 'model-display',
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
    style: 'individual-trapping-map',
    label: 'Trapping informations',
    latitudeProperty: 'trappingSite.geoWgsLat',
    longitudeProperty: 'trappingSite.geoWgsLong'
};

var trappingInformations = {
    type: 'model-display',
    fields: [
        'trappingMethod',
        'isTrappedAlive',
        'trappingAccuracy',
        'trappingSite'
        // 'trappingLandscapeHightResolution',
        // 'trappingLandscapeMediumResolution',
        // 'trappingLandscapeLowResolution'
    ]
};


var physiologicalFeatures = {
    type: 'model-display',
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
            widgets: [trappingMap, trappingInformations, physiologicalFeatures]
        }
    ]
};