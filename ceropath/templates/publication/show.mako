<%inherit file="/root.mako" />

<% disp = h.author_date_from_citation(reference) %>
<h1>${disp}</h1>

<script>
$(document).ready(function(){
    $('.synonyms').hide();
    $('.synonyms-more').click(function(){
        $(this).parent().find('ul').toggle();
    });
});
</script>
<div class="unit on-6 columns" style="width:1200px;">

    <div style="padding-bottom:10px;">
        <a href="#">Home</a> » Publications » ${disp}
        <hr />
    </div>

    <div class="column span-4">
        <div class="container" style="padding:10px;">
            ${reference}
        </div>
    </div>

    <div class="fixed column" style="width:390px;">
        <fieldset><legend>Informations</legend>
        <table>
            <tr> <th>ceropath id</th><td>${_id}</td> </tr>
            <tr> <th>source</th><td>${source}</td> </tr>
        </table>
        </fieldset>
        % if hosts_related:
            <fieldset><legend>Hosts related</legend>
            <ul>
            % for species in hosts_related:
                <li><a href="${h.url(h.url_for('species_show', id=species))}">${species.capitalize()}</a></li>
            % endfor
            </ul>
            </fieldset>
        % endif
        % if parasites_related:
        <fieldset><legend>Parasites related</legend>
            <ul>
            % for parasite in parasites_related:
                <li><a href="${h.url(h.url_for('parasite_show', id=parasite))}">${parasite.capitalize()}</a></li>
            % endfor
            </ul>
        </fieldset>
        % endif
        % if synonyms_related:
            <fieldset><legend>Names used in the publication for :</legend>
            <ul>
            % for species, synonyms in synonyms_related.iteritems():
                <li><a href="${h.url(h.url_for('species_show', id=species))}">${species.capitalize()}</a> <button class="synonyms-more">show</button>
                <ul class="synonyms">
                % for syn in synonyms:
                    <li>${syn}</li>
                % endfor
                </ul>
                </li>
            % endfor
            </ul>
            </fieldset>
        % endif
    </div>
</div>
