from ceropath.lib.uimodules import *
import os

class SpeciesMenu(UIModule):
    def render(self, id):
        modules = os.listdir(os.path.join('ceropath', 'public', 'data'))
        return render('/uimodules/species_menu.mako', extra_vars={
          '_id': id,
          'modules': modules,
        })
SpeciesMenu = SpeciesMenu()

