<%inherit file="/individual/show.mako" />

${h.ui.Measurements(_id, publications_list, measures_infos, traits, full=True, species=species)}

