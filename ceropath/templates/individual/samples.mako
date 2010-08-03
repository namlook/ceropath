<%inherit file="/individual/show.mako" />

<style>
tr:nth-child(even) {background: #FFF}
tr:nth-child(odd) {background: #F6FFDE}
</style>

<div class="span-30">
% for sample in samples:
    <fieldset><legend><h3>${sample['name']}</h3></legend>
    <table class="span-29">
        <tr><th class="span-5">Sample Type</th><td>${sample['name']}</td></tr>
        <tr><th>Conservation</th><td>${sample['conservation_method']}</td></tr>
        <tr><th>Samples owner</th><td>${samples_owner}</td></tr>
        <tr><th>Institute</th><td>
            % for institute in sample['institute']:
                <a href="${h.url(h.url_for('institute_show', id=institute['_id']))}">${institute['_id']}</a><br />
            % endfor
        </td></tr>
        <tr><th>Responsible</th><td>
            % for responsible in sample['responsible']:
                <a href="mailto:${responsible['email']}">${responsible['_id']}</a>
                (<a href="${h.url(h.url_for('institute_show', id=responsible['affiliation']['_id']))}">${responsible['affiliation']['_id']}</a>)
                 ${responsible['office_phone']}<br />
            % endfor
        </td></tr>
        <tr><th>Project institute</th><td>
            % for institute in sample['project_institute']:
                <a href="${h.url(h.url_for('institute_show', id=institute['_id']))}">${institute['_id']}</a><br />
            % endfor
        </td></tr>
        <tr><th>Project responsible</th><td>
            % for responsible in sample['project_responsible']:
                <a href="mailto:${responsible['email']}">${responsible['_id']}</a>
                (<a href="${h.url(h.url_for('institute_show', id=responsible['affiliation']['_id']))}">${responsible['affiliation']['_id']}</a>)
                ${responsible['office_phone']}<br />
            % endfor
        </td></tr>
    </table>
    </fieldset>
% endfor 
</div>
