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
        % for trait_id in sorted(traits):
            <%
                trait = traits[trait_id]
                measure = measures_infos.get(trait['name'])
                if not measure:
                    continue
            %>
            <tr><th>${trait['name']}</th>
                % for key in publications_list:
                    <%
                        m = measure.get(key)
                        if isinstance(m, dict):
                            if isinstance(m['n'], basestring):
                                m['n'] = int(float(m['n'].replace(',', '.'))) if m['n'] else 0
                    %>
                    <td>
                        <center>
                        % if m:
                            % if m['n']:
                                % if m['mean']:
                                    % if trait['measurement_accuracy']:
                                        ${round(float(m['mean']), trait['measurement_accuracy'])}
                                    % else:
                                        ${int(m['mean'])}
                                    % endif
                                % else:
                                    0
                                % endif
                                +/-
                                % if m['sd']:
                                    % if trait['measurement_accuracy']:
                                        ${round(float(m['sd']), trait['measurement_accuracy'])}
                                    % else:
                                        ${int(m['sd'])}
                                    % endif
                                % else:
                                    NAN
                                % endif
                                (${int(m['n'])})
                               <br />
                                % if m['min']:
                                    % if trait['measurement_accuracy']:
                                        ${round(float(m['min']), trait['measurement_accuracy'])}
                                    % else:
                                        ${int(m['min'])}
                                    % endif
                                % else:
                                    0
                                % endif
                                -
                                % if m['max']:
                                    % if trait['measurement_accuracy']:
                                        ${round(float(m['max']), trait['measurement_accuracy'])}
                                    % else:
                                        ${int(m['max'])}
                                    % endif
                                % else:
                                    0
                                % endif
                            % else:
                                ø
                            % endif
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
</div>
