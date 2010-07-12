
<!-- the tabs -->
<ul class="css-tabs">
    <li><a href="${h.url(h.url_for('species_show', id=_id))}">General Informations</a></li>
    <li><a href="${h.url(h.url_for('species_measurements', id=_id))}">Measurements</a></li>
    <li><a href="${h.url(h.url_for('species_sampling_map', id=_id))}">Sampling Map</a></li>
    <li><a href="${h.url(h.url_for('species_vouchers', id=_id))}">Vouchers</a></li> 
    <li><a href="${h.url(h.url_for('species_individuals', id=_id))}">Individuals</a></li> 
    <li><a href="${h.url(h.url_for('species_parasites', id=_id))}">Parasites</a></li> 
</ul>

