<%inherit file="/species/show.mako" />

<div class="column span-4">
    <div class="container" style="padding:10px;">

    ${h.literal(h.markdownize(description))}

    </div>
</div>

<div class="fixed column">
    % if image_path:
        <img style="padding-left:10px;padding-bottom:10px;" src="${image_path}" width="390px" />
    % endif
    <fieldset><legend>Also known as</legend>
    <ul>
            % for language, name in sorted(common_names.items()):
                % if name:
                    <li> <span>${name}</span> (${language}) </li> 
                % endif
            % endfor
        </ul>
    </fieldset>

    <fieldset><legend>Taxonomic ranks</legend>
    <table>
        <%ranks = ['kingdom', 'phylum', 'class', 'order', 'superfamily', 'family', 'subfamily', 'tribe', 'genus', 'subgenus']%>
        % for rank in ranks:
            % if taxonomic_rank[rank]:
                <tr>
                    <td><b>${rank}</b> </td>
                    <td>${taxonomic_rank[rank]}</td>
                </tr>
            % endif
        % endfor
    </table>
    </fieldset>
    % if synonyms:
        <fieldset><legend>Synonyms</legend>
        <ul>
        % for synonym in synonyms:
            <li> ${synonym.capitalize()} </li>
        % endfor
        </ul>
        </fieldset>
    % endif

    <fieldset style="padding:0px;"><legend>IUCN range map</legend>
        <img src="http://www.iucnredlist.org/apps/redlist/images/range/maps/${iucn_id}.png" width="390px" />
    </fieldset>
</div>

