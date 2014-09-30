#!/usr/bin/env node

var fs = require('fs');
var JSONStream = require('JSONStream');
var _ = require('underscore');
_.str = require('underscore.string');

var Eureka = require('eurekapi');

(function() {
    "use strict";

    var db = new Eureka({
        name: 'Ceropath',
        version: 1,
        port: 4000,
        database: {
            adapter: 'rdf',
            config: {
                store: 'virtuoso',
                graphURI: 'http://ceropath.org'
            }
        },
        schemas: require('../app/schemas')
    }).getDatabase();

    var hasData = function(value) {
        // return true if the value is not undefined or null
        return [undefined, null].indexOf(value) === -1;
    };

    var clean = function(string) {
        string = string.replace(/\\/g, '\\\\');
        return _.str.clean(string);
    };

    var cleanTags = function(string) {
        return clean(_.str.stripTags(string));
    };

    var removePunctuation = function(string) {
        // remove all punctuation except "'" in words
        string = string.replace(/[\-=_!"#%&*{},.\/:;?\(\)\[\]@\\$\^*+<>~`\u00a1\u00a7\u00b6\u00b7\u00bf\u037e\u0387\u055a-\u055f\u0589\u05c0\u05c3\u05c6\u05f3\u05f4\u0609\u060a\u060c\u060d\u061b\u061e\u061f\u066a-\u066d\u06d4\u0700-\u070d\u07f7-\u07f9\u0830-\u083e\u085e\u0964\u0965\u0970\u0af0\u0df4\u0e4f\u0e5a\u0e5b\u0f04-\u0f12\u0f14\u0f85\u0fd0-\u0fd4\u0fd9\u0fda\u104a-\u104f\u10fb\u1360-\u1368\u166d\u166e\u16eb-\u16ed\u1735\u1736\u17d4-\u17d6\u17d8-\u17da\u1800-\u1805\u1807-\u180a\u1944\u1945\u1a1e\u1a1f\u1aa0-\u1aa6\u1aa8-\u1aad\u1b5a-\u1b60\u1bfc-\u1bff\u1c3b-\u1c3f\u1c7e\u1c7f\u1cc0-\u1cc7\u1cd3\u2016\u2017\u2020-\u2027\u2030-\u2038\u203b-\u203e\u2041-\u2043\u2047-\u2051\u2053\u2055-\u205e\u2cf9-\u2cfc\u2cfe\u2cff\u2d70\u2e00\u2e01\u2e06-\u2e08\u2e0b\u2e0e-\u2e16\u2e18\u2e19\u2e1b\u2e1e\u2e1f\u2e2a-\u2e2e\u2e30-\u2e39\u3001-\u3003\u303d\u30fb\ua4fe\ua4ff\ua60d-\ua60f\ua673\ua67e\ua6f2-\ua6f7\ua874-\ua877\ua8ce\ua8cf\ua8f8-\ua8fa\ua92e\ua92f\ua95f\ua9c1-\ua9cd\ua9de\ua9df\uaa5c-\uaa5f\uaade\uaadf\uaaf0\uaaf1\uabeb\ufe10-\ufe16\ufe19\ufe30\ufe45\ufe46\ufe49-\ufe4c\ufe50-\ufe52\ufe54-\ufe57\ufe5f-\ufe61\ufe68\ufe6a\ufe6b\uff01-\uff03\uff05-\uff07\uff0a\uff0c\uff0e\uff0f\uff1a\uff1b\uff1f\uff20\uff3c\uff61\uff64\uff65]+/g, " ");
        string = _.str.trim(string, "'");
        return _.str.clean(string);
    };

    var readJSON = function(filename, processFunc, callback) {
        var stream = fs.createReadStream(filename, {encoding: 'utf8'});
        var parser = JSONStream.parse();

        stream.pipe(parser);

        parser.on('root', function(obj) {
            processFunc(obj, callback);
        });
    };


    var processSpecies = function(data, callback) {
        // console.log(data);return;

        var ge = {};
        ge._id = _.str.slugify(data._id);
        ge.title = _.str.capitalize(data._id);

        ge.msw3ID = data.id_msw3;

        // taxonomic ranks
        var taxonomicFields = [
            'kingdom', 'phylum', 'class', 'order', 'suborder', 'infraorder',
            'superfamily', 'family', 'subfamily', 'tribe', 'division',
            'groups', 'genus', 'subgenus', 'species', 'subspecies'
        ];

        taxonomicFields.forEach(function(fieldName) {
            if (data.taxonomic_rank[fieldName]) {
                var capitalizedName = _.str.capitalize(fieldName);
                var capitalizedValue = _.str.capitalize(data.taxonomic_rank[fieldName]);
                ge['taxonomic'+capitalizedName+'Rank'] = capitalizedValue;
            }
        });

        ge.taxonLevel = data.taxonomic_rank.taxon_level;
        ge.isExtinct = data['extinct'];

        // IUCN
        if (data.iucn.id) {
            ge.iucn = data.iucn.id;
        }
        if (data.iucn.status) {
            ge.iucnRedListStatus = data.iucn.status;
        }

        if (data.iucn.red_list_criteria_version) {
            ge.iucnRedListCriteriaVersion = data.iucn.red_list_criteria_version;
        }

        if (data.iucn.year_assessed) {
            ge.iucnYearAssessed = data.iucn.year_assessed;
        }

        if (data.iucn.trend) {
            ge.iucnTrend = data.iucn.trend;
        }

        // comment
        if (data.remark) {
            ge.comment = cleanTags(data.remark);
        }

        // species discovery
        if (data.reference.type.species) {
            ge.discoveryName = cleanTags(data.reference.type.species);
        }

        if (data.reference.type.locality) {
            ge.discoveryLocality = cleanTags(data.reference.type.locality);
        }

        if (data.reference.biblio.date) {
            ge.discoveryYear = parseInt(data.reference.biblio.date, 10);
        }

        if (data.reference.biblio.date) {
            ge.discoveryAuthor = cleanTags(data.reference.biblio.author);
        }

        var species = new db.Species(ge);

        // common names
        var commonNameFields = [
            {name: 'english', lang: 'en'},
            {name: 'french', lang: 'fr'},
            {name: 'spanish', lang: 'es'},
            {name: 'thai', lang: 'th'},
            {name: 'lao', lang: 'lo'},
            {name: 'khmer', lang: 'km'}
        ];

        commonNameFields.forEach(function(field) {
            if (data.name.common[field.name]) {
                species.set('commonNames', data.name.common[field.name], field.lang);
            }
        });

        // citations
        data.citations.forEach(function(cit) {
            if (_.str.slugify(cit.name).length > 3) {
                var citationID = cit.pubref.$id+'-'+_.str.slugify(cit.name);
                var citation = new db.Citation();
                citation.set('_id', citationID);
                citation.set('name', _.str.capitalize(removePunctuation(cit.name)));
                var publication = new db.Publication({_id: cit.pubref.$id});
                citation.set('publication', publication.reference());
                citation.set('species', species.reference());
                console.log(citation.serialize()); // output
                // species.push('citations', citation.reference());
            }
        });

        // synonyms
        data.synonyms.forEach(function(syn) {
            if (_.str.slugify(syn.name).length > 3) {
                var citation = new db.Citation();
                var citationID = syn.pubref.$id+'-'+_.str.slugify(syn.name);
                citation.set('_id', citationID);
                citation.set('name', _.str.capitalize(removePunctuation(syn.name)));
                var publication = new db.Publication({_id: syn.pubref.$id});
                citation.set('publication', publication.reference());
                citation.set('species', species.reference());
                console.log(citation.serialize()); // output
                // species.push('synonyms', citation.reference());
            }
        });

        // finally serialize the genetical entity
        console.log(species.serialize()); // output
    };

    var processPublication = function(data, callback) {
        // console.log(data);return;
        var pub = {};
        pub._id = data._id;
        pub.source = cleanTags(data.source);
        pub.reference = cleanTags(data.reference);
        pub.link = data.link;

        // generate title in format: author (year). Example: Wilson D. (2005)
        pub.title = cleanTags(data.reference.split('.')[0]);

        var year = data.reference.match(/\d{4}/);
        if (year) {
            year = parseInt(year[0], 10);
            pub.title += " ("+year+")";
        }

        var publication = new db.Publication(pub);

        // finally serialize the publication
        console.log(publication.serialize()); // output
    };

    var processIndividual = function(data, callback) {
        // console.log(data);return;

        var ind = {};
        ind._id = data._id;
        ind.title = ind._id;

        var speciesId = _.str.slugify(data.organism_classification.$id);
        ind.species = new db.Species({_id: speciesId}).reference();

        if (data.sex) {
            var gender;
            if (data.sex === 'f') {
                gender = new db.Gender({_id: 'female'});
            } else if (data.sex === 'm') {
                gender = new db.Gender({_id: 'male'});
            } else {
                gender = new db.Gender({_id: 'unknown'});
            }
            ind.gender = gender.reference();
        }

        if (data.adult) {
            ind.maturity = data.adult;
        }

        ind.voucherBarcoding = data.voucher_barcoding;
        ind.inSkullCollection = data.skull_collection;

        if (data.dissection_date) {
            ind.dissectionDate = new Date(data.dissection_date.$date);
        }

        // trapping informations
        ind.trappingMethod = data.trapping_informations.origin_how;
        ind.trapAccuracy = data.trapping_informations.trap_accuracy;
        ind.trappingID = data.trapping_informations.field_id;
        ind.trappedAlive = data.trapping_informations.alive;

        if (data.trapping_informations.site) {
            var siteID = _.str.slugify(data.trapping_informations.site.$id);
            var site = new db.Site({_id: siteID});
            console.log(site.serialize()); // output
            ind.trappingSite = site.reference();
        }

        ['hight', 'medium', 'low'].forEach(function(resolution) {
            var resolutionValue = data.trapping_informations.eco_typology[resolution];
            if (resolutionValue) {
                var fieldName = 'trappingLandscape'+_.str.capitalize(resolution)+'Resolution';
                resolutionValue = clean(resolutionValue.toLowerCase());
                var landscapeTypeID = _.str.slugify(resolutionValue);
                var landscapeType = new db.LandscapeType();
                landscapeType.set('_id', landscapeTypeID);
                landscapeType.set('label', _.str.humanize(landscapeTypeID), 'en');
                console.log(landscapeType.serialize()); // output
                ind[fieldName] = landscapeType;
            }
        });

        if (data.remark) {
            ind.comment = cleanTags(data.remark);
        }

        // physiological features
        data.physiologic_features.forEach(function(feature) {
            if (feature.type === 'Vagina') {
                ind.vagina = feature.value;
            } else if (feature.type === "Teats") {
                ind.teats = feature.value;
            } else if (feature.type === "Mammae_formula") {
                ind.mammaeDistribution = feature.value;
            } else if (feature.type === "Embryos Left" && feature.value) {
                ind.leftSideEmbryosNumber = parseInt(feature.value, 10);
            } else if (feature.type === "Embryos Right" && feature.value) {
                ind.rightSideEmbryosNumber = parseInt(feature.value, 10);
            } else if (feature.type === 'Testes') {
                ind.testesOutput = feature.value;
            } else if (feature.type === "Testes length" && feature.value) {
                var length = parseFloat(feature.value.replace(',', '.'));
                if (!isNaN(length)) {
                    ind.testesLength = length;
                }
            } else if (feature.type === "Seminal_vesicule") {
                ind.seminalVesicule = feature.value;
            } else if (feature.type === "sexual_maturity" && feature.value) {
                if (feature.value === 'yes') {
                    ind.sexualMaturity = true;
                } else if (feature.value === 'no') {
                    ind.sexualMaturity = false;
                }
            }  else if (feature.type === "M3_development") {
                ind.m3Development = feature.value;
            }
        });

        // measurements
        var traitFieldNames = {
            'Head & Body (mm)': 'headBodyMeasurement',
            'Tail (mm)': 'tailMeasurement',
            'Foot (mm)': 'footMeasurement',
            'Ear (mm)': 'earMeasurement',
            'Weight (g)': 'weighMeasurement',
            'Head (mm)': 'headMeasurement',
            'Breadth of Rostrum  (mm) (M01)': 'breadthOfRostrumMeasurement',
            'Length of rostrum (mm) (M02)': 'lengthOfRostrumMeasurement',
            'OccipitoNasal Length (mm) (M03)': 'occipitoNasalLengthMeasurement',
            'Interorbital Breadth (mm) (M04)': 'interorbitalBreadthMeasurement',
            'Breath of BrainCase (mm) (M05)': 'breathOfBrainCaseMeasurement',
            'Zygomatic Breadth (mm) (M06)': 'zygomaticBreadthMeasurement',
            'Breadth of Incisive Foramina (mm) (M07)': 'breadthOfIncisiveForaminaMeasurement',
            'Breadth of first upper Molar (mm) (M08)': 'breadthOfFirstUpperMolarMeasurement',
            'Length of Diastema (mm) (M09)': 'lengthOfDiastemaMeasurement',
            'Lenght of Incisive Foramina (mm) (M10)': 'lenghtOfIncisiveForaminaMeasurement',
            'Lenght of Bony Palate (mm) (M11)': 'lenghtOfBonyPalateMeasurement',
            'PostPalatal Length (mm) (M12)': 'postPalatalLengthMeasurement',
            'Length of auditory Bulla (mm) (M13)': 'lengthOfAuditoryBullaMeasurement',
            'Breadth of Mesopterygoid Fossa (mm) (M14)': 'breadthOfMesopterygoidFossaMeasurement',
            'Breadth of Bony Palate at first  (mm) (M15)': 'breadthOfBonyPalateAtfirstMeasurement',
            'Crown Length of Maxillary Molar  (mm) (M16)': 'crownLengthOfMaxillaryMolarMeasurement',
            'Breath of Zygomatic Plate (mm) (M17)': 'breathOfZygomaticPlateMeasurement',
            'Height of Braincase (mm) (M18)': 'heightOfBraincaseMeasurement',
            'Spleen weight (mg)': 'spleenWeightMeasurement',
            'Agpd (mm)': 'agpdMeasurement',
        };

        data.measures.forEach(function(measure) {
            if (measure.value) {
                var fieldName = traitFieldNames[measure.trait];
                value = measure.value.replace(',', '.').replace('>', '').replace('<', '');
                var value = parseFloat(value);
                if (!isNaN(value)) {
                    ind[fieldName] = value;
                }
            }
        });

        var individual = new db.Individual(ind);
        // finally serialize the individual
        console.log(individual.serialize()); // output
    };

    var processSite = function(data, callback) {
        // return console.log(data);

        var sit = {};
        sit._id = _.str.slugify(data._id);
        sit.title = sit._id;

        sit.region = data.region;
        sit.country = data.country;
        sit.province = data.province;
        sit.district = data.district;
        sit.village = data.village;

        sit.isCeropathSite = data.ceropath_sites;

        // houses presence
        if (data.house.number) {
            sit.averageHousesNumber = parseInt(data.house.number, 10);
        }
        if (data.house.distance) {
            sit.averageHousesDistance = parseInt(data.house.distance, 10);
        }

        // GPS coords
        if (data.coord_wgs.dll_lat) {
            sit.geoWgsLat = parseFloat(data.coord_wgs.dll_lat);

        }

        if (data.coord_wgs.dll_long) {
            sit.geoWgsLong = parseFloat(data.coord_wgs.dll_long);

        }

        if (data.coord_wgs.elevation) {
            sit.geoWgsAlt = parseFloat(data.coord_wgs.elevation);

        }

        // surrounding landscapes
        ['high', 'medium', 'low'].forEach(function(resolution) {
            var value = data.eco_typology[resolution];
            if (value) {
                var fieldName = 'surroundingLandscape'+_.str.capitalize(resolution)+'Resolution';
                var landscapeTypeID = _.str.slugify(clean(value.toLowerCase()));
                var landscapeType = new db.LandscapeType();
                landscapeType.set('_id', landscapeTypeID);
                landscapeType.set('label', _.str.humanize(landscapeTypeID), 'en');
                console.log(landscapeType.serialize()); // output
                sit[fieldName] = landscapeType.reference();
            }
        });

        // comment
        sit.comment = null;
        if (data.surrounding_landscape) {
            sit.comment = cleanTags(data.surrounding_landscape);
        }
        if (data.remark) {
            sit.comment += ' '+cleanTags(data.remark);
            sit.comment = clean(sit.comment);
        }

        var site = new db.Site(sit);
        // finally serialize the site
        console.log(site.serialize()); // output
    };

    var processGene = function(data, callback) {
        // return console.log(data);
        var gene = new db.Gene();
        var geneID = _.str.slugify(data._id);
        gene.set('_id', geneID);
        gene.set('id', geneID);
        gene.set('title', data.remark, 'en');

        // finally serialize the gene
        console.log(gene.serialize()); // output
    };

    var processPrimer = function(data, callback) {
        // return console.log(data);

        var primer = new db.Primer();
        primer.set('_id', data._id);
        primer.set('sequence', data.sequence);

        data.pubref.forEach(function(pubref) {
            var publication = new db.Publication({_id: pubref.$id});
            primer.push('referencedIn', publication.reference());
        });

        if (data.gene) {
            if (_.str.startsWith(data.gene.$id, "irbp")) {
                data.gene.$id = "irbp "+data.gene.$id.slice(-1);
            }
            var gene = new db.Gene({_id: _.str.slugify(data.gene.$id)});
            primer.set('gene', gene.reference());
        }

        // finally serialize the gene
        console.log(primer.serialize()); // output
    };

    var processSequence = function(data, callback) {
        // return console.log(data);

        var seq = {};
        var individual = new db.Individual({_id: data.individual.$id});
        seq.individual = individual.reference();

        var gene = new db.Gene({_id: _.str.slugify(data.gene.$id)});
        seq.gene = gene.reference();

        if (data.primer.forward) {
            var forwardPrimer = new db.Primer({_id: data.primer.forward.$id});
            seq.forwardPrimer = forwardPrimer.reference();
        }
        if (data.primer.reverse) {
            var reversePrimer = new db.Primer({_id: data.primer.reverse.$id});
            seq.reversePrimer = reversePrimer.reference();
        }

        seq.sequence = data.sequence;
        seq.chromatogramLink = data.chromatogram_link;
        seq.accessionNumber = data.accession_number;
        seq['length'] = data['length'];

        if (data.remark && !_.str.startsWith(data.remark, 'C:')) {
            seq.comment = cleanTags(data.remark);
        }

        var sequence = new db.Sequence(seq);

        // finally serialize the sequence
        console.log(sequence.serialize());
    };

    // var processSpeciesMeasurement = function(data, callback) {
    //     return console.log(data);
    // };

    var generateGenders = function() {
        var female = new db.Gender();
        female.set('_id', 'female');
        female.set('label', 'female', 'en');
        female.set('label', 'femelle', 'fr');
        console.log(female.serialize()); // output

        var male = new db.Gender();
        male.set('_id', 'male');
        male.set('label', 'male', 'en');
        male.set('label', 'mâle', 'fr');
        console.log(male.serialize()); // output

        var unknown = new db.Gender();
        unknown.set('_id', 'unknown');
        unknown.set('label', 'unknown', 'en');
        unknown.set('label', 'inconnu', 'fr');
        console.log(unknown.serialize()); // output
    };

    readJSON('../data/json/organism_classification.json', processSpecies);
    readJSON('../data/json/publication.json', processPublication);
    readJSON('../data/json/individual.json', processIndividual);
    readJSON('../data/json/site.json', processSite);
    readJSON('../data/json/gene.json', processGene);
    readJSON('../data/json/primer.json', processPrimer);
    readJSON('../data/json/sequence.json', processSequence);
    generateGenders();
    // readJSON('../data/json/species_measurement.json', processSpeciesMeasurement);
})();

