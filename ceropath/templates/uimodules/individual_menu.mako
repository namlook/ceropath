<!-- the tabs -->
<ul class="css-tabs">
    <li><a href="${h.url(h.url_for('individual_show', id=_id))}">General Informations</a></li>
    <li><a href="${h.url(h.url_for('individual_trapping', id=_id))}">Trapping Informations</a></li>
    <li><a href="${h.url(h.url_for('species_individuals', id=_id))}">Parasites</a></li> 
    ##% for module_name in modules:
    ##    <li><a href="${h.url(h.url_for('species_module', id=_id, name=module_name))}">${module_name.capitalize()}</a></li>
    ##% endfor
</ul>

