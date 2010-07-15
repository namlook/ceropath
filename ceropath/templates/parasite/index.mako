<%inherit file="/root.mako" />

<style>
    td{
        padding-top:3px;
    }
</style>

<script type="text/javascript" src="/js/jquery.autoSuggest.packed.js"></script>
<link rel="stylesheet" href="/css/autoSuggest.css"> 
<script type="text/javascript" language="javascript" src="/js/jquery.dataTables.js"></script> 

<script>
$('document').ready(function(){
    $("input[type=text]").autoSuggest("${h.url(h.url_for('parasite_filter'))}", {
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
    $('.dyntable').dataTable({
      "bPaginate": false,  
      "oLanguage": {
        "sSearch": "Search by all other values:  ",
      }
    });
});
</script>

<div class="span-30">
    <div style="padding-top:10px;">
        <form action="${h.url(h.url_for('parasite_index'))}" method="post">
            <fieldset><legend>Sort the list by typing a taxonomic rank...</legend>
                <input class="suggest" type="text" />
            </fieldset>
        </form>
    </div>
</div>


<style>
td{
    padding-right:30px;
}

fieldset{
    padding-top:20px;
    border:1px solid #F3F3F3;
}
</style>

<div class="span-30">
    % if enable_back:
        <a href="${h.url(h.url_for('parasite_index'))}">back to full list</a>
    % endif

    % for kingdom in sorted(parasites):
        <fieldset><legend><h2>${kingdom.capitalize()}</h2></legend>
        <table class="span-29 dyntable">
        <thead>
        <tr>
            <th>Phylum</th>
            <th>Class</th>
            <th>Order</th>
            <th>Family</th>
            <th>Genus</th>
            <th>Parasites</th>
        <tr>
        </thead>
        <tbody>
        % for parasite in sorted(parasites[kingdom]):
            <%
                phylum = parasite['taxonomic_rank']['phylum']
                _class = parasite['taxonomic_rank']['class']
                order = parasite['taxonomic_rank']['order']
                family = parasite['taxonomic_rank']['family']
                genus = parasite['taxonomic_rank']['genus']
            %>
            <tr>
                <td>${phylum.capitalize() if phylum else "unknown"}</td>
                <td>${_class.capitalize() if _class else "unknown"}</td>
                <td>${order.capitalize() if order else "unknown"}</td>
                <td>${family.capitalize() if family else "unknown"}</td>
                <td>${genus.capitalize() if genus else "unknown"}</td>
                <td><i><a href="${h.url(h.url_for('parasite_show', id=parasite['_id']))}">${parasite['_id'].capitalize()}</a></i></td>
            </tr>
        % endfor
        </tbody>
        </table>
        </fieldset>
    % endfor
</div>
