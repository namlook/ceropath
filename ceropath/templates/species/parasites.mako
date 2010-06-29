<%inherit file="/root.mako" />

<style>
td {
    text-align:center;
}
</style>

<h1> Parasites found on ${species.capitalize()} </h1>

<div style="padding-bottom:10px;">
    <a href="#">Home</a> » <a href="${h.url(h.url_for('species_show', id=species))}">Species</a> » parasites
</div>

<div class="unit on-1 columns">
    <div class="column">
        <table>
            <tr><th>Parasites</th><th>Publications</th><tr>
            % for rhp in rel_host_parasite:
                <tr>
                    ##<td>${rhp['_id']} ${rhp['parasite']}</td>
                    ##<td>${rhp['pubref']}</td>
                    <td><a href="${h.url(h.url_for('parasite_show', id=rhp['parasite']['_id']))}">${rhp['parasite']['_id'].capitalize()}</a></td>
                    <% author, date = h.author_date_from_citation(rhp['pubref']['reference']) %>
                    <td>${author} ${"(%s)" % date if date else ""}</td>
                </tr>
            % endfor
        </table>
    </div>
</div>


