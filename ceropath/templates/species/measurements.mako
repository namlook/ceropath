<%inherit file="/species/show.mako" />

<script type="text/javascript" src="/fancybox/jquery.fancybox-1.3.1.pack.js"></script>
<link rel="stylesheet" href="/fancybox/jquery.fancybox-1.3.1.css" type="text/css" media="screen" />

<div class="span-30 alt">
    <h2>CERoPath species measurements compare with literature data</h2>
</div>

<div class="span-23">
    <table class="measurements">
        <tr><th></th>
        % for pub, origin, species_article_name in publications_list:
            % if pub is not None:
                <th style="width:250px;">
                    Measurements in <a href="${h.url(h.url_for('publication_show', id=pub['_id']))}" title="${pub['reference']}">
                    ${h.author_date_from_citation(pub['reference'])}
                    </a>
                    for ${species_article_name.capitalize()} in ${origin} <small>(a)</small>
                 </th>
            % else:
                <th style="width:250px;">
                    Ceropath Measurements for ${_id.capitalize()} <small>(a)</small>
                </th>
            % endif
        % endfor
        </tr>
        <%
            traits_list = sorted(traits)
            traits_list.insert(2, '0')
            traits['0'] = {u'remark': None, u'_id': u'0', u'measurement_accuracy': 0, u'name': "Tail / Head & Body (%)"}
        %>
        % for trait_id in traits_list:
            <%
                trait = traits[trait_id]
                measure = measures_infos.get(trait['name'])
                if not measure:
                    continue
            %>
            <tr><th>${trait['name']}</th>
                % for key in publications_list:
                    <%
                        m = measure.get(key)
                        if isinstance(m, dict):
                            if isinstance(m['n'], basestring):
                                if m['n']:
                                    m['n'] = int(float(m['n'].replace(',', '.')))
                                else:
                                    m['n'] = 0
                    %>
                    <td>
                        <center>
                        % if m and isinstance(m, dict):
                            % if m.get('n'):
                                % if m['mean']:
                                    % if trait['measurement_accuracy']:
                                        ${round(float(m['mean']), trait['measurement_accuracy'])}
                                    % else:
                                        ${int(round(float(m['mean']), trait['measurement_accuracy']))}
                                    % endif
                                % else:
                                    ø
                                % endif
                                +/-
                                % if m.get('sd'):
                                    ${round(float(m['sd']), 2)}
                                % else:
                                    ø
                                % endif
                                (${int(m['n'])})
                               <br />
                                % if m.get('min'):
                                    % if trait['measurement_accuracy']:
                                        ${round(float(m['min']), trait['measurement_accuracy'])}
                                    % else:
                                        ${int(round(float(m['min']), trait['measurement_accuracy']))}
                                    % endif
                                % else:
                                    ø
                                % endif
                                -
                                % if m.get('max'):
                                    % if trait['measurement_accuracy']:
                                        ${round(float(m['max']), trait['measurement_accuracy'])}
                                    % else:
                                        ${int(round(float(m['max']), trait['measurement_accuracy']))}
                                    % endif
                                % else:
                                    ø
                                % endif
                            % else:
                                ø
                            % endif
                        % elif m:
                            ${m}
                        % else:
                            ø
                        % endif
                        </center>
                    </td>
                % endfor
            </tr>
        % endfor
    </table>
    <p>
    (a) The mean plus or minus one standard deviation, number of specimens in parentheses, and observed range are listed for each measurement.
    </p>
</div>

<div class="span-7 last">
&nbsp;
% if image_paths:
    % for image_path in image_paths:
        <div>
            <a class="image" href="${image_path}"><img align="righ" style="padding-bottom:10px;padding-top:10px;" src="${image_path}" width="250px" /></a>
        </div>
    % endfor
% endif
</div>

<script>
$('document').ready(function(){
    $("a.image").fancybox({
        'titlePosition'  : 'over',
        'transitionIn'  :   'elastic',
        'transitionOut' :   'elastic',
        'speedIn'       :   600, 
        'speedOut'      :   200, 
        'overlayShow'   :   true,
    });
});
</script>
