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
    
def format_loc_name(name):
    if name is None:
        return ''
    return ' '.join(i.capitalize() for i in name.split())
