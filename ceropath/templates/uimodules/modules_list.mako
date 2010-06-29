
    <ul>
        % for module in modules_list:
            <li><a href="${h.url(h.url_for('%s_module' % root, id=_id, name=module))}">${module}</a></li>
        % endfor
    </ul>

