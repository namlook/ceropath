<%inherit file="/root.mako" />


<!-- the tabs --> 
<ul class="tabs"> 
    <li><a href="#">General Informations</a></li> 
    <li><a href="#">Species measurements</a></li> 
</ul> 

<!-- tab "panes" --> 
<div class="panes"> 
    <!--- General Informations -->
    <div>
        <h1>${_id.capitalize()}</h1>
        <h4>(${author}, ${date})</h4>

        <fieldset><legend>Also known as</legend>
            <ul>
                % for language, name in common_names.iteritems():
                    % if name:
                        <li> ${name} (${language}) </li> 
                    % endif
                % endfor
            </ul>
        </fieldset>

        <fieldset><legend>Taxonomic ranks</legend>
        <table>
            <%ranks = ['kingdom', 'phylum', 'class', 'order', 'superfamily', 'family', 'subfamily', 'tribe', 'genus', 'subgenus']%>
            % for rank in ranks:
                <tr><td><b>${rank}</b></td><td>${taxonomic_rank[rank]}</td></tr>
            % endfor
        </table>
        </fieldset>
    </div> 
    <!--- Species measurements -->
    <div>
        <h2> Species measurements in literature</h2>

        <% publication_ids = publications_list.keys() %>
        <table>
            <tr><th></th>
            % for publication_id in publications_list:
                <th><a href="#">${publication_id}</a></th>
            % endfor
            </tr>
            % for trait, measure in measures_infos.iteritems():
                <tr><td>${trait}</td>
                    % for publication_id in publication_ids:
                        <% m = measure[publication_id] %>
                        <td>
                            <center>
                            <b>
                           ${m['mean'] or 0} +/- ${m['sd'] or 'NAN'} (${m['n']})
                           <br />
                           ${m['min'] or 0} - ${m['max'] or 0}
                            </b>
                            </center>
                        </td>
                    % endfor
                </tr>
            % endfor
        </table>

        <small>
            The mean plus or minus one standard deviation, number of <br />
            specimens in parentheses, and observed range are listed for each <br />
            measurement.
        </small>
    </div> 
</div> 


<!-- This JavaScript snippet activates those tabs --> 
<script> 
// perform JavaScript after the document is scriptable.
$(function() {
    // setup ul.tabs to work as tabs for each div directly under div.panes
    $("ul.tabs").tabs("div.panes > div");
});
</script> 
