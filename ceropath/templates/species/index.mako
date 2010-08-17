<%inherit file="/root.mako" />

<style>
    td{
        padding-top:3px;
    }
</style>

<script type="text/javascript" src="/rdbsea/js/jquery.autoSuggest.packed.js"></script>
<link rel="stylesheet" href="/rdbsea/css/autoSuggest.css"> 
<script type="text/javascript" language="javascript" src="/rdbsea/js/jquery.dataTables.js"></script> 

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
    $('#index').dataTable({
      "bPaginate": false,  
      "oLanguage": {
        "sSearch": "Search by all other values:  ",
      }
    });
});

</script>

<div class="span-30">
    % if enable_back:
        <a href="${h.url(h.url_for('species_index'))}">back to full list</a>
    % endif

    <div style="padding-top:10px">
        <div style="float:left;padding-right:5px;padding-top:10px">Search by taxonomic rank:</div> 
        <div style="width:350px;heigth:70px;">
            <form action="${h.url(h.url_for('species_index'))}" method="post">
                   <input class="suggest" type="text" />
            </form>
        </div>
    </div>


    <table id="index">
        <thead>
        <tr>
            <th>Species</th>
            <th>Common Name</th>
            <th>Thai Name</th>
            <th>Lao Name</th>
            <th>Khmer Name</th>
            <th>IUCN status</th>
            <th>IUCN trend</th>
            <th>IUCN version</th>
        </tr>
        </thead>
        <tbody>
        % for species in species_list:
            <tr>
                <td>
                    <i><a href="${h.url(h.url_for('species_show', id=species['_id']))}">${species['_id'].capitalize()}</a></i>
                    ${species['reference']['biblio']['author_date']}
                </td>
                <td>${species['name']['common']['english']}</td>
                <td>${species['name']['common']['thai']}</td>
                <td>${species['name']['common']['lao']}</td>
                <td>${species['name']['common']['khmer']}</td>
                <td>${species['iucn']['status']}</td>
                <td>${species['iucn']['trend']}</td>
                <td style="text-align:center">${species['iucn']['red_list_criteria_version']}</td>
            </tr>
        % endfor
        </tbody>
    </table>
</div>

