<%inherit file="/species/show.mako" />

<style>
td{
    padding-right:30px;
}
</style>

<div class="span-30" style="padding-top:10px;">
        <table>
        <tr>
            <th>Phylum</th>
            <th>Class</th>
            <th>Order</th>
            <th>Family</th>
            <th>Genus</th>
            <th>Parasites</th>
            <th>Publications</th>
            <th>Origin</th>
        <tr>
        % for rhp_id, (rhp, parasite, pubref) in rel_host_parasites.iteritems():
            <%
                phylum = parasite['taxonomic_rank']['phylum']
                _class = parasite['taxonomic_rank']['class']
                order = parasite['taxonomic_rank']['order']
                family = parasite['taxonomic_rank']['family']
                genus = parasite['taxonomic_rank']['genus']
            %>
            <tr>
                <td>${phylum.capitalize() if phylum else "unknown"}</td>
                <td>${_class.capitalize() if _class else "unknown"}</td>
                <td>${order.capitalize() if order else "unknown"}</td>
                <td>${family.capitalize() if family else "unknown"}</td>
                <td>${genus.capitalize() if genus else "unknown"}</td>
                <td><i><a href="${h.url(h.url_for('parasite_show', id=rhp['parasite']['$id'], species=_id))}">${rhp['parasite']['$id'].capitalize()}</a></i></td>
                <td><a href="${h.url(h.url_for('publication_show', id=pubref['_id']))}">${h.author_date_from_citation(pubref['reference'])}</a></td>
                <td>${rhp['country']}</td>
            </tr>
        % endfor
    </table>
</div>


