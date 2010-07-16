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
        pipelines = list(self.db.pipeline.find(fields=['_id']))
        return render('pipeline/index.mako', extra_vars={
            'pipelines': pipelines, 
        })

    def new(self):
        # use jquery tools forms validation
        return render('pipeline/new.mako')

    def create(self):
        pipeline = self.db.pipeline.Pipeline()
        pprint(request.POST)
        _id = request.POST.pop('name')
        if not _id:
            h.failure_flash("name is required")
            redirect(h.url_for('pipeline_new'))
        elif self.db.pipeline.get_from_id(_id):
            h.failure_flash("name already token")
            redirect(h.url_for('pipeline_new'))
        programs = {}
        for field, value in request.POST.iteritems():
            index, name = field.split('-')
            if index not in programs:
                programs[index] = {}
            programs[index][name] = value
        for index in programs:
            prog = {'cmd':None, 'use_stdin': False, 'output_ext': None}
            for field, value in programs[index].iteritems():
                if value:
                    prog[field] = value
                    if field == 'use_stdin':
                        prog[field] = bool(value)
            pipeline['programs'].append(prog)
        pipeline['_id'] = _id
        try:
            pipeline.save()
        except Exception, e:
            h.failure_flash(e)
            redirect(h.url_for('pipeline_new'))
        h.success_flash("pipeline saved")
        redirect(h.url_for('pipeline_list'))
 
    def list(self):
        pipelines = list(i['_id'] for i in self.db.pipeline.find(fields=['_id']))
        return render('pipeline/list.mako', extra_vars = {
          'pipelines': pipelines,
        })
    
    def edit(self, id):
        pipeline = self.db.pipeline.get_from_id(id)
        return render('pipeline/config.mako', extra_vars = {
          'programs':pipeline['programs'],
          '_id': id,
        })
    
    def update(self, id):
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
                if program[field_name]:
                    program[field_name] = program[field_name].strip()
                if field_name == 'use_stdin':
                    program[field_name] = bool(program[field_name])
            programs.append(program)
        pipeline = self.db.pipeline.Pipeline.get_from_id(id)
        pipeline['programs'] = programs
        pipeline.save()
        redirect(h.url_for('pipeline_index'))

    def delete(self, id):
        self.db.pipeline.remove({'_id': id})
        redirect(h.url_for('pipeline_list'))

    def phyloexplorer(self):
        if 'file' in request.POST:
            user_input = request.POST['file'].file.read()
        elif 'paste' in request.POST:
            user_input = request.POST['paste']
        else:
            redirect(h.url_for('pipeline_index'))
        id = request.params.get('pipeline_id')
        pipeline_config = self.db.pipeline.get_from_id(id)['programs']
        pypit = Pypit(pipeline_config)
        uid = uuid1()
        file_name = 'sequence-%s.fas' % uid
        file_path = os.path.join('data', 'pipeline', file_name)
        open(file_path, 'w').write(user_input)
        tree = pypit.run(file_name='sequence-%s.fas' % uid, cwd=os.path.join('data', 'pipeline'))
        if not tree:
            h.failure_flash('Something wrong appened. Please, check your data')
            redirect(h.url('pipeline_index'))
        if pypit.last_output_ext == 'svg':
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
          'last_output_ext': pypit.last_output_ext,
        })

    
