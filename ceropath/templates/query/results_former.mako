<% from mongokit import DBRef %>

<a href="${h.url(h.url_for('query_run', query=query, filters=filters, target='csv'))}">Download data in csv format</a>

<style>
tr:nth-child(even) {background: #F6FFDE}
tr:nth-child(odd) {background: #FFF}
</style>

<h2>Found ${results.count()} results</h2>

<% fields = ['individual', 'type', u'date', u'organism_classification', u'operator', u'remark'] %>

<table>
<tr>
    % for th in fields:
        <th style="padding:5px;">${th}</th>
    % endfor
</tr>
% for item in results:
    <tr>
        % for field in fields:
            % if field == 'individual':
                <th style="padding:5px;">${item[field].id.upper()}</th>
            % else:
                % if isinstance(item[field], DBRef):
                    <% item[field] = item[field].id %>
                % endif
                <td style="padding:5px;">${item[field]}</td>
            % endif
        % endfor
    </tr>
% endfor
</table>
