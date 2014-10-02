var editAction = {name: 'edit', icon: 'glyphicon glyphicon-pencil'};
var deleteAction = {name: 'delete', icon: 'glyphicon glyphicon-trash'};

module.exports = {
    Species: {
        label: {
            en: {
                plural: 'Species'
            },
            fr: {
                singular: 'Espèce'
            }
        },
        schema: {
            title: {
                type: 'string'
            },
            isExtinct: {
                type: 'boolean',
                label: 'extinct ?'
            },
            commonNames: {
                type: 'string',
                i18n: true,
                displayAllLanguages: true
                // in engligh, french, spanish, thai, lao and khmer
            },
            iucn: { // IUCN ID
                type: 'string',
                description: 'IUCN reference'
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
            discoveryAuthor: {
                type: 'string',
                description: 'author who described the species for the first time'
            },
            discoveryYear: {
                type: 'integer',
                label: 'description year',
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
            // citations: {
            //     type: 'Citation',
            //     multi: true,
            //     description: 'publications where the species is described'
            // },
            // synonyms: {
            //     type: 'Citation',
            //     multi: true,
            //     description: 'publications where the species was described in another name'
            // },
            msw3ID: {
                hidden: true,
                type: 'string',
                label: 'MSW3 reference',
                description: "reference id of Mammals Species of the World 3"
            },
            taxonomicKingdomRank: {
                type: 'string',
                label: 'kingdom',
                description: 'taxonomic kingdom'
            },
            taxonomicPhylumRank: {
                type: 'string',
                label: 'phylum',
                description: 'taxonomic phylum'
            },
            taxonomicClassRank: {
                type: 'string',
                label: 'class',
                description: 'taxonomic class'
            },
            taxonomicOrderRank: {
                type: 'string',
                label: 'order',
                description: 'taxonomic order'
            },
            taxonomicSuborderRank: {
                hidden: true,
                type: 'string',
                label: 'suborder',
                description: 'taxonomic suborder'
            },
            taxonomicInfraorderRank: {
                hidden: true,
                type: 'string',
                label: 'infraorder',
                description: 'taxonomic infraorder'
            },
            taxonomicSuperfamilyRank: {
                hidden: true,
                type: 'string',
                label: 'superfamily',
                description: 'taxonomic superfamily'
            },
            taxonomicFamilyRank: {
                type: 'string',
                label: 'family',
                description: 'taxonomic family'
            },
            taxonomicSubfamilyRank: {
                hidden: true,
                type: 'string',
                label: 'subfamily',
                description: 'taxonomic subfamily'
            },
            taxonomicTribeRank: { // not from MSW3
                hidden: true,
                type: 'string',
                label: 'tribe',
                description: 'taxonomic tribe',
            },
            taxonomicDivisionRank: { // not from MSW3
                hidden: true,
                type: 'string',
                label: 'division',
                description: 'taxonomic division'
            },
            taxonomicGroupsRank: {
                hidden: true,
                type: 'string',
                label: 'groups',
                description: 'taxonomic groups'
            },
            taxonomicGenusRank: {
                type: 'string',
                label: 'genus',
                description: 'taxonomic genus'
            },
            taxonomicSubgenusRank: {
                hidden: true,
                type: 'string',
                label: 'subgenus',
                description: 'taxonomic subgenus'
            },
            taxonomicSpeciesRank: {
                type: 'string',
                label: 'species',
                description: 'taxonomic species'
            },
            taxonomicSubspeciesRank: {
                hidden: true,
                type: 'string',
                label: 'subspecies',
                description: 'taxonomic subspecies'
            },
            taxonLevel: { // ???
                type: 'string',
                label: 'taxon level'
            }
        },
        views: {
            index: {
                widgets: [
                    [{
                        type: 'timeSeries',
                        field: 'discoveryYear',
                        label: 'Number of species discovered',
                        css: 'col-sm-9'
                    }, {
                        type: 'matchingQueryDonut',
                        css: 'col-sm-3'
                    }],
                    [{
                        type: 'tableView',
                        fields: ['title', 'commonNames', 'iucnRedListStatus', 'iucnTrend', 'iucnRedListCriteriaVersion'],
                    }]
                ]
            },
            display: {
                populate: 2
            }
        },
        facets: [
            'iucnTrend',
            {label: 'Genus', field: 'taxonomicGenusRank'}
        ],
        fieldsets : [
            {
                label: 'Taxonomic ranks',
                fields: [
                    'taxonomicKingdomRank',
                    'taxonomicPhylumRank',
                    'taxonomicClassRank',
                    'taxonomicOrderRank',
                    'taxonomicFamilyRank',
                    'taxonomicGenusRank',
                    'taxonomicSpeciesRank',
                    'taxonomicSubspeciesRank'
                ]
            },
            {
                label: 'IUCN',
                fields: [
                    "iucn",
                    "iucnRedListStatus",
                    "iucnRedListCriteriaVersion",
                    "iucnTrend"
                ]
            },
            {
                label: 'Species discovery',
                fields: [
                    'discoveryAuthor',
                    'discoveryYear',
                    'discoveryName',
                    'discoveryLocality'
                ]
            }
        ],
    },
    Individual: {
        facets: [
            'maturity',
            {label: 'gender', field: 'gender.label@en'},
            'voucherBarcoding',
            {label: 'species', field:'species.title', limit: 10}
        ],
        fieldsets: [
            {
                label: 'Trapping informations',
                fields: [
                    'trappingMethod',
                    'trappedAlive',
                    'trapAccuracy',
                    'trappingSite',
                    'trappingLandscapeHightResolution',
                    'trappingLandscapeMediumResolution',
                    'trappingLandscapeLowResolution',
                    'trappingID'
                ]
            },
            {
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
                    'm3Development',
                ]
            },
            {
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
                    'molecularIdentification',
                ]
            }
        ],
        views: {
            index: {
                widgets: [
                    [{
                        type: 'timeSeries',
                        field: 'dissectionDate',
                        label: 'Number of dissections',
                        aggregationType: '$year'
                    }],
                    [{
                        type: 'tableView',
                        fields: ['title', 'species', 'gender', 'maturity', 'voucherBarcoding'],
                        populate: 1,
                        limit: 15,
                        sortBy: 'maturity'
                    }],
                    [
                        {
                            type: 'matchingQueryDonut'
                        },
                        {
                            type: 'facetDonut',
                            field: 'maturity',
                            label: 'Maturity'
                        },
                        {
                            type: 'facetDonut',
                            field: 'gender.label',
                            label: 'Gender'
                        },
                        {
                            type: 'facetDonut',
                            field: 'voucherBarcoding',
                            label: 'Voucher barcoding'
                        }
                    ]
                ]
            },
            // _display: {
            //     widgets: [
            //         [{
            //             type: 'map'
            //         }],
            //         [{
            //             type: 'modelDisplay'
            //             //fieldsets: fieldsets,
            //         }]
            //     ]
            // }
        },
        schema: {
            title: {
                type: 'string'
            },
            species: {
                type: 'Species',
                inverse: 'individuals'
            },
            gender: { // from sex
                type: 'Gender',
            },
            maturity: {
                type: 'string'
            },
            voucherBarcoding: {
                type: 'boolean',
                description: "True if the individual is used as reference in the indentification tool"
            },
            inSkullCollection: { // from skull_collection
                type: 'boolean',
                description: "True if the skull has been cleaned and added to the collection"
            },
            dissectionDate: { // from Date_of_dissection
                type: 'date',
                dateFormat: 'll'
            },
            comment: {
                type: 'string'
            },
            // trapping informations
            trappingMethod: {
                type: 'string',
                description: 'Describes how the individual was collected'
            },
            trappedAlive: {
                type: 'boolean',
                description: 'True if the individual has been trapped alive'
            },
            trapAccuracy: {
                type: 'integer',
                description: "Trapping précision: 1=10m, 2=100m and 3=1km"
            },
            trappingSite: {
                type: 'Site',
                inverse: 'trappingIndividuals',
                description: 'the place where the individual has been trapped'
            },
            trappingLandscapeHightResolution: {
                type: 'LandscapeType',
                description: "Describe the type of landscape around the trap (hight resolution) "
            },
            trappingLandscapeMediumResolution: {
                type: 'LandscapeType',
                description: "Describe the type of landscape around the trap (medium resolution) "
            },
            trappingLandscapeLowResolution: {
                type: 'LandscapeType',
                description: "Describe the type of landscape around the trap (low resolution) "
            },
            trappingID: {
                hidden: true,
                type: 'string',
                description: 'temporal id given in the field when the individual was trapped'
            },
            // physiological features
            vagina: {
                type: 'string',
                description: "is the vagina open or closed ?"
            },
            teats: {
                type: 'string',
                description: "how visible are the teats ?"
            },
            mammaeDistribution: {
                type: 'string'
            },
            leftSideEmbryosNumber: {
                label: "# of left-side embryos",
                type: 'integer',
                description: "number of embryos in the left side"
            },
            rightSideEmbryosNumber: {
                label: "# of right-side embryos",
                type: 'integer',
                description: "number of embryos in the right side"
            },
            testesOutput: {
                type: 'string',
                description: "are the testes inside or outside"
            },
            testesLength: {
                type: 'float',
                precision: 3
            },
            seminalVesicule: {
                type: 'string',
                description: "how is developped the seminal vesicule"
            },
            sexualMaturity: {
                type: 'boolean',
                description: "is the individual sexualy mature ?"
            },
            m3Development: {
                type: 'string'
            },
            // measurements
            headBodyMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Head & Body (mm) (measurement_accuracy: 0)'
            },
            tailMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Tail (mm) (measurement_accuracy: 0)'
            },
            footMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Foot (mm) (measurement_accuracy: 0)'
            },
            earMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Ear (mm) (measurement_accuracy: 0)'
            },
            weighMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Weight (g) (measurement_accuracy: 0)'
            },
            headMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Head (mm) (measurement_accuracy: 0)'
            },
            breadthOfRostrumMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Breadth of Rostrum  (mm) (M01) (measurement_accuracy: 2)'
            },
            lengthOfRostrumMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Length of rostrum (mm) (M02) (measurement_accuracy: 2)'
            },
            occipitoNasalLengthMeasurement: {
                type: 'float',
                precision: 4,
                description: 'OccipitoNasal Length (mm) (M03) (measurement_accuracy: 2)'
            },
            interorbitalBreadthMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Interorbital Breadth (mm) (M04) (measurement_accuracy: 2)'
            },
            breathOfBrainCaseMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Breath of BrainCase (mm) (M05) (measurement_accuracy:)'
            },
            zygomaticBreadthMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Zygomatic Breadth (mm) (M06) (measurement_accuracy: 2)'
            },
            breadthOfIncisiveForaminaMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Breadth of Incisive Foramina (mm) (M07) (measurement_accuracy: 2)'
            },
            breadthOfFirstUpperMolarMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Breadth of first upper Molar (mm) (M08) (measurement_accuracy: 2)'
            },
            lengthOfDiastemaMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Length of Diastema (mm) (M09) (measurement_accuracy: 2)'
            },
            lenghtOfIncisiveForaminaMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Lenght of Incisive Foramina (mm) (M10) (measurement_accuracy: 2)'
            },
            lenghtOfBonyPalateMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Lenght of Bony Palate (mm) (M11) (measurement_accuracy: 2)'
            },
            postPalatalLengthMeasurement: {
                type: 'float',
                precision: 4,
                description: 'PostPalatal Length (mm) (M12) (measurement_accuracy: 2)'
            },
            lengthOfAuditoryBullaMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Length of auditory Bulla (mm) (M13) (measurement_accuracy: 2)'
            },
            breadthOfMesopterygoidFossaMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Breadth of Mesopterygoid Fossa (mm) (M14) (measurement_accuracy: 2)'
            },
            breadthOfBonyPalateAtfirstMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Breadth of Bony Palate at first  (mm) (M15) (measurement_accuracy: 2)'
            },
            crownLengthOfMaxillaryMolarMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Crown Length of Maxillary Molar  (mm) (M16) (measurement_accuracy: 2)'
            },
            breathOfZygomaticPlateMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Breath of Zygomatic Plate (mm) (M17) (measurement_accuracy: 2)'
            },
            heightOfBraincaseMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Height of Braincase (mm) (M18) (measurement_accuracy: 2)'
            },
            spleenWeightMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Spleen weight (mg) (measurement_accuracy: 0)'
            },
            agpdMeasurement: {
                type: 'float',
                precision: 4,
                description: 'Agpd (mm) (measurement_accuracy: 0)'
            },
            molecularIdentification: {
                hidden: true,
                type: 'boolean'
                // true if a molecular identification has been performed on the individual
            }

        }
    },
    Gender: {
        hidden: true,
        description: "Male, female or unknown",
        aliases: {title: 'label'},
        schema: {
            label: {
                type: 'string',
                i18n: true
            }
        }
    },
    LandscapeType: {
        hidden: true,
        description: "The type of landscape (lowland, upland, forest, settlement...)",
        aliases: {title: 'label'},
        schema: {
            label: {
                type: 'string',
                i18n: true
            }
        }
    },
    Site: {
        views: {
            index: {
                widgets: [
                    [{
                        type: 'map',
                        latitudeField: 'geoWgsLat',
                        longitudeField: 'geoWgsLong',
                        limit: 500,
                        groupMarkers: true
                    }],
                    [{
                        type: 'tableView',
                        fields: ['title', 'country', 'village', 'isCeropathSite']
                    }]
                ]
            }
        },
        facets: [
            'isCeropathSite',
            {label: 'High res. landscape', field: 'surroundingLandscapeHighResolution.label@en', limit: 10},
            {label: 'Medium res. landscape', field: 'surroundingLandscapeMediumResolution.label@en'},
            {label: 'Low res. landscape', field: 'surroundingLandscapeLowResolution.label@en'}
        ],
        schema: {
            title: {
                type: 'string'
            },
            region: {
                type: 'string',
                description: 'Asian region (ex: South East Asia)'
            },
            country: {
                type: 'string'
            },
            province: {
                type: 'string'
            },
            district: {
                type: 'string'
            },
            village: {
                type: 'string'
            },
            soilType: {
                type: 'SoilType'
            },
            isCeropathSite: {
                type: 'boolean'
            },
            averageHousesNumber: {
                type: 'integer',
                description: 'order of magnitude of the number of the surrounding houses: 1=10, 2=100 and 3=1000 house'
            },
            averageHousesDistance: {
                type: 'integer',
                description: 'order of magnitude of the distance of the houses: 1=10m, 2=100m and 3=1km'
            },
            geoWgsLat: {
                type: 'float',
                precision: 12,
                label: 'latitude',
                description: "wgs84 latitude (DLL projection)"
            },
            geoWgsLong: {
                type: 'float',
                precision: 12,
                label: 'longitude',
                description: "wgs84 longitude (DLL projection)"
            },
            geoWgsAlt: { // can be calculated from lat and long
                type: 'float',
                precision: 12,
                label: 'elevation',
                description: "wgs84 altitude (DLL projection)"
            },
            surroundingLandscapeHighResolution: {
                type: 'LandscapeType'
            },
            surroundingLandscapeMediumResolution: {
                type: 'LandscapeType'
            },
            surroundingLandscapeLowResolution: {
                type: 'LandscapeType'
            },
            comment: {
                type: 'string'
            }
        }
    },
    SoilType: {
        schema: {
            title: {
                type: 'string'
            }
        }
    },
    Citation: {
        hidden: true,
        populate: {
            index: 1,
            display: 1
        },
        schema: {
            species: {
                type: 'Species',
                inverse: 'citations',
                description: 'the species cited in the publication'
            },
            name: {
                type: 'string',
                description: 'the name of the species cited in the publication'
            },
            publication: {
                type: 'Publication',
                inverse: 'citations',
                description: 'the publication where the species has been described'
            }
        }
    },
    Publication: {
        aliases: {
            description: 'reference'
        },
        schema: {
            title: {
                type: 'string'
            },
            source: {
                type: 'string'
            },
            reference: {
                type: 'string'
            },
            link: {
                hidden: true,
                type: 'url'
            },
            comment: {
                type: 'string'
            }
        }
    },
    Gene: {
        hidden: true,
        schema: {
            title: {
                type: 'string',
                i18n: true,
                fallbackDefaultLang: true
            },
            id: {
                type: 'string'
            },
            comment: {
                type: 'string'
            }
        }
    },
    Primer: {
        hidden: true,
        schema: {
            sequence: {
                type: 'string'
            },
            gene: {
                type: 'Gene'
            },
            referencedIn: {
                type: 'Publication',
                multi: true
            },
            comment: {
                type: 'string'
            }
        }
    },
    Sequence: {
        schema: {
            individual: {
                type: 'Individual'
            },
            gene: {
                type: 'Gene'
            },
            forwardPrimer: {
                type: 'Primer'
            },
            reversePrimer: {
                type: 'Primer'
            },
            sequence: {
                type: 'string'
            },
            chromatogramLink: {
                type: 'string'
            },
            accessionNumber: { // ???
                type: 'string'
            },
            length: { // ???
                type: 'integer'
            },
            comment: {
                type: 'string'
            }
        },
        views: {
            index: {
                widgets: [
                    [{
                        type:'tableView',
                        fields: ['individual', 'gene', 'forwardPrimer', 'reversePrimer'],
                        limit: 15,
                        populate: 1,
                    }]
                ],
                search: {
                    field: 'individual.title',
                    placeholder: 'search a sequence on an individual'
                },
            },
            display: {
                populate: 1
            }
        }
    },
    GeoDatedFact: {
        views: {
            index: {
                widgets: [
                    [{
                        type: 'timeline',
                        startField: 'startDate',
                        endField: 'endDate',
                        populate: 1,
                    }],
                    [{
                        type: 'tableView',
                        populate: 1,
                        fields: ['subject', 'predicate', 'object', 'startDate', 'endDate', 'location']
                    }]
                ]
            },
            display: {
                actions: [
                    editAction,
                    deleteAction
                ]
            }
        },
        aliases: {
            description: 'note'
        },
        schema: {
            subject: {
                type: 'Thing'
            },
            predicate: {
                type: 'Predicate'
            },
            object: {
                type: 'Thing'
            },
            startDate: {
                type: 'date',
                dateFormat: 'L'
            },
            endDate: {
                type: 'date',
                dateFormat: 'L'
            },
            location: {
                type: 'Site'
            },
            value: {
                type: 'string'
            },
            note: {
                type: 'string'
            }
        }
    },
    Thing: {
        schema: {
            title: {
                type: 'string'
            }
        }
    },
    Predicate: {
        schema: {
            title: {
                type: 'string'
            }
        }
    },
    Fact: {
        views: {
            index: {
                widgets: [
                    [{
                        type: 'timeline',
                        contentField: 'title',
                        startField: 'startDate',
                        endField: 'endDate'
                    }],
                    [{
                        type: 'tableView',
                        populate: 1,
                        fields: ['title', 'what', 'who', 'startDate', 'endDate', 'where', 'why']
                    }]
                ]
            },
            display: {
                actions: [
                    editAction,
                    deleteAction
                ]
            }
        },
        aliases: {
            description: 'note'
        },
        schema: {
            title: {
                type: 'string'
            },
            what: {
                type: 'Topic',
                multi: true
            },
            startDate: {
                type: 'date',
                dateFormat: 'L'
            },
            endDate: {
                type: 'date',
                dateFormat: 'L'
            },
            where: {
                type: 'Site',
                multi: true
            },
            who: {
                type: 'SociologicalAgent'
            },
            sociologicalType: {
                type: 'SociologicalType',
                multi: true
            },
            why: {
                type: 'Reason',
                multi: true,
                description: "raisons qui explique le fait"
            },
            how: {
                type: 'Means',
                multi: true,
                description: "moyen (techniques, innovation sociale) mis en oeuvre"
            },
            note: {
                type: 'string'
            },
        }
    },
    Reason: {
        schema: {
            title: {
                type: 'string'
            }
        }
    },
    Means: {
        label: {
            en: {plural: 'Means'}
        },
        views: {
            display: {
                actions: [
                    editAction,
                    deleteAction
                ]
            }
        },
        schema: {
            title: {
                type: 'string'
            }
        }
    },
    SociologicalAgent: {
        schema: {
            title: {
                type: 'string'
            }
        }
    },
    SociologicalType: {
        schema: {
            title: {
                type: 'string'
            }
        }
    },
    Topic: {
        schema: {
            title: {
                type: 'string'
            }
        }
    }
};
