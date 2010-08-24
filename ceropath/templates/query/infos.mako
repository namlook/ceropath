<%inherit file="/root.mako" />

<div class="span-30">
    <div>
        <a href="${h.url(h.url_for('query_index'))}">back</a>
    </div>
    ${h.literal(h.markdownize(content))}
</div>

