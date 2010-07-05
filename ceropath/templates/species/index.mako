<%inherit file="/root.mako" />

<style>
    td{
        padding-left:5px;
        padding-right:15px;
        padding-top:3px;
    }
</style>

<div class="column" style="width:1200px;">
<table>
    <tr><th>Species</th><th>Common name</th><th>Thai Name</th><th>Lao Name</th><th>IUCN status</th><th>IUCN trend</th></tr>
    % for species in species_list:
        <tr>
            <td>
                <i><a href="${h.url(h.url_for('species_show', id=species['_id']))}">${species['_id'].capitalize()}</a></i>
                (${species['reference']['biblio']['author'].split(',')[0]}, ${species['reference']['biblio']['date']})
                ##${species['reference']['biblio']['author_date']}
            </td>
            <td>${species['name']['common']['english']}</td>
            <td>${species['name']['common']['thai']}</td>
            <td>${species['name']['common']['lao']}</td>
            <td>${species['iucn']['status']}</td>
            <td>${species['iucn']['trend']}</td>
        </tr>
    % endfor
</table>
</div>

