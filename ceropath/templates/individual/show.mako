<%inherit file="/root.mako" />

<div class="unit on-6 columns" style="width:1200px;">
    <h1><i>${_id.upper()}</i> <small>(<a href="${h.url(h.url_for('species_show', id=species))}">${species.capitalize()}</a>)</small></h1>

    <div style="padding-bottom:10px;">
    <a href="#">Home</a> » <a href="${h.url(h.url_for('species_individuals', id=species))}">Individual</a> » ${_id.upper()}
    </div>

    ${h.ui.SpeciesMenu(_id)}

    ${self.body()}
</div>
