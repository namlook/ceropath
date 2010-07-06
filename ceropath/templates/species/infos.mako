<%inherit file="/species/show.mako" />

<div class="column span-4">
    <div class="container" style="padding:10px;">
        Common names:
        <ul>
            % for language, name in sorted(common_names.items()):
                % if name:
                    <li> <span>${name}</span> (${language}) </li> 
                % endif
            % endfor
        </ul>
        ${h.literal(h.markdownize(description))}

        More information about ${_id.capitalize()} on the
        <a href="http://www.bucknell.edu/msw3/browse.asp?s=y&id=${id_msw3}" target='_blank'>
        Mammal Species of the World</a> website.
    </div>
</div>

<div class="fixed column">
    % if image_path:
        <div>
        <img style="padding-left:10px;padding-bottom:10px;" src="${image_path}" width="390px" />
        </div>
        <div>
        <center><small>© ${_id.capitalize()} by ${photo_author}</small></center>
        </div>
    % endif
    <fieldset><legend>Scientific fields</legend>
        ${h.ui.ModulesList(_id, root="species")}
    </fieldset>
    
    <fieldset style="padding:0px;"><legend><a href="http://www.iucnredlist.org/apps/redlist/details/${iucn_id}" target="_blank">IUCN range map</a></legend>
       <a href="http://www.iucnredlist.org/apps/redlist/images/range/maps/${iucn_id}.png" target="_blank">
        <img src="http://www.iucnredlist.org/apps/redlist/images/range/maps/${iucn_id}.png" width="385px" />
       </a>
    </fieldset>
    <fieldset><legend>Taxonomic ranks</legend>
    <table>
        <%ranks = ['kingdom', 'phylum', 'class', 'order', 'superfamily', 'family', 'subfamily', 'tribe', 'genus', 'subgenus']%>
        % for rank in ranks:
            % if taxonomic_rank[rank]:
                <tr>
                    <th>${rank}</th>
                    <td>${taxonomic_rank[rank].capitalize()}</td>
                </tr>
            % endif
        % endfor
    </table>
    </fieldset>
    % if synonyms:
        <fieldset><legend>Synonyms</legend>
            <table>
            % for synonym, pubref in synonyms.iteritems():
                <tr>
                    <td>${synonym.capitalize()}</td>
                    <td>
                    <a href="${h.url(h.url_for('publication_show', id=pubref['_id']))}">
                    ${h.author_date_from_citation(pubref['reference'])}</a>
                    </td>
                </tr>
            % endfor
            </table>
        </fieldset>
    % endif

</div>

