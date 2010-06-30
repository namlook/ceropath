<%inherit file="/root.mako" />

<style>
td {
    text-align:center;
}
</style>

<h1> Parasites found on ${_id.upper()} </h1>

<div style="padding-bottom:10px;">
    <a href="#">Home</a> » <a href="${h.url(h.url_for('individual_show', id=_id))}">${_id}</a> » parasites
</div>

<div class="unit on-1 columns">
    <div class="column">
        ${h.ui.ParasitesList(rel_host_parasites, individual=_id)}
    </div>
</div>


