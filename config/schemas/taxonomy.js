
module.exports = {
    meta: {
        instanceRdfPrefix: 'http://ceropath.org/instances/taxonomy',
    },
    properties: {
        title: {
            type: 'string'
        },

        description: {
            type: 'string',
            meta: {
                eureka: {
                    widget: 'markdown'
                }
            }
        },

        comment: {
            type: 'string',
            meta: {
                eureka: {
                    widget: 'textarea'
                }
            }
        },

        isExtinct: {
            type: 'boolean',
            label: 'extinct ?'
        },

        // commonNames: {
        //     hidden: true, // XXX TODO
        //     type: 'string',
        //     i18n: true,
        //     displayAllLanguages: true
        //     // in engligh, french, spanish, thai, lao and khmer
        // },

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
            type: 'number',
            validate: ['integer'],
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
            type: 'string',
            label: 'suborder',
            description: 'suborder rank',
            meta: {
                eureka: {
                    hidden: true
                }
            }
        },
        infraorderRank: {
            type: 'string',
            label: 'infraorder',
            description: 'infraorder rank',
            meta: {
                eureka: {
                    hidden: true
                }
            }
        },
        superfamilyRank: {
            type: 'string',
            label: 'superfamily',
            description: 'superfamily rank',
            meta: {
                eureka: {
                    hidden: true
                }
            }
        },
        familyRank: {
            type: 'string',
            label: 'family',
            description: 'family rank'
        },
        subfamilyRank: {
            type: 'string',
            label: 'subfamily',
            description: 'subfamily rank',
            meta: {
                eureka: {
                    hidden: true
                }
            }
        },
        tribeRank: { // not from MSW3
            type: 'string',
            label: 'tribe',
            description: 'tribe rank',
            meta: {
                eureka: {
                    hidden: true
                }
            }
        },
        divisionRank: { // not from MSW3
            type: 'string',
            label: 'division',
            description: 'division rank',
            meta: {
                eureka: {
                    hidden: true
                }
            }
        },
        groupsRank: {
            type: 'string',
            label: 'groups',
            description: 'groups rank',
            meta: {
                eureka: {
                    hidden: true
                }
            }
        },
        genusRank: {
            type: 'string',
            label: 'genus',
            description: 'genus rank'
        },
        subgenusRank: {
            type: 'string',
            label: 'subgenus',
            description: 'subgenus rank',
            meta: {
                eureka: {
                    hidden: true
                }
            }
        },
        speciesRank: {
            type: 'string',
            label: 'species',
            description: 'species rank'
        },
        subspeciesRank: {
            type: 'string',
            label: 'subspecies',
            description: 'subspecies rank',
            meta: {
                eureka: {
                    hidden: true
                }
            }
        },

        rankLevel: { // ???
            type: 'string',
            label: 'rank level'
        },

        msw3ID: {
            type: 'string',
            label: 'MSW3 reference',
            description: "reference id of Mammals Species of the World 3",
            meta: {
                eureka: {
                    hidden: true
                }
            }
        }
    },
    inverseRelationships: {
        individuals: {
            type: 'Individual',
            property: 'taxonomy'
        },
        references: {
            type: 'Reference',
            property: 'taxonomy'
        }
    }
};