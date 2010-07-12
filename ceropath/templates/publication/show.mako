<%inherit file="/root.mako" />

<% disp = h.author_date_from_citation(reference) %>

<div class="span-30" style="padding-bottom:10px;">
    <h1>${disp}</h1>
    <a href="${h.url(h.url_for('species_index'))}">Home</a> » Publications » ${disp}
    <hr />
</div>

<div class="span-20">
    ${reference}
</div>

<div class="span-10 last">
    <fieldset><legend>Informations</legend>
    <table>
        <tr> <th>ceropath id</th><td>${_id}</td> </tr>
        <tr> <th>source</th><td>${source}</td> </tr>
    </table>
    </fieldset>
    % if hosts_related:
        <fieldset><legend>Host related interesting Ceropath project</legend>
        <ul>
        % for species in hosts_related:
            <li><a href="${h.url(h.url_for('species_show', id=species))}">${species.capitalize()}</a></li>
        % endfor
        </ul>
        </fieldset>
    % endif
    % if parasites_related:
    <fieldset><legend>Parasites related interesting Ceropath project</legend>
        <ul>
        % for parasite in parasites_related:
            <li><a href="${h.url(h.url_for('parasite_show', id=parasite))}">${parasite.capitalize()}</a></li>
        % endfor
        </ul>
    </fieldset>
    % endif
    % if host_synonyms_related:
        <fieldset><legend>Host synonyms in this publication</legend>
        <ul>
        % for species, synonyms in sorted(host_synonyms_related.items()):
            <li><a href="${h.url(h.url_for('species_show', id=species))}">${species.capitalize()}</a> <button class="synonyms-more">names in reference</button>
            <ul class="synonyms">
            % for syn in synonyms:
                <% name = syn.split() %>
                % if len(name) > 1:
                    <li>${" ".join(name).capitalize()}</li>
                % else:
                    <li>${name[0]}</li>
                % endif
            % endfor
            </ul>
            </li>
        % endfor
        </ul>
        </fieldset>
    % endif
    % if parasite_synonyms_related:
        <fieldset><legend>Parasites synonyms in this publication</legend>
        <ul>
        % for parasite, synonyms in sorted(parasite_synonyms_related.items()):
            <li><a href="${h.url(h.url_for('parasite_show', id=parasite))}">${parasite.capitalize()}</a> <button class="synonyms-more">names in reference</button>
            <ul class="synonyms">
            % for syn in synonyms:
                <% name = syn.split() %>
                % if len(name) > 1:
                    <li>${" ".join(name).capitalize()}</li>
                % else:
                    <li>${name[0]}</li>
                % endif
            % endfor
            </ul>
            </li>
        % endfor
        </ul>
        </fieldset>
    % endif

</div>

<script>
$(document).ready(function(){
    $('.synonyms').hide();
    $('.synonyms-more').click(function(){
        $(this).parent().find('ul').toggle();
    });
});
</script>


