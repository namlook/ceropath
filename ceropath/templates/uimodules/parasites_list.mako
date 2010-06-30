
        <table>
            <tr><th>Parasites</th><th>Publications</th><tr>
            % for rhp in rel_host_parasites:
                <tr>
                    <td><a href="${h.url(h.url_for('parasite_show', id=rhp['parasite']['_id'], **options))}">${rhp['parasite']['_id'].capitalize()}</a></td>
                    <td>${h.author_date_from_citation(rhp['pubref']['reference'])}</td>
                </tr>
            % endfor
        </table>

