
module.exports = {
    // meta: {
    // },
    properties: {
        title: {
            type: 'string'
        },
        taxonomyID: {
            label: 'taxonomy',
            type: 'RodentiaTaxonomy'
        },
        sex: {
            type: 'string'
        },

        // identification informations
        identificationType: {
            type: 'string'
        },
        identificationDate: {
            type: 'date'
        },
        identificationMethod: {
            type: 'string'
        },

        isVoucherBarcoding: {
            type: 'boolean',
            description: 'True if the individual is used as reference in the indentification tool'
        },
        inSkullCollection: {
            type: 'boolean',
            description: 'True if the skull has been cleaned and added to the collection'
        },
        // trapping informations
        trappingDate: {
            type: 'date'
            // dateFormat: 'll'
        },
        trappingMethod: {
            type: 'string',
            description: 'Describes how the individual was collected'
        },
        trappingAccuracy: {
            type: 'number',
            validate: ['integer'],
            description: 'Trapping accuracy: 1=10m, 2=100m and 3=1km'
        },
        trappingLandscapeMediumRes: {
            type: 'string',
            label: 'trapping landscape medium resolution',
            description: 'Describe the type of landscape around the trap (medium resolution)'
        },
        trappingLandscapeLowRes: {
            type: 'string',
            label: 'trapping landscape low resolution',
            description: 'Describe the type of landscape around the trap (low resolution)'
        },
        trappingSiteID: {
            type: 'Site',
            label: 'trapping site',
            description: 'the place where the individual has been trapped'
        },
        isTrappedAlive: {
            type: 'boolean',
            description: 'True if the individual has been trapped alive'
        },
        isDissected: {
            type: 'boolean',
            description: 'True if the individual has been dissected'
        },

        internet_display: {
            type: 'boolean'
        },

        // measurements
        headBodyMeasurement: {
            type: 'number',
            validate: [{precision: 0}],
            label: 'head & body (mm)',
            description: 'Head & Body (mm) (measurement_accuracy: 0)'
        },
        tailMeasurement: {
            type: 'number',
            validate: [{precision: 0}],
            label: 'tail (mm)',
            description: 'Tail (mm) (measurement_accuracy: 0)'
        },
        hindfootMeasurement: {
            type: 'number',
            validate: [{precision: 0}],
            label: 'foot (mm)',
            description: 'Foot (mm) (measurement_accuracy: 0)'
        },
        earMeasurement: {
            type: 'number',
            validate: [{precision: 0}],
            label: 'ear (mm)',
            description: 'Ear (mm) (measurement_accuracy: 0)'
        },
        bodyWeight: {
            type: 'number',
            validate: [{precision: 0}],
            label: 'weight (g)',
            description: 'Weight (g) (measurement_accuracy: 0)'
        },
        headMeasurement: {
            type: 'number',
            validate: [{precision: 0}],
            label: 'head (mm)',
            description: 'Head (mm) (measurement_accuracy: 0)'
        },
        spleenWeight: {
            type: 'number',
            validate: [{precision: 0}],
            label: 'spleen weight (mg)',
            description: 'Spleen weight (mg) (measurement_accuracy: 0)'
        },
        anusGenitalDistance: {
            type: 'number',
            validate: [{precision: 1}],
            label: 'anus/genital distance (mm)',
            description: 'Distance beetween the anus and the genital parts'
        },


        // physiological features
        vagina: {
            type: 'string',
            description: 'is the vagina open or closed ?'
        },
        teats: {
            type: 'string',
            description: 'how visible are the teats ?'
        },
        mammae: {
            type: 'string'
        },
        embryoLeftSide: {
            label: '# of left-side embryos',
            type: 'number',
            validate: ['integer'],
            description: 'number of embryos in the left side'
        },
        embryoRightSide: {
            label: '# of right-side embryos',
            type: 'number',
            validate: ['integer'],
            description: 'number of embryos in the right side'
        },
        testes: {
            type: 'string',
            description: 'are the testes inside or outside'
        },
        testesLength: {
            type: 'number',
            validate: [{precision: 3}]
        },
        seminalVesicle: {
            type: 'string',
            description: 'how is developped the seminal vesicule'
        },

        // photos

        skullPhotos: {
            type: 'array',
            items: 'File'
        },
        alivePhotos: {
            type: 'array',
            items: 'File'
        },
        morphologyPhotos: {
            type: 'array',
            items: 'File'
        },

        credit: {
          type: 'string'
        }
        // sexualMaturity: {
        //     type: 'boolean',
        //     description: 'is the individual sexualy mature ?'
        // },
        // m3Development: {
        //     type: 'string'
        // },

        // breadthOfRostrumMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'breadth of rostrum (mm)',
        //     description: 'Breadth of Rostrum  (mm) (M01) (measurement_accuracy: 2)'
        // },
        // lengthOfRostrumMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'length of rostrum (mm)',
        //     description: 'Length of Rostrum (mm) (M02) (measurement_accuracy: 2)'
        // },
        // occipitoNasalLengthMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'occipitoNasal length (mm)',
        //     description: 'OccipitoNasal Length (mm) (M03) (measurement_accuracy: 2)'
        // },
        // interorbitalBreadthMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     description: 'Interorbital Breadth (mm) (M04) (measurement_accuracy: 2)'
        // },
        // breathOfBrainCaseMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'breath of brainCase (mm)',
        //     description: 'Breath of BrainCase (mm) (M05) (measurement_accuracy:)'
        // },
        // zygomaticBreadthMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'zygomatic breadth (mm)',
        //     description: 'Zygomatic Breadth (mm) (M06) (measurement_accuracy: 2)'
        // },
        // breadthOfIncisiveForaminaMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'breadth of incisive foramina (mm)',
        //     description: 'Breadth of Incisive Foramina (mm) (M07) (measurement_accuracy: 2)'
        // },
        // breadthOfFirstUpperMolarMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'breadth of first upper Molar (mm)',
        //     description: 'Breadth of first upper Molar (mm) (M08) (measurement_accuracy: 2)'
        // },
        // lengthOfDiastemaMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'length of Diastema (mm)',
        //     description: 'Length of Diastema (mm) (M09) (measurement_accuracy: 2)'
        // },
        // lenghtOfIncisiveForaminaMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'lenght of incisive foramina (mm)',
        //     description: 'Lenght of Incisive Foramina (mm) (M10) (measurement_accuracy: 2)'
        // },
        // lenghtOfBonyPalateMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'lenght of bony palate (mm)',
        //     description: 'Lenght of Bony Palate (mm) (M11) (measurement_accuracy: 2)'
        // },
        // postPalatalLengthMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'post-palatal length (mm)',
        //     description: 'PostPalatal Length (mm) (M12) (measurement_accuracy: 2)'
        // },
        // lengthOfAuditoryBullaMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'length of auditory bulla (mm)',
        //     description: 'Length of auditory Bulla (mm) (M13) (measurement_accuracy: 2)'
        // },
        // breadthOfMesopterygoidFossaMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'breadth of mesopterygoid fossa (mm)',
        //     description: 'Breadth of Mesopterygoid Fossa (mm) (M14) (measurement_accuracy: 2)'
        // },
        // breadthOfBonyPalateAtfirstMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'breadth of bony palate at first (mm)',
        //     description: 'Breadth of Bony Palate at first  (mm) (M15) (measurement_accuracy: 2)'
        // },
        // crownLengthOfMaxillaryMolarMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'crown length of maxillary molar (mm)',
        //     description: 'Crown Length of Maxillary Molar  (mm) (M16) (measurement_accuracy: 2)'
        // },
        // breathOfZygomaticPlateMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'breath of zygomatic plate (mm)',
        //     description: 'Breath of Zygomatic Plate (mm) (M17) (measurement_accuracy: 2)'
        // },
        // heightOfBraincaseMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'height of braincase (mm)',
        //     description: 'Height of Braincase (mm) (M18) (measurement_accuracy: 2)'
        // },
        // agpdMeasurement: {
        //     type: 'number',
        //     validate: [{precision: 0}],
        //     label: 'AGPD (mm)',
        //     description: 'AGPD (mm) (measurement_accuracy: 0)'
        // },
        // molecularIdentification: {
        //     type: 'boolean',
        //     description: 'true if a molecular identification has been performed on the individual',
        //     meta: {
        //         eureka: {
        //             hidden: true
        //         }
        //     }
        // }


    }
};
