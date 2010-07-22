from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1279625292.9102249
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
        h = context.get('h', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n')
        # SOURCE LINE 4
        __M_writer(u'    <link rel="stylesheet" type="text/css" href="/css/tabs-no-images.css" /> \n')
        # SOURCE LINE 6
        __M_writer(u'    <link rel="stylesheet" href="/css/blueprint.1200.compressed.css" type="text/css" media="screen, projection">\n')
        # SOURCE LINE 9
        __M_writer(u'    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>\n    <script src="http://cdn.jquerytools.org/1.2.3/jquery.tools.min.js"></script>\n')
        # SOURCE LINE 12
        __M_writer(u'    <link rel="stylesheet" href="/css/demo_table.css" />\n    <style> \n        /* tab pane styling */\n        .panes div {\n            display:none;       \n            padding:15px 10px;\n            border-top:0;\n            height:100px;\n            font-size:14px;\n            background-color:#fff;\n        }\n        table th{\n            background-color: #FD9834;\n        }\n    </style> \n</head>\n<body>\n    <div class="container">\n        <div class="span-30">\n            <a href="')
        # SOURCE LINE 31
        __M_writer(escape(h.url(h.url_for('species_index'))))
        __M_writer(u'"><img src="/img/header.jpg" width="1200" alt="Home" /></a>\n        </div>\n        <div class="flash-message">\n            ')
        # SOURCE LINE 34

        message = h.failure_flash.pop_messages()
        flash_color = "red"
        if not message:
            message = h.success_flash.pop_messages()
            flash_color = "green"
                    
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['flash_color','message'] if __M_key in __M_locals_builtin()]))
        # SOURCE LINE 40
        __M_writer(u'\n')
        # SOURCE LINE 41
        if message:
            # SOURCE LINE 42
            __M_writer(u'                <div style="text-decoration:bold;color:')
            __M_writer(escape(flash_color))
            __M_writer(u'">')
            __M_writer(escape(message[0]))
            __M_writer(u'</div>\n')
        # SOURCE LINE 44
        __M_writer(u'        </div>\n        ')
        # SOURCE LINE 45
        __M_writer(escape(next.body()))
        __M_writer(u'\n    </div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


