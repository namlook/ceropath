<%inherit file="/root.mako" />

<link rel="stylesheet" type="text/css" href="/rdbsea/css/formskin.css"/> 

<script>
$(document).ready(function(){
    $('select[multiple]=multiple').live('change', function(value){
        var id = $(this).attr('id');
        var field = $("select#"+id+" > option:selected").text();
        var target = $(this).attr('t');
        var res = $.get("/rdbsea/query/expand", {'name':$(this).attr('name'), 'values':field}, function(data){
            $('#'+target).empty();
            for(var i=0;i<data.length;i++){
                $('#'+target).append('<option>'+data[i]+'&nbsp;</option>'); 
            }
        });
    });
    $(":date").dateinput({selectors: true,});
    $('.select-all').click(function(){
        var id = $(this).attr('id');
        if($(this).attr('checked')){
            $("select[name="+id+"] > option").each(function(){;
                $(this).attr('selected', 'selected');
            });
        }
        else{
            $("select[name="+id+"] > option").each(function(){;
                $(this).attr('selected', '');
            });
        }
    });
});
</script>

<style>

    th{
        padding:5px;
    }
    select{
        height:100%;
        width:100%;
    }
</style>

<div class="span-30 last">
<h1>South East Asian Rodents Data Base queries generator</h1>

<form action="${h.url(h.url_for('query_run'))}" method="get">
<fieldset><legend><h2>Query by individual id...</h2></legend>
    <input type="text" name="individual_id" />
</fieldset>

<fieldset><legend><h2>... or by</h2></legend>
<div class="span-29">
    <div class="span-9">
        <h3>taxonomy</h3>
        <table>
            <tr><th>family</th><th>genus</th><th>species</th></tr>
            <tr><td>
            <select id="family" name="family" t="genus" multiple="multiple">
                % for family in family_genus:
                    <option value="${family}">${family}&nbsp;</option>
                % endfor
            </select>
            </td><td>
            <select id="genus" name="genus" t="species" multiple="multiple">
            </select>
            </td><td>
            <select id="species" name="species" multiple="multiple">
            </select>
            </td></tr>
        </table>
    </div>

    <div class="span-9">
    <h3>administrative division</h3>
        <table>
            <tr><th>country</th><th>province</th><th>place</th></tr>
            <tr><td>
            <select id="country" name="country" t="province" multiple="multiple">
                % for country in country_province:
                    <option value="${country}">${country}&nbsp;</option>
                % endfor
            </select>
            </td><td>
            <select id="province" name="province" t="place" multiple="multiple">
            </select>
            </td><td>
            <select id="place" name="place" multiple="multiple">
            </select>
            </td></tr>
        </table>
    </div>

    <div class="span-9 last">
    <h3>topology</h3>
    <table>
        <tr><th>low</th><th>medium</th></tr>
        <tr><td>
        <select id="low" name="low" t="medium" multiple="multiple">
            % for low in typo_low_medium:
                <option value="${low}">${low}&nbsp;</option>
            % endfor
        </select>
        </td><td>
        <select id="medium" name="medium" multiple="multiple">
        </select>
        </td></tr>
    </table>
    </div>
</div>



<div class="span-29">
    <div class="span-9">
    <h3>other</h3>
      <table>
        <tr><th>sex</th><th>mission number</th></tr>
        <tr><td>
        <select id="sex" name="sex" multiple="multiple">
            <option value="f">f&nbsp;</option>
            <option value="m">m&nbsp;</option>
        </select>
        </td><td>
        <select id="mission_id" name="mission_id" multiple="multiple">
            % for mission_number in mission_numbers:
                <option value="${mission_number}">${mission_number}&nbsp;</option>
            % endfor
        </select>
        </td></tr>
    </table>
    </div>

    <div class="span-18">
        <h3>dissection date</h3>
        <div><label>choose a date :</label> <input type="date" name="dissection_date" /></div>
        <div><label>or beetween </label> <input type="date" name="dissection_date_start" />
        <label> and </label> <input type="date" name="dissection_date_end" /></div>
    </div>
</div>
</fieldset>

<h1>Display information</h1>

<fieldset><legend><h2> Choose the information you want to display... </h2></legend>

<p>check the boxes to select/unselect all</p>

<table>
    <tr>
        <th>individual information <input type="checkbox" class="select-all" id="filter::individual" /></th>
        <th>measures <input type="checkbox" class="select-all" id="filter::measures" /></th>
        <th>physiologic features <input type="checkbox" class="select-all" id="filter::physiologic_features" /></th>
    </tr>
    <tr>
        <td><select name="filter::individual" multiple="multiple">
            % for field in individual:
                <option name=${field}>${field}</option>
            % endfor
        </select></td>
        <td><select name="filter::measures" multiple="multiple">
            % for measure in measures:
                <option name=${measure}>${measure}</option>
            % endfor
        </select></td>
        <td><select name="filter::physiologic_features" multiple="multiple">
            % for feature in physiologic_features:
                <option name=${feature}>${feature}</option>
            % endfor
        </select></td>
    </tr>
</table>

<table>
    <tr>
        <th>microparasites <input type="checkbox" class="select-all" id="filter::microparasites" /></th>
        <th>macroparasites <input type="checkbox" class="select-all" id="filter::macroparasites" /></th>
        <th>sequences <input type="checkbox" class="select-all" id="filter::sequences" /></th>
        <th>samples <input type="checkbox" class="select-all" id="filter::samples" /></th>
    </tr>
    <tr>
         <td><select name="filter::microparasites" multiple="multiple">
            % for parasite in microparasites:
                <option name=${parasite}>${parasite}</option>
            % endfor
        </select></td>
        <td><select name="filter::macroparasites" multiple="multiple">
            % for parasite in macroparasites:
                <option name=${parasite}>${parasite}</option>
            % endfor
        </select></td>
        <td><select name="filter::sequences" multiple="multiple">
            % for gene in genes:
                <option name=${gene}>${gene}</option>
            % endfor
        </select></td>
        <td><select name="filter::samples" multiple="multiple">
            % for sample in samples:
                <option name=${sample}>${sample}</option>
            % endfor
        </select></td>
    </tr>
</table>
</fieldset>

<fieldset><legend><h2>... or display only former identifications</h2></legend>
<table>
    <tr><th>former identification <input type="checkbox" class="select-all" id="filter::former_identification" /></th></tr>
    <tr><td><select name="filter::former_identification" multiple="multiple">
        % for identification in former_identification:
            <option name=${identification}>${identification}</option>
        % endfor
    </select></td></tr>
</table>
</fieldset>

<input type="submit" />

</form>

</div>

