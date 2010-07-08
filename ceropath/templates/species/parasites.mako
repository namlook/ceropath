<%inherit file="/root.mako" />

<style>
td {
    text-align:center;
}
</style>

<h1> Parasites found on ${species.capitalize()} </h1>

<div style="padding-bottom:10px;">
    <a href="${h.url(h.url_for('species_index'))}">Home</a> » <a href="${h.url(h.url_for('species_show', id=species))}">${species.capitalize()}</a> » parasites
</div>

<div class="unit on-1 columns">
    <div class="column">
        ${h.ui.ParasitesList(rel_host_parasites, species=species)}
    </div>
</div>


