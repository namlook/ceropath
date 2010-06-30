
from pipeline import Pipeline
from core import Core
from organism_classification import OrganismClassification
from species_measurement import SpeciesMeasurement
from responsible import Responsible
from publication import Publication
from institute import Institute
from sequence import Sequence
from gene import Gene
from primer import Primer
from individual import Individual
from site import Site
from rel_host_parasite import RelHostParasite

register_models = [
Pipeline,
Core,
OrganismClassification,
Responsible, 
Publication,
Institute,
Sequence,
Gene,
Primer,
Individual,
SpeciesMeasurement,
Site,
RelHostParasite,
]
