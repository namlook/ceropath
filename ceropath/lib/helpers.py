"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password

from pylons import url
from routes import url_for

from webhelpers.html import literal
from markdown import markdown
from ceropath import uimodules as ui

from webhelpers.pylonslib import Flash as _Flash
success_flash = _Flash('success')
failure_flash = _Flash('failure')

def markdownize(text):
    # wants unicode
    return markdown(text)

import re
REX_DATE = re.compile('\d{4}')

def author_date_from_citation(citation):
    splitter = "."
    author = citation.split(splitter)[0].strip()
    date = REX_DATE.findall(citation)
    if len(date):
       date = date[0] 
    if date:
        return "%s (%s)" % (author, date)
    return author

try:
    from xml.etree import ElementTree
except: #python 2.4
    from elementtree import ElementTree

def clickify_svg(svg, db, users_individuals):
    root = ElementTree.fromstring(svg)
    root.attrib['xmlns:xlink'] = "http://www.w3.org/1999/xlink"
    individuals_list = [child.text.split()[0].lower() for child in root if child.tag == '{http://www.w3.org/2000/svg}text']
    species = dict((i['_id'], {'species_id':i['organism_classification']['$id'],'voucher_barcoding':i['voucher_barcoding']}) for i in db.individual.find(
      {'_id':{'$in':individuals_list}},
      fields=['organism_classification.$id', 'voucher_barcoding']
    ))
    for child in root:
        if child.tag == '{http://www.w3.org/2000/svg}text':
            individual_id = child.text.split()[0].lower()
            fill_color = ""
            if individual_id in users_individuals:
                fill_color = "#FF0000"
            print fill_color or '#1139E5', individual_id
            if species.get(individual_id):
                if species[individual_id]['voucher_barcoding']:
                    individual_link = root.makeelement('ns0:a', {'target':'_blank', 'fill': fill_color or '#1139E5', 'xlink:href':"/individual/%s" % individual_id })
                    individual_link.text = individual_id.upper()
                    child.append(individual_link)
                    child.text = ""
                else:
                    child.text = individual_id.upper()
                species_link = root.makeelement('ns0:a', {'target':'_blank', 'fill': fill_color or "#FFB010", 'xlink:href':"/species/%s" % species[individual_id]['species_id']})
                species_link.text =  " (%s)" % species[individual_id]['species_id'].capitalize()
                child.append(species_link)
            child.attrib['fill'] = fill_color or "#FFFFF"
    return ElementTree.tostring(root)
