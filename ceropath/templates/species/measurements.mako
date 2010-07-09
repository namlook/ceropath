<%inherit file="/species/show.mako" />

<div class="span-30 alt">
    <h2> Species measurements in literature</h2>
</div>

<div class="span-30">
    <table class="measurements">
        <tr><th></th>
        % for pub, origin in publications_list:
            % if pub is not None:
                <th style="width:250px;">
                    Measurements in <a href="${h.url(h.url_for('publication_show', id=pub['_id']))}" title="${pub['reference']}">
                    ${h.author_date_from_citation(pub['reference'])}
                    </a>
                    for ${_id.capitalize()} in ${origin} <small>(a)</small>
                 </th>
            % else:
                <th style="width:250px;">
                    Ceropath Measurements for ${_id.capitalize()} <small>(a)</small>
                </th>
            % endif
        % endfor
        </tr>
        <%
            first_measures = ['Head & Body (mm)', 'Tail (mm)', 'Foot (mm)', 'Head (mm)', 'Ear (mm)', 'Weight (g)']
            last_measures = sorted(i.strip() for i in measures_infos if i not in first_measures)
        %>
        % for trait in first_measures + last_measures:
            <% measure = measures_infos[trait] %>
            <tr><th>${trait}</th>
                % for key in publications_list:
                    <%
                        m = measure.get(key)
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
</div>
