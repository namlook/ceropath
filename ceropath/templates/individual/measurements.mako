<%inherit file="/individual/show.mako" />

<div class="span-30">
${h.ui.Measurements(_id, publications_list, measures_infos, traits, full=True, species=species)}
</div>

