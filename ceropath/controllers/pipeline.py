# -*- coding:utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render
from ceropath.lib import phylogelib

log = logging.getLogger(__name__)
from pprint import pprint, pformat

class PipelineController(BaseController):

    def index(self):
        return render('pipeline/index.mako')

    def phyloexplorer(self):
        if 'file' in request.POST:
            tree = request.POST['file'].file.read()
        elif 'paste' in request.POST:
            tree = request.POST['paste']
        else:
            redirect('pipeline_index')
        # TODO add pipeline here
        tree = phylogelib.removeBootStraps(tree)
        return render('pipeline/phyloexplorer.mako', extra_vars = {
          'tree':phylogelib.getGraph(tree),
          'source':tree,
          'taxa_list':phylogelib.getTaxa(tree)
        })

    
