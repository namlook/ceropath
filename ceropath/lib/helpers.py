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

def markdownize(text):
    return markdown(text.decode('utf-8'))

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

from xml.etree import ElementTree

def clickify_svg(svg, db=None):
    root = ElementTree.fromstring(svg)
    root.attrib['xmlns:xlink'] = "http://www.w3.org/1999/xlink"
    individuals_list = [child.text.split()[0].lower() for child in root if child.tag == '{http://www.w3.org/2000/svg}text']
    species = dict((i['_id'], i['organism_classification']['$id']) for i in db.individual.find(
      {'_id':{'$in':individuals_list}},
      fields=['organism_classification.$id']
    ))
    for child in root:
        if child.tag == '{http://www.w3.org/2000/svg}text':
            individual_id = child.text.split()[0].lower()
            if species.get(individual_id):
                individual_link = root.makeelement('ns0:a', {'target':'_blank', 'xlink:href':"/individual/%s" % individual_id })
                individual_link.text = individual_id.upper()
                child.append(individual_link)
                species_link = root.makeelement('ns0:a', {'target':'_blank', 'fill': "#FFB010", 'xlink:href':"/species/%s" % species[individual_id]})
                species_link.text =  " (%s)" % species[individual_id].capitalize()
                child.append(species_link)
                child.text = ""
                child.attrib['fill'] = "#1139E5"
    return ElementTree.tostring(root)
