<%inherit file="/species/show.mako" />

<h2> Species measurements in literature</h2>

<%doc>
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
</%doc>
     <%
         theaders = [(_id, 'species')]
         theaders.extend((i, 'pubref') for i in publications_list.keys())
     %>
    <table class="measurements">
        <tr><th></th>
        % for header in theaders:
            % if header[1] == 'pubref':
                <th style="width:250px;">
                    Measurements in <a href="" title="${publications_list[header[0]]['reference']}">
                    ${h.author_date_from_citation(publications_list[header[0]]['reference'])}
                    </a>
                    for ${_id.capitalize()} <small>(a)</small>
                 </th>
            % elif header[1] == 'species':
                <th style="width:250px;">
                    Ceropath Measurements for ${header[0].capitalize()} <small>(a)</small>
                </th>
            % else:
                <th>Measurements for ${header[0].upper()} ${age}</th>
            % endif
        % endfor
        </tr>
        <%
            # XXX skull -> head
            first_measures = ['Head & Body (mm)', 'Tail (mm)', 'Foot (mm)', 'Skull  (mm)', 'Ear (mm)', 'Weight (g)']
            last_measures = sorted(i.strip() for i in measures_infos if i not in first_measures)
        %>
        % for trait in first_measures + last_measures:
            <% measure = measures_infos[trait] %>
            <tr><th>${trait}</th>
                % for publication_id in theaders:
                    <%
                        publication_id = publication_id[0]
                        m = measure.get(publication_id)
                        if isinstance(m, dict):
                            if isinstance(m['n'], basestring):
                                m['n'] = int(float(m['n'].replace(',', '.'))) if m['n'] else 0
                    %>
                    <td>
                        <center>
                        % if isinstance(m, dict):
                            % if m['n']:
                               ${m['mean'] or 0} +/- ${m['sd'] or 'NAN'} (${m['n']})
                               <br />
                               ${m['min'] or 0} - ${m['max'] or 0}
                            % else:
                                ø
                            % endif
                        % else:
                            ${m or u'ø'}
                        % endif
                        </center>
                    </td>
                % endfor
            </tr>
        % endfor
    </table>
    <p>
    (a) The mean plus or minus one standard deviation, number of specimens in parentheses, and observed range are listed for each measurement.
    </p>

