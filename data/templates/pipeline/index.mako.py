from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1274966969.3074329
_template_filename='/home/namlook/Documents/projets/ceropath/ceropath/templates/pipeline/index.mako'
_template_uri='pipeline/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/root.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n    <fieldset>\n        <legend>Choose the file containing a sequence (fasta format)...</legend>\n        <form action="')
        # SOURCE LINE 5
        __M_writer(escape(h.url(h.url_for('pipeline_phyloexplorer'))))
        __M_writer(u'" method="post" enctype="multipart/form-data">\n            <br/>\n            <b>Filename:</b> <input type="file" name="file" class="button" /><br />\n            <input type="reset" class="button" value="Reset" />\n            <input type="submit" />\n')
        # SOURCE LINE 11
        __M_writer(u'        </form>\n    </fieldset>\n    <br />\n    <fieldset>\n        <legend>... OR paste your sequence...</legend>\n        <form action="')
        # SOURCE LINE 16
        __M_writer(escape(h.url(h.url_for('pipeline_phyloexplorer'))))
        __M_writer(u'" method="post" enctype="multipart/form-data">\n            <textarea rows="10" cols="80" name="paste" value=""></textarea><br />\n\n')
        # SOURCE LINE 21
        __M_writer(u'            <input type="button" class="button" value="Reset" id="badreset"/>\n            <input type="submit" />\n')
        # SOURCE LINE 24
        __M_writer(u'        </form>\n    </fieldset>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


