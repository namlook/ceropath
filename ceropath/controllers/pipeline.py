# -*- coding:utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render
from ceropath.lib import phylogelib
from ceropath.lib import helpers as h

log = logging.getLogger(__name__)

from pprint import pprint
from pypit import Pypit
from StringIO import StringIO
from uuid import uuid1
import os.path, os

class PipelineController(BaseController):

    def index(self):
        return render('pipeline/index.mako')

    def config(self):
        pipeline = self.db.config.get_from_id('pipeline')
        return render('pipeline/config.mako', extra_vars = {
          'programs':pipeline['programs']
        })
    
    def update_config(self):
        order = []
        field_names = ['path', 'name', 'shell', 'input', 'output', 'options']
        for i in request.POST:
            index = i.split('-')[0]
            if index not in order:
                order.append(index)
        programs = []
        for index in order:
            program = {}
            for field_name in field_names:
                program[field_name] = request.POST.get('%s-%s' % (index, field_name), None)
                if field_name == 'shell':
                    program[field_name] = bool(program[field_name])
            programs.append(program)
        pipeline = self.db.config.Pipeline.get_from_id('pipeline')
        pipeline['programs'] = programs
        pipeline.save()
        redirect(h.url_for('pipeline_index'))

    def phyloexplorer(self):
        if 'file' in request.POST:
            user_input = request.POST['file'].file.read()
        elif 'paste' in request.POST:
            user_input = request.POST['paste']
        else:
            redirect(h.url_for('pipeline_index'))
        pipeline_config = self.db.config.get_from_id('pipeline')['programs']
        pypit = Pypit(pipeline_config)
        uid = uuid1()
        file_name = os.path.join('data', 'sequence-%s.txt' % uid)
        open(file_name, 'w').write(user_input)
        input_file = open(file_name, 'r')
        tree = pypit.run(input_file=input_file)
        os.remove(file_name)
        #tree = phylogelib.removeBootStraps(tree)
        #graph = phylogelib.getGraph(tree)
        #taxa_list = phylogelib.getTaxa(tree)
        return render('pipeline/phyloexplorer.mako', extra_vars = {
          'tree':'',#graph
          'source':tree,
          'taxa_list':''#taxa_list,
        })

    
