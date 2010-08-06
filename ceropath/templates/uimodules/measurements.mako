    % if not full and len(publications_list) > 4:
        <div style="text-align:right;color:red;">
        ${len(publications_list) - 4} column left. <a href="${h.url(h.url_for('individual_measurements', id=_id))}">See full table</a>
        </div>
    % endif
    <table class="measurements">
        <tr><th></th>
        <%
        if species:
            sorted_publications_list = publications_list
        else:
            sorted_publications_list = sorted(publications_list)
        if not full:
            sorted_publications_list = sorted_publications_list[:4]
        %>
        % for pub, origin, species_article_name in sorted_publications_list:
            % if pub is not None:
                <th>
                    Measurements in <a href="${h.url(h.url_for('publication_show', id=pub['_id']))}" title="${pub['reference']}">
                    ${h.author_date_from_citation(pub['reference'])}
                    </a>
                    for ${species_article_name.capitalize()} in ${origin} <small>(a)</small>
                 </th>
            % elif origin == _id or species is None:
                <th> Ceropath Measurements for ${_id.capitalize()} <small>(a)</small> </th>
            % else:
                <th> Ceropath Measurements for ${species.capitalize()} <small>(a)</small></th>
            % endif
        % endfor
        </tr>
        <%
            traits_list = sorted(traits)
            traits_list.insert(2, '0')
            traits['0'] = {u'remark': None, u'_id': u'0', u'measurement_accuracy': 0, u'name': "Tail / Head & Body (%)"}
        %>
        % for trait_id in traits_list:
            <%
                trait = traits[trait_id]
                measure = measures_infos.get(trait['name'])
                if not measure:
                    continue
            %>
            <tr><th>${trait['name']}</th>
                % for key in sorted_publications_list:
                    <%
                        m = measure.get(key)
                        if isinstance(m, dict):
                            if isinstance(m['n'], basestring):
                                if m['n']:
                                    m['n'] = int(float(m['n'].replace(',', '.')))
                                else:
                                    m['n'] = 0
                    %>
                    <td>
                        <center>
                        % if m and isinstance(m, dict):
                            % if m.get('n'):
                                % if m['mean']:
                                    % if trait['measurement_accuracy']:
                                        ${round(float(m['mean']), trait['measurement_accuracy'])}
                                    % else:
                                        ${int(round(float(m['mean']), trait['measurement_accuracy']))}
                                    % endif
                                % else:
                                    ø
                                % endif
                                +/-
                                % if m.get('sd'):
                                    ${round(float(m['sd']), 2)}
                                % else:
                                    ø
                                % endif
                                (${int(m['n'])})
                               <br />
                                % if m.get('min'):
                                    % if trait['measurement_accuracy']:
                                        ${round(float(m['min']), trait['measurement_accuracy'])}
                                    % else:
                                        ${int(round(float(m['min']), trait['measurement_accuracy']))}
                                    % endif
                                % else:
                                    ø
                                % endif
                                -
                                % if m.get('max'):
                                    % if trait['measurement_accuracy']:
                                        ${round(float(m['max']), trait['measurement_accuracy'])}
                                    % else:
                                        ${int(round(float(m['max']), trait['measurement_accuracy']))}
                                    % endif
                                % else:
                                    ø
                                % endif
                            % else:
                                ø
                            % endif
                        % elif m:
                            ${m}
                        % else:
                            ø
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

