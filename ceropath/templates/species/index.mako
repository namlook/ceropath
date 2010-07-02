<%inherit file="/root.mako" />

<div class="column" style="width:1200px;">
<table>
    <tr><th>Species</th><th>Common name</th><th>Thai Name</th><th>IUCN status</th><th>IUCN trend</th></tr>
    % for species in species_list:
        <tr>
            <td><a href="${h.url(h.url_for('species_show', id=species['_id']))}">${species['_id'].capitalize()}</a></td>
            <td>${species['name']['common']['english']}</td>
            <td>${species['name']['common']['thai']}</td>
            <td>${species['iucn']['status']}</td>
            <td>${species['iucn']['trend']}</td>
        </tr>
    % endfor
</table>
</div>

