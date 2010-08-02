import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render

log = logging.getLogger(__name__)

class InstituteController(BaseController):

    def show(self, id):
        institute = self.db.institute.get_from_id(id)
        if not institute:
            abort(404)
        return render('institute/show.mako', extra_vars={
            'institute': institute,
            'title': "%s institute" % id,
        })
