<%inherit file="/species/show.mako" />

<div class="span-30" style="padding-top:10px;">
    <table>
        <tr><th>Individu Number</th><th> Sex</th><th> Country</th><th> Province</th><th>Identification Type</th><th>Identification Date</th><th> Remarks about Identification</th><tr>
        % for _id, (individual, site) in sorted(individuals.items()):
            <tr>
                <td><a href="${h.url(h.url_for('individual_show', id=individual['_id']))}">${individual['_id'].upper()}</a></td>
                <td>${(individual['sex'] or '').upper()}</td>
                <td>${site['country'] if site is not None else ''}</td>
                <td>${site['province'] if site is not None else ''}</td>
                <td>${individual['identification']['type']}</td>
                <td>${individual['identification']['date'].date() if individual['identification']['date'] else ''}</td>
                <td>${individual['identification']['method']}</td>
            </tr>
        % endfor
    </table>
</div>


