from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1274961735.545485
_template_filename='/home/namlook/Documents/projets/ceropath/ceropath/templates/phyloexplorer.mako'
_template_uri='phyloexplorer.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['display_tree', 'display_species', 'display_genre']


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
        __M_writer(u'<style>\n.treline\n{\n    font-family: "Verdana", "Arial", "XHelvetica", "Helvetica", sans-serif;\n    font-size: 22px;\n    line-height: 10px;\n\n}\n</style>\n\n<big>\n<tt>\n')
        # SOURCE LINE 13
        __M_writer(escape(display_tree(collection=None, list_taxa_collection=taxa_list, d_stats=None, tree=tree, source=source, root=source)))
        __M_writer(u'\n</tt>\n</big>\n\n')
        # SOURCE LINE 93
        __M_writer(u'\n\n')
        # SOURCE LINE 97
        __M_writer(u'\n\n')
        # SOURCE LINE 102
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
        # SOURCE LINE 17
        __M_writer(u'\n')
        # SOURCE LINE 19
        if root == source:
            # SOURCE LINE 26
            __M_writer(u'            <span class="treeline">|</span><br />\n            ')
            # SOURCE LINE 27

            #    root = Taxonomy.objects.get( name = 'root' )
            

            # SOURCE LINE 29
            __M_writer(u'\n')
        # SOURCE LINE 32
        if root in tree.nodes():
            # SOURCE LINE 33
            for node in tree.successors( root ):
                # SOURCE LINE 34
                __M_writer(u'                ')

                n = tree.predecessors( node ) + tree.successors(node)
                                
                
                # SOURCE LINE 36
                __M_writer(u'\n')
                # SOURCE LINE 38
                if len(n) == 2:
                    # SOURCE LINE 39
                    __M_writer(u'                    ')

                    nextdepth=mydepth
                                        
                    
                    # SOURCE LINE 41
                    __M_writer(u'\n')
                    # SOURCE LINE 42
                    if node in list_taxa_collection:
                        # SOURCE LINE 43
                        __M_writer(u'                        ')

                        depth = 0
                                                
                        
                        # SOURCE LINE 45
                        __M_writer(u'\n')
                        # SOURCE LINE 46
                        while depth != mydepth :
                            # SOURCE LINE 47
                            __M_writer(u'                            <span class="treeline">|</span>\n                            ')
                            # SOURCE LINE 48

                            depth += 1
                                                        
                            
                            # SOURCE LINE 50
                            __M_writer(u'\n')
                        # SOURCE LINE 52
                        __M_writer(u'                        ')
                        __M_writer(escape(display_species(node)))
                        __M_writer(u'\n                        ')
                        # SOURCE LINE 53

                        nextdepth +=1
                                                
                        
                        # SOURCE LINE 55
                        __M_writer(u'\n')
                    # SOURCE LINE 57
                    __M_writer(u'                    ')
                    __M_writer(escape(display_tree( collection, list_taxa_collection, d_stats, source, tree,  node, nextdepth, 
                      lastnode = node, blockname = blockname+"a", show_nb_trees = show_nb_trees, progress=progress)))
                    # SOURCE LINE 58
                    __M_writer(u'\n                    ')
                    # SOURCE LINE 59

                    continue
                                        
                    
                    # SOURCE LINE 61
                    __M_writer(u'\n')
                # SOURCE LINE 63
                __M_writer(u'                ')

                ## Create arborescence display
                depth = 0
                                
                
                # SOURCE LINE 66
                __M_writer(u'\n')
                # SOURCE LINE 67
                while depth != mydepth :
                    # SOURCE LINE 68
                    __M_writer(u'                    <span class="treeline">|</span>\n                    ')
                    # SOURCE LINE 69

                    depth += 1
                                        
                    
                    # SOURCE LINE 71
                    __M_writer(u'\n')
                # SOURCE LINE 73
                __M_writer(u'                ')

                subnodes = tree.successors( node )
                                
                
                # SOURCE LINE 75
                __M_writer(u'\n')
                # SOURCE LINE 77
                if subnodes:
                    # SOURCE LINE 78
                    __M_writer(u'                    <span genre="')
                    __M_writer(escape(node))
                    __M_writer(u'">\n')
                    # SOURCE LINE 79
                    if node in list_taxa_collection:
                        # SOURCE LINE 80
                        __M_writer(u'                        ')
                        __M_writer(escape(display_species(node)))
                        __M_writer(u'\n')
                        # SOURCE LINE 81
                    else:
                        # SOURCE LINE 82
                        __M_writer(u'                        ')
                        __M_writer(escape(display_genre(node)))
                        __M_writer(u'\n')
                    # SOURCE LINE 84
                    __M_writer(u'                    ')
                    __M_writer(escape(display_tree( collection, list_taxa_collection, d_stats,source, tree,  node, depth + 1,
                      lastnode = node, blockname = blockname+"a", show_nb_trees = show_nb_trees, progress=progress)))
                    # SOURCE LINE 85
                    __M_writer(u'\n                    </span>\n')
                    # SOURCE LINE 88
                else:
                    # SOURCE LINE 89
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
        # SOURCE LINE 95
        __M_writer(u'\n    +-')
        # SOURCE LINE 96
        __M_writer(escape(node))
        __M_writer(u'<br />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_display_genre(context,node):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 99
        __M_writer(u'\n    +-\\<br />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


