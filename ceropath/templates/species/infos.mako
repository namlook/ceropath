<%inherit file="/species/show.mako" />

<script type="text/javascript" src="/rdbsea/fancybox/jquery.fancybox-1.3.1.pack.js"></script>
<link rel="stylesheet" href="/rdbsea/fancybox/jquery.fancybox-1.3.1.css" type="text/css" media="screen" />

<style>
a img{
    border:0px solid;
}
</style>

<div class="span-20">
    <div class="span-7">
    &nbsp;
    % if image_paths:
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
    % endif
    </div>

    <div class="span-5 colborder" style="padding-top:20px;">
        <fieldset><legend><h3>Scientific fields</h3></legend>
            ${h.ui.ModulesList(_id, root="species")}
        </fieldset>
    </div>

        <div class="span-6 last" style="text-align:right;">
        <h3>Common names:</h3>
            % for language, name in sorted(common_names.items()):
                % if name:
                    <span>${name}</span> (${language}) <br />
                % endif
            % endfor
        </div>

        <div class="span-20">
        <br />
        % if not internet_display or not has_individuals:
            <p style="color:red;">This species wasn't sampled by Ceropath project </p>
        % else:
            ${h.literal(h.markdownize(description))}
        % endif

        More information about <i>${_id.capitalize()}</i> on the
        <a href="http://www.bucknell.edu/msw3/browse.asp?s=y&id=${id_msw3}" target='_blank'>
        Mammal Species of the World</a> or 
        <a href="http://www.iucnredlist.org/apps/redlist/details/${iucn_id}" target="_blank">IUCN</a>
        website.
        <br />
        <br />
        </div>
           % if citations:
           <div class="span-20">
            <fieldset class="span-10"><legend>Recorded in</legend>
                <table>
                % for author_ref, cit in citations:
                    <tr>
                        <td>
                        <a href="${h.url(h.url_for('publication_show', id=cit['pubref']['_id']))}">
                            ${author_ref}
                        </td>
                        <td>as ${cit['name'].capitalize()}</td>
                    </tr>
                % endfor
                </table>
            </fieldset>
            </div>
        % endif
 
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
            <fieldset class="span-9"><legend>Taxonomic ranks</legend>
            <table>
                <%ranks = ['kingdom', 'phylum', 'class', 'order', 'superfamily', 'family', 'subfamily', 'tribe', 'division', 'genus', 'subgenus']%>
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



    % if iucn_web_path and iucn_id:
        <fieldset class="span-9"><legend>IUCN range map</legend>
           <a href="${iucn_web_path}/${iucn_id}.png" target="_blank">
            <img src="${iucn_web_path}/${iucn_id}.png" width="350px" />
           </a>
        </fieldset>
    % endif

        % if synonyms:
            <fieldset class="span-9"><legend>Synonyms</legend>
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
