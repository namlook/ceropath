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
        field_names = ['name', 'cmd', 'output_ext', 'use_stdin']
        for i in request.POST:
            index = i.split('-')[0]
            if index not in order:
                order.append(index)
        programs = []
        for index in order:
            program = {}
            for field_name in field_names:
                program[field_name] = request.POST.get('%s-%s' % (index, field_name), None)
                if field_name == 'use_stdin':
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
        file_name = 'sequence-%s.fas' % uid
        file_path = os.path.join('data', 'pipeline', file_name)
        open(file_path, 'w').write(user_input)
        tree = pypit.run(file_name='sequence-%s.fas' % uid, cwd=os.path.join('data', 'pipeline'))
        svg_path = os.path.join('ceropath', 'public', 'usrdata', file_name+".afa.phy.mat.nwk.svg")
        open(svg_path, 'w').write(h.clickify_svg(tree, self.db))
        #tree = phylogelib.removeBootStraps(tree)
        #graph = phylogelib.getGraph(tree)
        #taxa_list = phylogelib.getTaxa(tree)
        return render('pipeline/phyloexplorer.mako', extra_vars = {
          'tree':'',#graph,
          'svg_path': os.path.join('/', 'usrdata', file_name+".afa.phy.mat.nwk.svg"),
          'source':tree,
          'taxa_list':'',#taxa_list,
        })

    
