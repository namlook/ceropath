<%inherit file="/individual/show.mako" />

<style>
table.measurements td{
    border:1px solid #E6E6E6;
    padding:10px;
}
</style>

<div class="column span-4">
    <div class="container" style="padding:10px;">

    <%
         theaders = [(_id, 'individual'), (species, 'species')]
         theaders.extend((i, 'pubref') for i in publications_list.keys())
     %>
    <table class="measurements">
        <tr><th></th>
        % for header in theaders:
            % if header[1] == 'pubref':
                <% author, date = h.author_date_from_citation(publications_list[header[0]]['reference']) %>
                <th>
                    Measurements in <a href="" title="${publications_list[header[0]]['reference']}">(${author}, ${date})</a>
                    for ${species.capitalize()} <small>(a)</small>
                 </th>
            % elif header[1] == 'species':
                <th>Ceropath Measurements for ${header[0].capitalize()} <small>(a)</small></th>
            % else:
                <th>Measurements for ${header[0].upper()} ${age}</th>
            % endif
        % endfor
        </tr>
        % for trait, measure in sorted(measures_infos.items()):
            <tr><td>${trait}</td>
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
                        <b>
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
                        </b>
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
</div>


<div class="fixed column">
    % if image_path:
        <img style="padding-left:10px;padding-bottom:10px;" src="${image_path}" width="390px" />
    % endif
    <fieldset><legend>Informations</legend>
        <table>
            <tr><th>species</th><td><a href="${h.url(h.url_for('species_show', id=species))}">${species.capitalize()}</a></td></tr>
            <tr><th>sex</th><td>${sex}</td></tr>
            <tr><th>age</th><td>${age}</td></tr>
            <tr><th>dissection date</th><td>${dissection_date}</td></tr>
        </table>
    </fieldset>

</div>


