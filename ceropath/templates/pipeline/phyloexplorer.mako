<%inherit file="/root.mako" />

<style>
.treline
{
    font-family: "Verdana", "Arial", "XHelvetica", "Helvetica", sans-serif;
    font-size: 22px;
    line-height: 10px;

}
</style>

<div class="span-30">
% if last_output_ext == 'svg':
    <iframe src ="${h.url(h.url_for('pipeline_servesvg', name=svg_path))}" width="100%" height="80%">
        <p>Your browser does not support iframes.</p>
    </iframe>
% else:
    <pre>${source}</pre>
% endif
</div>

<%doc>
<tt>
${display_tree(collection=None, list_taxa_collection=taxa_list, d_stats=None, tree=tree, source=source, root=source)}
</tt>
</%doc>


<%def name="display_tree( collection, list_taxa_collection, d_stats, source, tree, root = '',  mydepth = 0, lastnode = 'R5241_Cann', blockname = '', show_nb_trees = True, progress=True )">
        ## Create root node display
        % if root == source:
            <span class="treeline">|</span><br />
        % endif
        ## Create tree display
        % if root in tree.nodes():
            % for node in tree.successors( root ):
                <%
                    n = tree.predecessors( node ) + tree.successors(node)
                %>
                ## Create div for interparents (parents beetween nodes)
                % if len(n) == 2:
                    <%
                        nextdepth=mydepth
                    %>
                    % if node in list_taxa_collection:
                        <%
                            depth = 0
                        %>
                        % while depth != mydepth :
                            <span class="treeline">|</span>
                            <%
                                depth += 1
                            %>
                        % endwhile
                        ${display_species(node)}
                        <%
                            nextdepth +=1
                        %>
                    % endif
                    ${display_tree( collection, list_taxa_collection, d_stats, source, tree,  node, nextdepth, 
                      lastnode = node, blockname = blockname+"a", show_nb_trees = show_nb_trees, progress=progress)}
                    <%
                        continue
                    %>
                % endif
                <%
                ## Create arborescence display
                    depth = 0
                %>
                % while depth != mydepth :
                    <span class="treeline">|</span>
                    <%
                        depth += 1
                    %>
                % endwhile
                <%
                    subnodes = tree.successors( node )
                %>
                 ## it's a genre
                % if subnodes:
                    <span genre="${node}">
                    % if node in list_taxa_collection:
                        ${display_species(node)}
                    % else:
                        ${display_genre(node)}
                    % endif
                    ${display_tree( collection, list_taxa_collection, d_stats,source, tree,  node, depth + 1,
                      lastnode = node, blockname = blockname+"a", show_nb_trees = show_nb_trees, progress=progress)}
                    </span>
                ## it's a species (ie taxon)
                % else:
                    ${display_species(node)}
                % endif
            % endfor
        % endif
</%def>

<%def name='display_species(node)'>
    +-${node}<br />
</%def>

<%def name='display_genre(node)'>
    +-\<br />
</%def>
