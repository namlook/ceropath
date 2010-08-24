<% from mongokit import DotCollapsedDict, DBRef %>
<% from datetime import datetime %>


id;
% for filt in sorted(filters):
    % for field in sorted(filters[filt]):
${h.literal(field)};
    % endfor
% endfor
:::

% for item in results:
    <% item = DotCollapsedDict(item) %>
${item['_id'].upper()};
        % for filt in sorted(filters):
            % for field in sorted(filters[filt]):
                % if filt == 'individual':
                    <%
                        if ' >> ' in field:
                            field = field.replace(' >> ', '.')
                        if isinstance(item[field], DBRef):
                            item[field] = item[field].id
                            if field == "organism_classification":
                                item[field] = " ".join(i.capitalize() for i in item[field].split())
                        elif isinstance(item[field], datetime):
                            item[field] = item[field].date()
                    %>
${item[field]};
                % elif filt=='measures':
                    <%measures = dict((i['trait'], i['value']) for i in item['measures'])%>
${measures.get(field)};
                % elif filt=='physiologic_features':
                    <%physiologic_features = dict((i['type'], i['value']) for i in item['physiologic_features'])%>
${physiologic_features.get(field)};
                % elif filt=='microparasites':
                    <%microparasites = dict((i['method'], i['status']) for i in item['microparasites'])%>
${microparasites.get(field)};
                % elif filt=='macroparasites':
                    <%macroparasites = dict((i['name'], i['quantity']) for i in item['macroparasites'])%>
${macroparasites.get(field)};
                % elif filt=='samples':
                    <%samples = dict((i['name'], ([j.id for j in i['institute']], [j.id for j in i['responsible']])) for i in item['samples'])%>
                       % if samples.get(field):
                           <% institute, responsible = samples.get(field) %>
                           % if responsible:
${responsible[0]};
                           % endif
                           % if institute: 
(${institute[0]});
                           % endif
                       % endif
                % elif filt=='sequences':
                    <% seq = db.sequence.find_one({"gene.$id":field, "individual.$id":item['_id']}, fields=['sequence']) %>
                    % if seq:
${seq['sequence']};
                    % endif
                % elif filt=='sites':
                    <% site = db.site.get_from_id(item['trapping_informations.site'].id) %>
${site[field]};
                % endif
            % endfor
        % endfor
:::
% endfor
