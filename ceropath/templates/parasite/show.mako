<%inherit file="/root.mako" />

<div class="unit on-6 columns" style="width:1200px;">
    <h1><i>${_id.capitalize()}</i> <small>(${author}, ${date})</small></h1>

    <div style="padding-bottom:10px;">
        % if species:
            <a href="${h.url(h.url_for('species_index'))}">Home</a> » <a href="${h.url(h.url_for('species_parasites', id=species))}">${species.capitalize()}'s parasites</a> » ${_id.capitalize()}
        % elif individual:
            <a href="${h.url(h.url_for('species_index'))}">Home</a> » <a href="${h.url(h.url_for('individual_parasites', id=individual))}">${individual.upper()}'s parasites</a> » ${_id.capitalize()}
        % else:
            <a href="${h.url(h.url_for('species_index'))}">Home</a> » Parasite » ${_id.capitalize()}
        % endif 
        <hr />
    </div>

    <div class="column span-4">
        <div class="container" style="padding:10px;">

        </div>
    </div>


    <div class="fixed column" style="width:390px;">
        % if image_path:
            <img style="padding-left:10px;padding-bottom:10px;" src="${image_path}" width="390px" />
        % endif
        % if [i for i in common_names.values() if i is not None]:
            <fieldset><legend>Also known as</legend>
            <ul>
                    % for language, name in sorted(common_names.items()):
                        % if name:
                            <li> <span>${name}</span> (${language}) </li> 
                        % endif
                    % endfor
                </ul>
            </fieldset>
        % endif

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
            <ul>
            % for synonym in synonyms:
                <li> ${synonym.capitalize()} </li>
            % endfor
            </ul>
            </fieldset>
        % endif
        <fieldset><legend>Species infected</legend>
            <table>
            % for (host_id, pubref_id), rhp in sorted(rel_host_parasites.items()):
                <tr>
                    % if rhp['host']['internet_display']:
                        <td><a href="${h.url(h.url_for('species_show', id=rhp['host']['_id']))}">${rhp['host']['_id']}</a></td>
                        <td> <a href="${h.url(h.url_for('publication_show', id=rhp['pubref']['_id']))}">${h.author_date_from_citation(rhp['pubref']['reference'])}</a></td>
                    % endif
                </tr>
            % endfor
            </table>
        </fieldset>

    </div>

</div>
