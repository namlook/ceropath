
<!-- the tabs -->
<ul class="css-tabs">
    <li><a href="${h.url(h.url_for('species_show', id=_id))}">General Informations</a></li>
    <li><a href="${h.url(h.url_for('species_measurements', id=_id))}">Measurements</a></li>
    <li><a href="${h.url(h.url_for('species_vouchers', id=_id))}">Vouchers</a></li> 
    <li><a href="${h.url(h.url_for('species_individuals', id=_id))}">Individus</a></li> 
    ##% for module_name in modules:
    ##    <li><a href="${h.url(h.url_for('species_module', id=_id, name=module_name))}">${module_name.capitalize()}</a></li>
    ##% endfor
</ul>

