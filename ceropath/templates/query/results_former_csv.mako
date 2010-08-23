<% from mongokit import DBRef %>

<% fields = ['individual', 'type', u'date', u'organism_classification', u'operator', u'remark'] %>

% for th in fields:
${th};
% endfor
|||

% for item in results:
    % for field in fields:
        % if field == 'individual':
${item[field].id};
        % else:
            % if isinstance(item[field], DBRef):
<% item[field] = item[field].id %>
            % endif
${item[field]};
        % endif
    % endfor
|||
% endfor
