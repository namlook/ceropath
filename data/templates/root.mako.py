from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1276865468.847014
_template_filename='/home/namlook/Documents/projets/ceropath/ceropath/templates/root.mako'
_template_uri='/root.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n    <link rel="stylesheet" type="text/css" href="/css/tabs.css" /> \n    <script src="/js/jquery.tools.min.js"></script>\n    <style> \n        /* tab pane styling */\n        .panes div {\n            display:none;       \n            padding:15px 10px;\n            border-top:0;\n            height:100px;\n            font-size:14px;\n            background-color:#fff;\n        }\n    </style> \n</head>\n<body>\n    <div class="header"><a href="index.php"><img src="/img/header.jpg" width="1200" height="200" alt="Home"/></a></div>\n    ')
        # SOURCE LINE 19
        __M_writer(escape(next.body()))
        __M_writer(u'\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


