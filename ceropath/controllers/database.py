import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render
from routes import url_for
from ceropath.lib import helpers as h
from ceropath.lib.precalculatemeasurments import pre_calculate_measurements
from ceropath.lib.unzip import unzip
from config import json_allowed

from pprint import pprint, pformat
import os
from pylons import config

log = logging.getLogger(__name__)

class DatabaseController(BaseController):

    admin_requires_auth_actions = ['index', 'load', 'status']

    def index(self):
        """
        Show the page where the admin can update the database. The file must be
        a zip file which contains json files in its root.
        """
        return render('database/index.mako', extra_vars={
            'title': 'Update database',
        })

    def load(self):
        """
        after the index action:

        load the zip file, extract it and import all json files to the database
        """
        not_allowed_files = []
        if not 'jsonzip' in request.POST:
            h.failure_flash("You must provide a jsons zip archive")
            redirect(url_for('database_index'))
        open(os.path.join('data', 'json.zip'), 'w').write(request.POST['jsonzip'].file.read())
        zip = unzip()
        zip.extract(os.path.join('data', 'json.zip'), os.path.join('data', 'json'))
        for filename in os.listdir(os.path.join('data', 'json')):
            base, ext = os.path.splitext(filename)
            if base not in json_allowed:
                not_allowed_files.append(filename)
                continue
            print "Importing:", base
            file_path = os.path.join('data', 'json', filename)
            os.system("mongoimport --drop -d %s -c %s --file %s" % (config['db_name'], base, file_path))
        pre_calculate_measurements(self.db)
        if not_allowed_files:
            h.failure_flash("Following files are not allowed : %s" % ', '.join(not_allowed_files))
        else:
            h.success_flash('Importation succeed')
        redirect(url_for('database_index'))

    def status(self):
        """
        return database information status
        """
        db_stats = pformat(self.db.command('dbstats'))
        server_status = pformat(self.db.command('serverStatus'))
        return render('database/status.mako', extra_vars={
            'db_stats': db_stats,
            'server_status': server_status,
            'title': 'database status',
        })
