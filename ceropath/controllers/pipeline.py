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
            'title': 'DNA Sequence Identification',
        })

    def new(self):
        # TODO use jquery tools forms validation
        return render('pipeline/new.mako', extra_vars={
            'title': 'New pipeline',
        })

    def create(self):
        pipeline = self.db.pipeline.Pipeline()
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
          'title': "Pipeline list",
        })
    
    def edit(self, id):
        pipeline = self.db.pipeline.get_from_id(id)
        return render('pipeline/config.mako', extra_vars = {
          'programs':pipeline['programs'],
          'title': 'Edit pipeline %s' % id,
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

    def result(self):
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
        result = pypit.run(file_name='sequence-%s.fas' % uid, cwd=os.path.join('data', 'pipeline'))
        errors = ""
        output_format = pypit.last_output_ext
        if not result:
            h.failure_flash('Something wrong appened. Please, check your data')
            errors = pypit.errors.read()
        elif output_format == 'nwk':
            from Bio import Nexus, Phylo
            t = Nexus.Trees.Tree(open(os.path.join('data', 'pipeline', '%s.afa.phy.mat.nwk' % file_name)).read())
            t.root_with_outgroup('R5241_Cann')
            from StringIO import StringIO
            n = Phylo.read(StringIO(t.to_string().split('=')[1].strip()), 'newick')
            f = StringIO()
            individuals = []
            users_individuals = []
            for clade in n.find_clades():
                if clade.name:
                    clade_name = clade.name.split('_')[0].lower()
                    individual = self.db.individual.get_from_id(clade_name)
                    if individual:
                        individuals.append(individual)
                    else:
                        users_individuals.append(clade_name)
                    clade.name = clade_name.upper()
            Phylo.draw_ascii(n, file=f, column_width=110)
            f.seek(0)
            result = f.read().replace(' ', '&nbsp;').replace('\n', '<br />').replace('...', ' ')
            for individual_id in users_individuals:
                result = result.replace(individual_id.upper(),'<span style="color:red;">%s</span>' % individual_id.upper())
            for individual in individuals:
                try:
                    species_id = individual['organism_classification']['$id']
                except: # XXX Why the hell ?
                    species_id = individual['organism_classification'].id
                individual_id = individual['_id']
                if individual['voucher_barcoding']:
                    result = result.replace(individual_id.upper(),
                      '<a class="individual" href="/individual/%s">%s</a>' % (
                        individual_id, individual_id.upper()) + ' <a class="species" href="/species/%s">(<i>%s</i>)</a>' % (
                          species_id.replace(' ', '%20'), species_id.capitalize()))
                else:
                    result = result.replace(individual_id.upper(),
                      individual_id.upper() + ' <a class="species" href="/species/%s">(<i>%s</i>)</a>' % (
                        species_id.replace(' ', '%20'), species_id.capitalize()))
        elif output_format == 'svg':
            svg_path = os.path.join('ceropath', 'public', 'usrdata', file_name+".afa.phy.mat.nwk.svg")
            users_individuals = [line.strip()[1:].strip().lower() for line in open(file_path).readlines() if line.strip().startswith('>')]
            open(svg_path, 'w').write(h.clickify_svg(result, self.db, users_individuals))
            result = file_name+".afa.phy.mat.nwk.svg"
        return render('pipeline/result.mako', extra_vars = {
          'errors': errors,
          'result':result,
          'output_format': output_format,
          'title': 'DNA Sequence Identification Results',
        })

    def infos(self, name):
        if name in os.listdir(os.path.join('ceropath', 'public', 'data', 'pipeline')):
            content = open(os.path.join('ceropath', 'public', 'data', 'pipeline', name)).read()
        else:
            content = "Not informations about this pipeline was found... sorry."
        return render('pipeline/infos.mako', extra_vars = {
            'content': content,
            'title': '%s informations' % name,
        })

    def servesvg(self, name):
        response.headers['Content-type'] = "image/svg+xml"
        return open(os.path.join('ceropath', 'public', 'usrdata', name)).read()
