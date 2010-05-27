from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1274966969.3115971
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
        __M_writer(u'<html>\n<head>\n</head>\n<body>\n    <div class="header"><a href="index.php"><img src="/img/header.jpg" width="1200" height="200" alt="Home"/></a></div>\n    ')
        # SOURCE LINE 6
        __M_writer(escape(next.body()))
        __M_writer(u'\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


