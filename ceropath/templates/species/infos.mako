<%inherit file="/species/show.mako" />

<script type="text/javascript" src="/fancybox/jquery.fancybox-1.3.1.pack.js"></script>
<link rel="stylesheet" href="/fancybox/jquery.fancybox-1.3.1.css" type="text/css" media="screen" />

<div class="span-20">
    % if image_paths:
        <div class="span-7">
        <% i=0 %>
        % for image_path, photo_author in image_paths:
            % if i: 
                <% hidden = "hidden" %>
            % else:
                <% hidden = "" %>
            % endif
                <a id="image" rel="group" class="group ${hidden}" title="© ${_id.capitalize()} by ${photo_author}" href="${image_path}"><img align="righ" style="padding-bottom:10px;padding-top:10px;" src="${image_path}" width="250px" /></a>
            <% i+=1 %>
        % endfor
        </div>
    % endif

        <div class="span-13 last" style="text-align:right;">
        <h3>Common names:</h3>
            % for language, name in sorted(common_names.items()):
                % if name:
                    <span>${name}</span> (${language}) <br />
                % endif
            % endfor
        </div>
        <div class="span-20">
        % if not internet_display:
            <p style="color:red;">This species wasn't sampling by Ceropath project </p>
        % else:
            ${h.literal(h.markdownize(description))}
        % endif

        More information about ${_id.capitalize()} on the
        <a href="http://www.bucknell.edu/msw3/browse.asp?s=y&id=${id_msw3}" target='_blank'>
        Mammal Species of the World</a> or 
        <a href="http://www.iucnredlist.org/apps/redlist/details/${iucn_id}" target="_blank">IUCN</a>
        website.
        <br />
        <br />
        </div>
</div>

<div class="span-10 last">
    <%doc>
    % if image_paths:
        <fieldset class="span-10">
        <div id="images">
        <% i=0 %>
        % for image_path, photo_author in image_paths:
            % if i: 
                <% hidden = "hidden" %>
            % else:
                <% hidden = "" %>
            % endif
                <a id="image" rel="group" class="group ${hidden}" title="© ${_id.capitalize()} by ${photo_author}" href="${image_path}"><img style="padding-bottom:10px;" src="${image_path}" width="390px" /></a>
            <% i+=1 %>
        % endfor
        </div>
        </fieldset>
    % endif
    </%doc>
            <fieldset class="span-10"><legend>Taxonomic ranks</legend>
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

    <fieldset class="span-10"><legend>Scientific fields</legend>
        ${h.ui.ModulesList(_id, root="species")}
    </fieldset>

           % if citations:
            <fieldset class="span-10"><legend>Recorded in</legend>
                <table>
                % for cit in citations:
                    <tr>
                        <td>
                        <a href="${h.url(h.url_for('publication_show', id=cit['pubref']['_id']))}">
                            ${h.author_date_from_citation(cit['pubref']['reference'])}</a>
                        </td>
                        <td>as ${cit['name'].capitalize()}</td>
                    </tr>
                % endfor
                </table>
            </fieldset>
        % endif
 
    % if iucn_web_path:
        <fieldset class="span-10"><legend>IUCN range map</legend>
           <a href="${iucn_web_path}/${iucn_id}.png" target="_blank">
            <img src="${iucn_web_path}/${iucn_id}.png" width="385px" />
           </a>
        </fieldset>
    % endif

        % if synonyms:
            <fieldset class="span-10"><legend>Synonyms</legend>
                <table>
                % for syn in synonyms:
                    <tr>
                        <% name = syn['name'].split() %>
                        % if len(name) > 1:
                            <td>${" ".join(name).capitalize()}</td>
                        % else:
                            <td>${name[0]}</td>
                        % endif
                        <td>
                        <a href="${h.url(h.url_for('publication_show', id=syn['pubref']['_id']))}">
                            ${h.author_date_from_citation(syn['pubref']['reference'])}</a>
                        </td>
                    </tr>
                % endfor
                </table>
            </fieldset>
        % endif

</div>

<script>
$('document').ready(function(){
    $('.hidden').hide();
    $("a.group").fancybox({
        'titlePosition'  : 'over',
        'transitionIn'  :   'elastic',
        'transitionOut' :   'elastic',
        'speedIn'       :   600, 
        'speedOut'      :   200, 
        'overlayShow'   :   true,
    });
});
</script>
