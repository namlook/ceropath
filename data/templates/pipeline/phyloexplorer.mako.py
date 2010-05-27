from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1274967064.212374
_template_filename='/home/namlook/Documents/projets/ceropath/ceropath/templates/pipeline/phyloexplorer.mako'
_template_uri='pipeline/phyloexplorer.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['display_tree', 'display_species', 'display_genre']


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
        def display_tree(collection,list_taxa_collection,d_stats,source,tree,root='',mydepth=0,lastnode='root',blockname='',show_nb_trees=True,progress=True):
            return render_display_tree(context.locals_(__M_locals),collection,list_taxa_collection,d_stats,source,tree,root,mydepth,lastnode,blockname,show_nb_trees,progress)
        tree = context.get('tree', UNDEFINED)
        taxa_list = context.get('taxa_list', UNDEFINED)
        source = context.get('source', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<style>\n.treline\n{\n    font-family: "Verdana", "Arial", "XHelvetica", "Helvetica", sans-serif;\n    font-size: 22px;\n    line-height: 10px;\n\n}\n</style>\n\n<big>\n<tt>\n')
        # SOURCE LINE 15
        __M_writer(escape(display_tree(collection=None, list_taxa_collection=taxa_list, d_stats=None, tree=tree, source=source, root=source)))
        __M_writer(u'\n</tt>\n</big>\n\n')
        # SOURCE LINE 95
        __M_writer(u'\n\n')
        # SOURCE LINE 99
        __M_writer(u'\n\n')
        # SOURCE LINE 104
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_display_tree(context,collection,list_taxa_collection,d_stats,source,tree,root='',mydepth=0,lastnode='root',blockname='',show_nb_trees=True,progress=True):
    context.caller_stack._push_frame()
    try:
        def display_tree(collection,list_taxa_collection,d_stats,source,tree,root='',mydepth=0,lastnode='root',blockname='',show_nb_trees=True,progress=True):
            return render_display_tree(context,collection,list_taxa_collection,d_stats,source,tree,root,mydepth,lastnode,blockname,show_nb_trees,progress)
        def display_species(node):
            return render_display_species(context,node)
        len = context.get('len', UNDEFINED)
        def display_genre(node):
            return render_display_genre(context,node)
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\n')
        # SOURCE LINE 21
        if root == source:
            # SOURCE LINE 28
            __M_writer(u'            <span class="treeline">|</span><br />\n            ')
            # SOURCE LINE 29

            #    root = Taxonomy.objects.get( name = 'root' )
            

            # SOURCE LINE 31
            __M_writer(u'\n')
        # SOURCE LINE 34
        if root in tree.nodes():
            # SOURCE LINE 35
            for node in tree.successors( root ):
                # SOURCE LINE 36
                __M_writer(u'                ')

                n = tree.predecessors( node ) + tree.successors(node)
                                
                
                # SOURCE LINE 38
                __M_writer(u'\n')
                # SOURCE LINE 40
                if len(n) == 2:
                    # SOURCE LINE 41
                    __M_writer(u'                    ')

                    nextdepth=mydepth
                                        
                    
                    # SOURCE LINE 43
                    __M_writer(u'\n')
                    # SOURCE LINE 44
                    if node in list_taxa_collection:
                        # SOURCE LINE 45
                        __M_writer(u'                        ')

                        depth = 0
                                                
                        
                        # SOURCE LINE 47
                        __M_writer(u'\n')
                        # SOURCE LINE 48
                        while depth != mydepth :
                            # SOURCE LINE 49
                            __M_writer(u'                            <span class="treeline">|</span>\n                            ')
                            # SOURCE LINE 50

                            depth += 1
                                                        
                            
                            # SOURCE LINE 52
                            __M_writer(u'\n')
                        # SOURCE LINE 54
                        __M_writer(u'                        ')
                        __M_writer(escape(display_species(node)))
                        __M_writer(u'\n                        ')
                        # SOURCE LINE 55

                        nextdepth +=1
                                                
                        
                        # SOURCE LINE 57
                        __M_writer(u'\n')
                    # SOURCE LINE 59
                    __M_writer(u'                    ')
                    __M_writer(escape(display_tree( collection, list_taxa_collection, d_stats, source, tree,  node, nextdepth, 
                      lastnode = node, blockname = blockname+"a", show_nb_trees = show_nb_trees, progress=progress)))
                    # SOURCE LINE 60
                    __M_writer(u'\n                    ')
                    # SOURCE LINE 61

                    continue
                                        
                    
                    # SOURCE LINE 63
                    __M_writer(u'\n')
                # SOURCE LINE 65
                __M_writer(u'                ')

                ## Create arborescence display
                depth = 0
                                
                
                # SOURCE LINE 68
                __M_writer(u'\n')
                # SOURCE LINE 69
                while depth != mydepth :
                    # SOURCE LINE 70
                    __M_writer(u'                    <span class="treeline">|</span>\n                    ')
                    # SOURCE LINE 71

                    depth += 1
                                        
                    
                    # SOURCE LINE 73
                    __M_writer(u'\n')
                # SOURCE LINE 75
                __M_writer(u'                ')

                subnodes = tree.successors( node )
                                
                
                # SOURCE LINE 77
                __M_writer(u'\n')
                # SOURCE LINE 79
                if subnodes:
                    # SOURCE LINE 80
                    __M_writer(u'                    <span genre="')
                    __M_writer(escape(node))
                    __M_writer(u'">\n')
                    # SOURCE LINE 81
                    if node in list_taxa_collection:
                        # SOURCE LINE 82
                        __M_writer(u'                        ')
                        __M_writer(escape(display_species(node)))
                        __M_writer(u'\n')
                        # SOURCE LINE 83
                    else:
                        # SOURCE LINE 84
                        __M_writer(u'                        ')
                        __M_writer(escape(display_genre(node)))
                        __M_writer(u'\n')
                    # SOURCE LINE 86
                    __M_writer(u'                    ')
                    __M_writer(escape(display_tree( collection, list_taxa_collection, d_stats,source, tree,  node, depth + 1,
                      lastnode = node, blockname = blockname+"a", show_nb_trees = show_nb_trees, progress=progress)))
                    # SOURCE LINE 87
                    __M_writer(u'\n                    </span>\n')
                    # SOURCE LINE 90
                else:
                    # SOURCE LINE 91
                    __M_writer(u'                    ')
                    __M_writer(escape(display_species(node)))
                    __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_display_species(context,node):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 97
        __M_writer(u'\n    +-')
        # SOURCE LINE 98
        __M_writer(escape(node))
        __M_writer(u'<br />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_display_genre(context,node):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 101
        __M_writer(u'\n    +-\\<br />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


