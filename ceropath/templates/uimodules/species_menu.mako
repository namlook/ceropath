
<%def name="current(name)">
    % if tmpl_context.action == name:
        current
    % endif
</%def>

<!-- the tabs -->
<ul class="css-tabs">
    <li class="${current('show')}"><a href="${h.url(h.url_for('species_show', id=_id))}">General Information</a></li>
    <li class="${current('measurements')}"><a href="${h.url(h.url_for('species_measurements', id=_id))}">Measurements</a></li>
    <li class="${current('sampling_map')}"><a href="${h.url(h.url_for('species_sampling_map', id=_id))}">Sampling Map</a></li>
    <li class="${current('vouchers')}"><a href="${h.url(h.url_for('species_vouchers', id=_id))}">Vouchers</a></li> 
    <li class="${current('individuals')}"><a href="${h.url(h.url_for('species_individuals', id=_id))}">Individuals</a></li> 
    <li class="${current('parasites')}"><a href="${h.url(h.url_for('species_parasites', id=_id))}">Parasites</a></li> 
</ul>

