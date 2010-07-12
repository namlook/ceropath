<%inherit file="/root.mako" />

<div class="span-30 last">
    <h1><i>${_id.capitalize()}</i> <small>${author_date}</small></h1>

    <div style="padding-bottom:10px;">
    <a href="${h.url(h.url_for('species_index'))}">Home</a> » <a href="${h.url(h.url_for('species_index'))}">Species</a> » ${_id.capitalize()}
    </div>

    ${h.ui.SpeciesMenu(_id)}
</div>

    ${self.body()}

