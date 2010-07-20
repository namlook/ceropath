import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from ceropath.lib.base import BaseController, render
from ceropath.lib import helpers as h
import config

log = logging.getLogger(__name__)

class LoginController(BaseController):

    def show(self):
        """
        Show login form. Submits to /login/submit
        """
        return render('login/show.mako')

    def submit(self):
        """
        Verify username and password
        """
        # Both fields filled?
        username = str(request.params.get('username'))
        password = str(request.params.get('password'))

        # There is only one user so we don't need to get it from database
        # the usename and password are describes in config.py
        if username != config.username:
           h.failure_flash('wrong username or password')
           return render('login/show.mako')

        # We don't care much about security here so no need to salt password
        if password != config.password:
           h.failure_flash('wrong username or password')
           return render('login/show.mako')

        # Mark user as logged in
        session['user'] = username
        session.save()

        # Send user back to the page he originally wanted to get to
        if session.get('path_before_login'):
           redirect(session['path_before_login'])
        else: # if previous target is unknown just send the user to a welcome page
           return redirect(h.url_for('species_index'))

    def logout(self):
        """
        Logout the user and display a confirmation message
        """
        if 'user' in session:
           del session['user']
           session.save()
           h.success_flash('you are logged out')
        return redirect(h.url_for('species_index'))
        
