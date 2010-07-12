<%inherit file="/root.mako" />

<style>
    td{
        padding-top:3px;
    }
</style>

<script type="text/javascript" src="/js/jquery.autoSuggest.packed.js"></script>
<link rel="stylesheet" href="/css/autoSuggest.css"> 

<script>
$('document').ready(function(){
    $("input[type=text]").autoSuggest("${h.url(h.url_for('species_filter'))}", {
        minChars: 2,
        matchCase: false,
        selectionAdded: function(elem){$('form').submit();},
        selectedItemProp: 'name',
        asHtmlID: 'filter',
        startText: 'enter a rank...',
        formatList: function(data, elem){
            return elem.html(data.name);
        },
    });
});
</script>

<div class="span-30">
    <div style="padding-top:10px;">
        <form action="${h.url(h.url_for('species_index'))}" method="post">
            <fieldset><legend>Sort the list by typing a taxonomic rank...</legend>
                <input class="suggest" type="text" />
            </fieldset>
        </form>
    </div>
</div>

<div class="span-30">
    % if enable_back:
        <a href="${h.url(h.url_for('species_index'))}">back to full list</a>
    % endif

    <table>
        <tr><th>Species</th><th>Common name</th><th>Thai Name</th><th>Lao Name</th><th>IUCN status</th><th>IUCN trend</th><th>IUCN version</th></tr>
        % for species in species_list:
            <tr>
                <td>
                    <i><a href="${h.url(h.url_for('species_show', id=species['_id']))}">${species['_id'].capitalize()}</a></i>
                    ${species['reference']['biblio']['author_date']}
                </td>
                <td>${species['name']['common']['english']}</td>
                <td>${species['name']['common']['thai']}</td>
                <td>${species['name']['common']['lao']}</td>
                <td>${species['iucn']['status']}</td>
                <td>${species['iucn']['trend']}</td>
                <td style="text-align:center">${species['iucn']['red_list_criteria_version']}</td>
            </tr>
        % endfor
    </table>
</div>

