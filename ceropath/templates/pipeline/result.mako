<%inherit file="/root.mako" />

<div class="span-30">
<div><a href="${h.url(h.url_for('pipeline_index'))}">back</a></div>
% if result:
    % if output_format == 'svg':
        <iframe src ="${h.url(h.url_for('pipeline_servesvg', name=result))}" width="100%" height="80%">
            <p>Your browser does not support iframes.</p>
        </iframe>
    % elif output_format == 'nwk':
        <style>
            .species{
                color: #FFB010;
            }
        </style>
        <tt>${h.literal(result)}</tt>
    % else:
        <pre>${result}</pre>
    % endif
% elif errors:
    <pre>${errors}</pre>
% endif
</div>

