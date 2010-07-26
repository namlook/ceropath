from ceropath.lib.uimodules import *
from pylons.controllers.util import abort
import os
import codecs

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
        for file_name in os.listdir(os.path.join(module_path, name)):
            if id in file_name.lower() or id.split()[0].lower() in file_name.lower():
                base_file_name, ext = os.path.splitext(file_name)
                if ext.lower() in ['.jpg', '.jpeg', '.png']:
                    files_list[file_name] = base_file_name
                    if '%s.txt' % base_file_name in os.listdir(os.path.join(module_path, name)):
                        legend_file = os.path.join(module_path, name, '%s.txt' % base_file_name)
                    else:
                        legend_file = None
                    if legend_file:
                        legends[file_name] = codecs.open(legend_file, encoding='utf-8', errors='ignore').read()
                if 'bibliography' in file_name.lower():
                    bibliography = codecs.open(os.path.join(module_path, name, file_name), encoding='utf-8', errors='ignore').read()
        if '%s.txt' % id.capitalize() in os.listdir(os.path.join(module_path, name)):
            legend_file = os.path.join(module_path, name, '%s.txt' % id.capitalize())
            legends[id] = codecs.open(legend_file, encoding='utf-8', errors='ignore').read()
        if not bibliography:
            if 'bibliography.txt' in os.listdir(os.path.join(module_path, name)):
                bibliography = codecs.open(os.path.join(module_path, name, 'bibliography.txt'), encoding='utf-8', errors='ignore').read()
        return render('/uimodules/module.mako', extra_vars={
            '_id': id,
            'files_list': files_list,
            'width': width,
            'legends': legends,
            'bibliography': bibliography,
            'data_path': os.path.join('/', 'data', 'dynamic', name),
        })
Module = Module()
 
class ModulesList(UIModule):
    def render(self, id, root): 
        modules_list = set([])
        for module in os.listdir(os.path.join('ceropath', 'public', 'data', 'dynamic')):
            for file_name in os.listdir(os.path.join('ceropath', 'public', 'data', 'dynamic', module)):
                if id in file_name.decode('utf-8').lower() or id.split()[0].lower() in file_name.decode('utf-8').lower():
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
        path = os.path.join('ceropath', 'public', 'data', 'static', 'chromatogram', gene.lower())
        web_path = os.path.join('/', 'data', 'static', 'chromatogram', gene.lower())
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
            
        
