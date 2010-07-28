<%inherit file="/root.mako" />

<% disp = h.author_date_from_citation(reference) %>

<div class="span-30" style="padding-bottom:10px;">
    <h1>${disp}</h1>
    <a href="${h.url(h.url_for('species_index'))}">Home</a> » Publications » ${disp}
    <hr />
</div>

<%def name="display_related(related, type)">
    <ul>
    % for species, synonyms in sorted(related.items()):
        <li>
        % if type == "mammal":
            <a href="${h.url(h.url_for('species_show', id=species))}">${species.capitalize()}</a>
        % elif type == "parasite":
            <a href="${h.url(h.url_for('parasite_show', id=species))}">${species.capitalize()}</a>
        % endif
        % if synonyms:
            <button class="synonyms-more">names in reference</button>
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
        % endif
        </li>
    % endfor
    </ul>
</%def>

<div class="span-30">
    ${reference}
    <br />
    <br />
    <div class="span-13 colborder">
    <h3>Host related interesting Ceropath project</h3>
    % if hosts_related:
        ${display_related(hosts_related, type="mammal")}
    % else:
        not found
    % endif
    </div>
    <div class="span-14 last">
    <h3>Parasites related interesting Ceropath project</h3>
    % if parasites_related:
        ${display_related(parasites_related, type="parasite")}
    % else:
        not found
    % endif
    </div>
</div>

<script>
$(document).ready(function(){
    $('.synonyms').hide();
    $('.synonyms-more').click(function(){
        $(this).parent().find('ul').toggle();
    });
});
</script>


