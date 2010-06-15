
from pipeline import Pipeline
from core import Core
from organism_classification import Mammal, OrganismClassification, Parasite
from responsible import Responsible
from publication import Publication
from institute import Institute

register_models = [Pipeline, Core, Mammal, Parasite, OrganismClassification,
  Responsible, Publication, Institute]
