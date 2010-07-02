
        <table>
            <tr><th>Parasites</th><th>Publications</th><tr>
            % for rhp_id, (rhp, pubref) in rel_host_parasites.iteritems():
                <tr>
                    <td><i><a href="${h.url(h.url_for('parasite_show', id=rhp['parasite']['$id'], **options))}">${rhp['parasite']['$id'].capitalize()}</i></a></td>
                    <td><a href="${h.url(h.url_for('publication_show', id=pubref['_id']))}">${h.author_date_from_citation(pubref['reference'])}</a></td>
                </tr>
            % endfor
        </table>

