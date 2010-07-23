import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render
from routes import url_for
from ceropath.lib import helpers as h
from config import json_allowed

from pprint import pprint, pformat
import os
from pylons import config

log = logging.getLogger(__name__)

class DatabaseController(BaseController):

    def index(self):
        return render('database/index.mako')

    def load(self):
        pprint( request.POST)
        not_allowed_files = []
        for name, field_storage in request.POST.iteritems():
            if hasattr(field_storage, 'filename'):
                base, ext = os.path.splitext(field_storage.filename)
                if base not in json_allowed:
                    not_allowed_files.append(field_storage.filename)
                    continue
                open(os.path.join('data', 'usrjson', field_storage.filename), 'w+b').write(field_storage.file.read())
                print "Importing:", base
                file_path = os.path.join('data', 'usrjson', field_storage.filename)
                os.system("mongoimport --drop -d %s -c %s --file %s ; rm %s" % (config['db_name'], base, file_path, file_path))
        if not_allowed_files:
            h.failure_flash("Following files are not allowed : %s" % ', '.join(not_allowed_files))
        else:
            h.success_flash('Importation succeed')
        redirect(url_for('database_index'))

    def status(self):
        db_stats = pformat(self.db.command('dbstats'))
        server_status = pformat(self.db.command('serverStatus'))
        return render('database/status.mako', extra_vars={
            'db_stats': db_stats,
            'server_status': server_status,
        })
