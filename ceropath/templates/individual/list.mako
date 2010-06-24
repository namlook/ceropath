<%inherit file="/root.mako" />

<style>
td {
    text-align:center;
}
</style>

<div class="unit on-1 columns">
<div class="column">
<table>
    <tr><th>Individu Number</th><th> Sex</th><th> Country</th><th> Province</th><th>Identification Type</th><th>Identification Date</th><th> Remarks about Identification</th><tr>
    % for individual in individuals_list:
        <tr>
            <td><a href="${h.url(h.url_for('individual_show', id=individual['_id']))}">${individual['_id'].upper()}</a></td>
            <td>${(individual['sex'] or '').upper()}</td>
            <td></td>
            <td></td>
            <td>${individual['identification']['type']}</td>
            <td>${individual['identification']['date'].date() if individual['identification']['date'] else ''}</td>
            <td>${individual['identification']['method']}</td>
        </tr>
    % endfor
</table>
</div>
</div>
