<%inherit file="/root.mako" />

<h1> BLAAAAAAAAAAAAAAAAAAAAA</h1>

## XXX a supprimer

<div class="span-30" style="padding-bottom:10px;padding-top:10px;">
    <a href="${h.url(h.url_for('species_index'))}">Home</a> » <a href="${h.url(h.url_for('species_show', id=species))}">${species.capitalize()}</a> » individuals
</div>

<div class="span-30">
    <table>
        <tr><th>Individual ID</th><th> Sex</th><th> Country</th><th> Province</th><th>Identification Type</th><th>Identification Date</th><th> Remarks about Identification</th><tr>
        % for _id, (individual, site) in sorted(individuals.items()):
            <tr>
                <td><a href="${h.url(h.url_for('individual_show', id=individual['_id']))}">${individual['_id'].upper()}</a></td>
                <td>${(individual['sex'] or '').upper()}</td>
                <td>
                    % if site['country']:
                        ${site['country']}
                    % endif
                </td>
                <td>
                    % if site['province']:
                        ${site['province']}
                    % endif
                </td>
                <td>${individual['identification']['type']}</td>
                <td>
                    % if individual['identification']['date']:
                        ${individual['identification']['date'].date()}
                    % endif
                </td>
                <td>${individual['identification']['method']}</td>
            </tr>
        % endfor
    </table>
</div>


