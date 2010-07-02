<%inherit file="/root.mako" />

<div class="unit on-6 columns" style="width:1200px;">
    <h1><i>${_id.capitalize()}</i> <small>(${author}, ${date})</small></h1>

    <div style="padding-bottom:10px;">
    <a href="${h.url(h.url_for('species_index'))}">Home</a> » <a href="${h.url(h.url_for('species_index'))}">Species</a> » ${_id.capitalize()}
    </div>

    ${h.ui.SpeciesMenu(_id)}

    ${self.body()}

</div>
