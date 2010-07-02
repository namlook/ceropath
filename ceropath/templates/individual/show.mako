<%inherit file="/root.mako" />

<div class="unit on-6 columns" style="width:1200px;">
    <h1><i>${_id.upper()}</i> <small><i><a href="${h.url(h.url_for('species_show', id=species))}">${species.capitalize()}</a></i> ${'(voucher)' if voucher else ''}</small></h1>

    <div style="padding-bottom:10px;">
    <a href="${h.url(h.url_for('species_index'))}">Home</a> » <a href="${h.url(h.url_for('species_individuals', id=species))}">${species.capitalize()}'s individuals</a> » ${_id.upper()}
    </div>

    ${h.ui.IndividualMenu(_id)}

    ${self.body()}
</div>
