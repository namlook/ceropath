import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render
from ceropath.lib.helpers import markdownize
from mongokit import IS, DotCollapsedDict
from datetime import datetime
import os

log = logging.getLogger(__name__)

class QueryController(BaseController):

    requires_auth_actions = ['index', 'run']

    family_genus = {}
    genus_species = {}
    country_province = {}
    province_place = {}
    typo_low_medium = {}

    microparasites = []
    macroparasites = []
    former_identification = []
    physiologic_features = []
    samples = []
    measures = []
    individual = []
    genes = []
    mission_numbers = []
    sites = []

    def __before__(self, action):
        super(QueryController, self).__before__(action)
        if not QueryController.family_genus or not QueryController.genus_species:
            for item in self.db.organism_classification.find({'type':'mammal', 'internet_display':True}, 
              fields=['taxonomic_rank.family', 'taxonomic_rank.genus', 'taxonomic_rank.species']):
                if item['taxonomic_rank']['family'] and item['taxonomic_rank']['family'] not in QueryController.family_genus:
                        QueryController.family_genus[item['taxonomic_rank']['family']] = set([])
                QueryController.family_genus[item['taxonomic_rank']['family']].add(item['taxonomic_rank']['genus'].capitalize())
                if item['taxonomic_rank']['genus'] and item['taxonomic_rank']['genus'] not in QueryController.genus_species:
                        QueryController.genus_species[item['taxonomic_rank']['genus']] = set([])
                QueryController.genus_species[item['taxonomic_rank']['genus']].add(item['taxonomic_rank']['species'])
        if not QueryController.country_province or not QueryController.province_place :
            for item in self.db.site.find(fields=['province', 'country']):
                if not item['country'] in QueryController.country_province:
                    QueryController.country_province[item['country']] = set([])
                QueryController.country_province[item['country']].add(item['province'])
                if not item['province'] in QueryController.province_place:
                    QueryController.province_place[item['province']] = set([])
                QueryController.province_place[item['province']].add(item['_id'])
        if not QueryController.typo_low_medium:
            for item in self.db.individual.find({'internet_display':True},
              fields=['trapping_informations.eco_typology.low', 'trapping_informations.eco_typology.medium']):
                low = item['trapping_informations']['eco_typology']['low']
                medium = item['trapping_informations']['eco_typology']['medium']
                if low:
                    if low not in QueryController.typo_low_medium:
                        QueryController.typo_low_medium[low] = set([])
                    QueryController.typo_low_medium[low].add(medium)
        # filter 
        if not QueryController.microparasites:
            res = []
            [res.extend([j['method'] for j in i['microparasites']]) for i in self.db.individual.find(fields=['microparasites.method'])]
            QueryController.microparasites = list(sorted(set(res)))
        if not QueryController.macroparasites:
            res = []
            [res.extend([j['name'] for j in i['macroparasites']]) for i in self.db.individual.find(fields=['macroparasites.name'])]
            QueryController.macroparasites = list(sorted(set(res)))
        if not QueryController.former_identification:
            QueryController.former_identification = list(sorted(set([i['type'] for i in self.db.former_identification.find(fields=['type'])])))
        if not QueryController.physiologic_features:
            res = []
            [res.extend([j['type'] for j in i['physiologic_features']]) for i in self.db.individual.find(fields=['physiologic_features'])]
            QueryController.physiologic_features = list(sorted(set(res)))
        if not QueryController.samples:
            res = []
            [res.extend([j['name'] for j in i['samples']]) for i in self.db.individual.find(fields=['samples'])]
            QueryController.samples = list(sorted(set(res)))
        if not QueryController.individual:
            QueryController.individual = list(sorted(u' >> '.join(k.split('.')) for k in DotCollapsedDict(self.db.individual.find_one())))
            for i in ['_id', 'internet_display', 'measures', 'physiologic_features', 'samples', 'microparasites', 'macroparasites']:
                QueryController.individual.remove(i)
        if not QueryController.measures:
            res = []
            [res.extend([j['trait'] for j in i['measures']]) for i in self.db.individual.find(fields=['measures'])]
            QueryController.measures = list(sorted(set(res)))
        if not QueryController.genes:
            QueryController.genes = list(sorted(set([i['_id'] for i in self.db.gene.find(fields=['_id'])])))
        if not QueryController.mission_numbers:
            QueryController.mission_numbers = list(sorted(set([i['mission']['remark'] for i in self.db.individual.find(fields=['mission.remark'])])))
        if not QueryController.sites:
            d = self.db.site.find_one()
            del d['eco_typology']
            QueryController.sites = list(sorted(u' >> '.join(k.split('.')) for k in DotCollapsedDict(d)))

    def index(self):
        return render('query/index.mako', extra_vars={
           'title': 'query the database', 
           'family_genus': self.family_genus,
           'country_province': self.country_province,
           'typo_low_medium': self.typo_low_medium,
           # filter
           'microparasites': self.microparasites,
           'macroparasites': self.macroparasites,
           'former_identification': self.former_identification,
           'physiologic_features': self.physiologic_features,
           'samples': self.samples,
           'individual': self.individual,
           'measures': self.measures,
           'genes': self.genes,
           'mission_numbers': self.mission_numbers,
           'sites': self.sites,
        })

    def expand(self):
        values = request.params.get('values', '').strip(u'\xa0').split(u'\xa0')
        name = request.params.get('name')
        results = []
        mapping = {
            'family': self.family_genus,
            'genus': self.genus_species,
            'country': self.country_province,
            'province': self.province_place,
            'low': self.typo_low_medium,
        }
        if name in mapping:
            for item in values:
                l = mapping[name][item.lower()]
                results.extend(list(l))
            response.headers['Content-type'] = 'application/json'
            import anyjson
            return anyjson.serialize(list(sorted(results)))

    def run(self):
        target = request.GET.pop('target', 'html')
        query = request.GET.pop('query', {})
        filters = request.GET.pop('filters', {})
        if not query or not filters:
            query = {'internet_display': True}
            organism_classification_query = {}
            site_query = {}
            for k, v in request.GET.iteritems():
                if k.startswith('filter::'):
                    name = k.split('filter::')[1]
                    if name not in filters:
                        filters[name] = []
                    filters[name].append(v)
                    continue
                if v:
                    v = v.strip(u'\xa0')
                    if k == 'individual_id':
                        query['_id'] = v.lower()
                    elif k == 'sex':
                        if not 'sex' in query:
                            query['sex'] = {'$in': []}
                        query['sex']['$in'].append(v.lower())
                    elif k == 'mission':
                        if not 'mission.remark' in query:
                            query['mission.remark'] = {'$in':[]}
                        query['mission.remark']['$in'].append(v)
                    elif k in ['family', 'genus', 'species']:
                        _k = 'taxonomic_rank.%s' % k
                        if _k not in organism_classification_query:
                            organism_classification_query[_k] = {'$in':[]}
                        organism_classification_query[_k]['$in'].append(v.lower())
                    elif k in ['country', 'province', 'place']:
                        if k == 'place':
                            k = '_id'
                        if k not in site_query:
                            site_query[k] = {'$in':[]}
                        site_query[k]['$in'].append(v)
                    elif k in ['low', 'medium']:
                        query['trapping_informations.eco_typology.%s' % k] = v
                    elif k in ['dissection_date', 'dissection_date_start', 'dissection_date_end']:
                        v = datetime.strptime(v, '%m/%d/%y')
                        if k == 'dissection_date':
                            query['dissection_date'] = v
                        if k == 'dissection_date_start':
                            if 'dissection_date' not in query:
                                query['dissection_date'] = {}
                            if isinstance(query['dissection_date'], dict):
                                query['dissection_date']['$gt'] = v
                        if k == 'dissection_date_end':
                            if 'dissection_date' not in query:
                                query['dissection_date'] = {}
                            if isinstance(query['dissection_date'], dict):
                                query['dissection_date']['$lt'] = v
            if organism_classification_query:
                query['organism_classification.$id'] = {
                  '$in':[i['_id'] for i in self.db.organism_classification.find(organism_classification_query, fields=['_id'])]
                }
            if site_query:
                query['trapping_informations.site.$id'] = {
                  '$in':[i['_id'] for i in self.db.site.find(site_query, fields=['_id'])]
                }
        else:
            filters = eval(filters)
            query = eval(query)
        if filters.get('former_identification'):
            _results = self.db.individual.find(query, fields=['_id'])
            results = self.db.former_identification.find({'individual.$id':{'$in':[i['_id'] for i in _results]}}).sort('individual.$id')
            if target == 'csv':
                res = render('query/results_former_csv.mako', extra_vars={
                    'title': 'results for your query',
                    'query': query,
                    'results': results,
                    'filters': filters,
                    'db':self.db,
                })
                response.headers['Content-type'] = 'text/csv; charset=utf-8'
                response.headers['Content-disposition'] = 'attachment; filename=results.csv'
                return ''.join([i for i in res.split('\n') if i.strip()]).replace(';|||', '\n').strip()
            return render('query/results_former.mako', extra_vars={
                'title': 'results for your query',
                'query': query,
                'results': results,
                'filters': filters,
                'db':self.db,
            })
        results = self.db.individual.find(query).sort('_id')
        if target == 'csv':
            res = render('query/results_csv.mako', extra_vars={
                'title': 'results for your query',
                'query': query,
                'results': results,
                'filters': filters,
                'db':self.db,
            })
            response.headers['Content-type'] = 'text/csv; charset=utf-8'
            response.headers['Content-disposition'] = 'attachment; filename=results.csv'
            return ''.join([i for i in res.split('\n') if i.strip()]).replace(';:::', '\n').strip()
        return render('query/results.mako', extra_vars={
                'title': 'results for your query',
                'query': query,
                'results': results,
                'filters': filters,
                'db':self.db,
            })

    def infos(self):
        path = os.path.join('ceropath', 'public', 'data', 'query')
        if 'documentation.txt' in os.listdir(path):
            content = open(os.path.join(path, 'documentation.txt')).read()
        else:
            content = "Not informations about this pipeline was found... sorry."
        return render('query/infos.mako', extra_vars={
            'title': 'Queries engine documentation',
            'content': content,
        })

