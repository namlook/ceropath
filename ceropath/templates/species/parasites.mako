<%inherit file="/species/show.mako" />

<style>
td{
    padding-right:30px;
}
</style>

<div class="span-30" style="padding-top:10px;">
        <table>
        <tr>
            <th>Parasites</th>
            <th>Publications</th>
            <th>Phylum</th>
            <th>Class</th>
            <th>Order</th>
            <th>Family</th>
            <th>Genus</th>
        <tr>
        % for rhp_id, (rhp, host, pubref) in rel_host_parasites.iteritems():
            <%
                phylum = host['taxonomic_rank']['phylum']
                _class = host['taxonomic_rank']['class']
                order = host['taxonomic_rank']['order']
                family = host['taxonomic_rank']['family']
                genus = host['taxonomic_rank']['genus']
            %>
            <tr>
                <td><i><a href="${h.url(h.url_for('parasite_show', id=rhp['parasite']['$id'], species=_id))}">${rhp['parasite']['$id'].capitalize()}</i></a></td>
                <td><a href="${h.url(h.url_for('publication_show', id=pubref['_id']))}">${h.author_date_from_citation(pubref['reference'])}</a></td>
                <td>${phylum.capitalize() if phylum else "unknown"}</td>
                <td>${_class.capitalize() if _class else "unknown"}</td>
                <td>${order.capitalize() if order else "unknown"}</td>
                <td>${family.capitalize() if family else "unknown"}</td>
                <td>${genus.capitalize() if genus else "unknown"}</td>
            </tr>
        % endfor
    </table>
</div>


