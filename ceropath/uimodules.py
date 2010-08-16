from ceropath.lib.uimodules import *
from pylons.controllers.util import abort
import os
import codecs

class Measurements(UIModule):
    def render(self, id, publications_list, measures_infos, traits, full=False, species=None, age=None):
        return render('/uimodules/measurements.mako', extra_vars={
          '_id': id,
          'publications_list': publications_list,
          'measures_infos': measures_infos,
          'traits': traits,
          'species': species,
          'age': age,
          'full': full,
        })
Measurements = Measurements()


class SpeciesMenu(UIModule):
    def render(self, id):
        modules = os.listdir(os.path.join('ceropath', 'public', 'data'))
        return render('/uimodules/species_menu.mako', extra_vars={
          '_id': id,
          'modules': modules,
        })
SpeciesMenu = SpeciesMenu()

class IndividualMenu(UIModule):
    def render(self, id):
        modules = os.listdir(os.path.join('ceropath', 'public', 'data'))
        return render('/uimodules/individual_menu.mako', extra_vars={
          '_id': id,
          'modules': modules,
        })
IndividualMenu = IndividualMenu()

class ParasiteMenu(UIModule):
    def render(self, id):
        modules = os.listdir(os.path.join('ceropath', 'public', 'data'))
        return render('/uimodules/parasite_menu.mako', extra_vars={
          '_id': id,
          'modules': modules,
        })
ParasiteMenu = ParasiteMenu()

class Module(UIModule):
    def render(self, id, name,  width=1200):
        module_path = os.path.join('ceropath', 'public', 'data', 'dynamic')
        if name not in os.listdir(module_path):
            return "module not found"
        files_list = {}
        legends = {}
        bibliography = ""
        file_names = {'species':[], 'genus': []}
        list_file_names = []
        for file_name in os.listdir(os.path.join(module_path, name)):
            if id in file_name.lower() or '%s sp.' % id.split()[0].lower() in file_name.lower():
                list_file_names.append(os.path.splitext(file_name))
        for (base_file_name, ext) in list_file_names:
            file_name = "".join([base_file_name, ext])
            legend_file = None
            if ext.lower() in ['.jpg', '.jpeg', '.png']:
                files_list[file_name] = base_file_name
                #if '%s.txt' % base_file_name in os.listdir(os.path.join(module_path, name)):
                #    legend_file = os.path.join(module_path, name, '%s.txt' % base_file_name)
                #    legends[file_name] = codecs.open(legend_file, encoding='utf-8', errors='ignore').read()
            elif ext.lower() == '.txt' and legend_file is None:
                if id.lower() in base_file_name.lower() or '%s sp.' % id.split()[0].lower() in base_file_name.lower():
                    legend_file = os.path.join(module_path, name, file_name)
                    legends[id.lower()] = codecs.open(legend_file, encoding='utf-8', errors='ignore').read()
#            if 'bibliography' in file_name.lower():
#                bibliography = codecs.open(os.path.join(module_path, name, file_name), encoding='utf-8', errors='ignore').read()
        if '%s.txt' % id.capitalize() in os.listdir(os.path.join(module_path, name)):
            legend_file = os.path.join(module_path, name, '%s.txt' % id.capitalize())
            legends[id] = codecs.open(legend_file, encoding='utf-8', errors='ignore').read()
#        if not bibliography:
#            if 'bibliography.txt' in os.listdir(os.path.join(module_path, name)):
#                bibliography = codecs.open(os.path.join(module_path, name, 'bibliography.txt'), encoding='utf-8', errors='ignore').read()
        return render('/uimodules/module.mako', extra_vars={
            '_id': id,
            'files_list': files_list,
            'width': width,
            'legends': legends,
#            'bibliography': bibliography,
            'data_path': os.path.join('/', 'data', 'dynamic', name),
        })
Module = Module()
 
class ModulesList(UIModule):
    def render(self, id, root): 
        modules_list = set([])
        for module in os.listdir(os.path.join('ceropath', 'public', 'data', 'dynamic')):
            for file_name in os.listdir(os.path.join('ceropath', 'public', 'data', 'dynamic', module)):
                if id in file_name.decode('utf-8').lower() or '%s sp.' % id.split()[0].lower() in file_name.decode('utf-8').lower():
                    base_file_name, ext = os.path.splitext(file_name.lower())
                    if ext in ['.jpg', '.jpeg', '.png']:
                        modules_list.add(module)
                        break
        return render('/uimodules/modules_list.mako', extra_vars={
            '_id': id,
            'modules_list': modules_list,
            'root': root,
        })
ModulesList = ModulesList()

class ChromatogramList(UIModule):
    def render(self, individual_id, gene):
        chromatograms = []
        good_directory = None
        for directory in os.listdir(os.path.join('ceropath', 'public', 'data', 'static', 'chromatogram')):
            if gene.lower() in directory.lower():
                good_directory = directory
        if not good_directory:
            return ""
        path = os.path.join('ceropath', 'public', 'data', 'static', 'chromatogram', good_directory)
        web_path = os.path.join('/', 'data', 'static', 'chromatogram', good_directory)
        for file_name in os.listdir(path):
            try:
                if individual_id in file_name.lower():
                    chromatograms.append(file_name)
            except:
                print file_name, "has not a good encoding"
        return render('/uimodules/chromatogram_list.mako', extra_vars={
            'path':web_path,
            'chromatograms': chromatograms,
        })
ChromatogramList = ChromatogramList()
