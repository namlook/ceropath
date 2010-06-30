<%inherit file="/root.mako" />

<style>
td {
    text-align:center;
}
</style>

<div style="padding-bottom:10px;">
    <a href="#">Home</a> » <a href="${h.url(h.url_for('species_show', id=species))}">Species</a> » individuals
</div>

<div class="unit on-1 columns">
    <div class="column">
        <table>
            <tr><th>Individu Number</th><th> Sex</th><th> Country</th><th> Province</th><th>Identification Type</th><th>Identification Date</th><th> Remarks about Identification</th><tr>
            % for _id, (individual, site) in individuals.iteritems():
                <tr>
                    <td><a href="${h.url(h.url_for('individual_show', id=individual['_id']))}">${individual['_id'].upper()}</a></td>
                    <td>${(individual['sex'] or '').upper()}</td>
                    <td>${h.format_loc_name(site['country'] if site is not None else '')}</td>
                    <td>${h.format_loc_name(site['province'] if site is not None else '')}</td>
                    <td>${individual['identification']['type']}</td>
                    <td>${individual['identification']['date'].date() if individual['identification']['date'] else ''}</td>
                    <td>${individual['identification']['method']}</td>
                </tr>
            % endfor
        </table>
    </div>
</div>


