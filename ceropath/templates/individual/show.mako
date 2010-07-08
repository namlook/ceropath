<%inherit file="/root.mako" />

<div class="span-30">
    % if voucher:
        <h1><i>${_id.upper()}</i> <small>is a barcoding voucher for <i><a href="${h.url(h.url_for('species_show', id=species))}">${species.capitalize()}</a></i></small></h1>
    % else:
        <h1><i>${_id.upper()}</i> <small><i><a href="${h.url(h.url_for('species_show', id=species))}">${species.capitalize()}</a></i></small></h1>
    % endif

    <div style="padding-bottom:10px;">
        <a href="${h.url(h.url_for('species_index'))}">Home</a> » <a href="${h.url(h.url_for('species_individuals', id=species))}">${species.capitalize()}'s individuals</a> » ${_id.upper()}
    </div>

    ${h.ui.IndividualMenu(_id)}
</div>

    ${self.body()}
