<%def name="current(name)">
    % if tmpl_context.action == name:
        current
    % endif
</%def>

<!-- the tabs -->
<ul class="css-tabs">
    <li class="${current('show')}"><a href="${h.url(h.url_for('individual_show', id=_id))}">General Informations</a></li>
    <li class="${current('trapping')}"><a href="${h.url(h.url_for('individual_trapping', id=_id))}">Trapping Informations</a></li>
    <li class="${current('samples')}"><a href="${h.url(h.url_for('individual_samples', id=_id))}">Samples</a></li> 
</ul>

