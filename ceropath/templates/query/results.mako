<% from mongokit import DotCollapsedDict, DBRef %>

<a href="${h.url(h.url_for('query_run', query=query, filters=filters, target='csv'))}">Download data in csv format</a>

<style>
tr:nth-child(even) {background: #F6FFDE}
tr:nth-child(odd) {background: #FFF}
</style>

<h2>Found ${results.count()} results</h2>

<table>
<tr>
    <th>individual id</th>
% for filt in sorted(filters):
    % for field in sorted(filters[filt]):
        <th style="padding:5px;">${field}</th>
    % endfor
% endfor
</tr>
% for item in results:
    <% item = DotCollapsedDict(item) %>
    <tr>
        <th style="padding:5px;">${item['_id'].upper()}</th>
        % for filt in sorted(filters):
            % for field in sorted(filters[filt]):
                <td style="text-align:center;padding:5px;">
                % if filt == 'individual':
                    <%
                        if ' >> ' in field:
                            field = field.replace(' >> ', '.')
                        if isinstance(item[field], DBRef):
                            item[field] = item[field].id
                    %>
                    <pre>${item[field]}</pre>
                % elif filt=='measures':
                    <%measures = dict((i['trait'], i['value']) for i in item['measures'])%>
                    <pre>${measures.get(field)}</pre>
                % elif filt=='physiologic_features':
                    <%physiologic_features = dict((i['type'], i['value']) for i in item['physiologic_features'])%>
                    <pre>${physiologic_features.get(field)}</pre>
                % elif filt=='microparasites':
                    <%microparasites = dict((i['method'], i['status']) for i in item['microparasites'])%>
                    <pre>${microparasites.get(field)}</pre>
                % elif filt=='macroparasites':
                    <%macroparasites = dict((i['name'], i['quantity']) for i in item['macroparasites'])%>
                    <pre>${macroparasites.get(field)}</pre>
                % elif filt=='samples':
                    <%samples = dict((i['name'], ([j.id for j in i['institute']], [j.id for j in i['responsible']])) for i in item['samples'])%>
                       % if samples.get(field):
                           <% institute, responsible = samples.get(field) %>
                           % if responsible:
                                <pre>${responsible[0]}</pre>
                           % endif
                           % if institute: 
                                <pre>(${institute[0]})</pre>
                           % endif
                       % endif
                % elif filt=='sequences':
                    <% seq = db.sequence.find_one({"gene.$id":field, "individual.$id":item['_id']}, fields=['sequence']) %>
                    % if seq:
                        <pre>${seq['sequence']}</pre>
                    % endif
                % endif
            </td>
            % endfor
        % endfor
    </tr>
% endfor
</table>
