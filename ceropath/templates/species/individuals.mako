<%inherit file="/species/show.mako" />

<script type="text/javascript" language="javascript" src="/js/jquery.dataTables.js"></script> 

<script>
$('document').ready(function(){
    $('.dyntable').dataTable({
      "bPaginate": false,  
      "oLanguage": {
        "sSearch": "Search by all other values:  ",
      }
    });
});
</script>


<div class="span-30" style="padding-top:10px;">
    <table class="dyntable">
        <thead>
        <tr><th>Individual ID</th><th> Sex</th><th> Country</th><th> Province</th><th>Identification Type</th><th>Identification Date</th><th> Remarks about Identification</th><tr>
        </thead>
        <tbody>
        % for _id, (individual, site) in sorted(individuals.items()):
            <tr>
                <td><a href="${h.url(h.url_for('individual_show', id=individual['_id']))}">${individual['_id'].upper()}</a></td>
                <td>${(individual['sex'] or '').upper()}</td>
                <td>
                    % if site is not None:
                        ${site['country']}
                    % endif
                </td>
                <td>
                    % if site is not None:
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
        </tbody>
    </table>
</div>


