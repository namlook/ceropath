<%inherit file="/species/show.mako" />

<h2> Species measurements in literature</h2>

<% publication_ids = publications_list.keys() %>
<table>
    <tr><th></th>
    % for publication_id in publications_list:
        <th><a href="#">${publication_id}</a></th>
    % endfor
    </tr>
    % for trait, measure in measures_infos.iteritems():
        <tr><th>${trait}</th>
            % for publication_id in publication_ids:
                <%
                m = measure[publication_id]
                m['n'] = int(m['n'].split(',')[0]) if m['n'] else 0
                %>
                <td>
                    <center>
                    <b>
                    % if m['n']:
                       ${m['mean'] or 0} +/- ${m['sd'] or 'NAN'} (${m['n']})
                       <br />
                       ${m['min'] or 0} - ${m['max'] or 0}
                    % else:
                        ø
                    % endif
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

