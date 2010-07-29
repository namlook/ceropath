<%inherit file="/individual/show.mako" />

<style>
table.measurements td{
    border:1px solid #E6E6E6;
    padding:10px;
}
</style>

<div class="span-20">
    <table class="measurements">
        <tr><th></th>
        % for pub, origin in publications_list:
            % if pub is not None:
                <th>
                    Measurements in <a href="${h.url(h.url_for('publication_show', id=pub['_id']))}" title="${pub['reference']}">
                    ${h.author_date_from_citation(pub['reference'])}
                    </a>
                    for ${species.capitalize()} <small>(a)</small>
                 </th>
            % elif origin is None:
                <th>Ceropath measurements for ${species.capitalize()} <small>(a)</small></th>
            % else:
                <th>Measurements for ${_id.upper()} (${age})</th>
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
                                % if m.get('mean'):
                                    % if trait['measurement_accuracy']:
                                        ${round(float(m['mean']), trait['measurement_accuracy'])}
                                    % else:
                                        ${int(m['mean'])}
                                    % endif
                                % else:
                                    ø
                                % endif
                                +/-
                                % if m.get('sd'):
                                    % if trait['measurement_accuracy']:
                                        ${round(float(m['sd']), trait['measurement_accuracy'])}
                                    % else:
                                        ${int(m['sd'])}
                                    % endif
                                % else:
                                    ø
                                % endif
                                (${int(m['n'])})
                               <br />
                                % if m.get('min'):
                                    % if trait['measurement_accuracy']:
                                        ${round(float(m['min']), trait['measurement_accuracy'])}
                                    % else:
                                        ${int(m['min'])}
                                    % endif
                                % else:
                                    ø
                                % endif
                                -
                                % if m.get('max'):
                                    % if trait['measurement_accuracy']:
                                        ${round(float(m['max']), trait['measurement_accuracy'])}
                                    % else:
                                        ${int(m['max'])}
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


<div class="span-8 last">
    % if image_path:
        <fieldset>
        <a href="${image_path}" target="_blank"> <img style="padding-bottom:10px;" src="${image_path}" width="360px" /> </a>
        <p style="text-align:center;margin:0px;padding:0px;"><small>Click on the image to see skull measurments</small></p>
        </fieldset>
    % endif
    <fieldset><legend>General Informations</legend>
        <table style="width:360px">
            <tr><th>species</th><td><a href="${h.url(h.url_for('species_show', id=species))}">${species.capitalize()}</a></td></tr>
            <tr><th>sex</th><td>${sex}</td></tr>
            <tr><th>age</th><td>${age}</td></tr>
            <tr><th>dissection date</th><td>${dissection_date}</td></tr>
        </table>
    </fieldset>
    <fieldset style="width:360px;"><legend>Scientific fields</legend>
        ${h.ui.ModulesList(_id, root="individual")}
    </fieldset>
    <fieldset><legend>Trapping Informations</legend>
        <table>
            <tr><th>region</th><td>${region}</td></tr>
            <tr><th>country</th><td>${country}</td></tr>
            <tr><th>province</th><td>${province}</td></tr>
        </table>
        % if latitude and longitude:
            <div style="padding-top:10px">
                <div id="map_canvas" style="width:360px;height:400px;"></div>
            </div>
        % endif
    </fieldset>
    <fieldset><legend>Sequences produced by Ceropath</legend>
        <table style="width:360px">
            <tr><th>Name</th><th>Accession number</th><th>Download</th></tr>
            % for gene, seq in sequences.iteritems():
                % if seq['sequence']:
                    <tr><td>${gene.upper()}</td>
                        <td>
                        % if seq['accession_number']:
                            ${seq['accession_number'].upper()}
                        % else:
                            not registered
                        % endif
                        </td>
                        <td>
                        % if seq['internet_display']:
                            <button onclick="javascript:$(this).parent().find('.download-list').toggle();">download</button>
                            <ul class="download-list">
                                <li> <a href="${h.url(h.url_for('individual_sequence', id=_id, gene=gene))}">consensus sequence</a></li>
                                ${h.ui.ChromatogramList(individual_id=_id, gene=gene.lower())}
                            </ul>
                        % else:
                            private
                        % endif
                        </td>
                    </tr>
                % endif
            % endfor
        </table>
    </fieldset>
    <fieldset><legend>Physiologic features</legend>
        <table style="width:360px">
            % for feature in physiologic_features:
                <tr><th>${feature['type']}</th><td>${feature['value'] or 'unknown'}</td></tr>
            % endfor
        </table>
    </fieldset>
    <fieldset><legend>Genotypes</legend>
        <table style="width:360px">
            % for name, value in genotypes.iteritems():
                <tr><th>${name}</th><td>${value}</td></tr>
            % endfor
        </table>
    </fieldset>


</div>

<script src="http://maps.google.com/maps?file=api&amp;v=2&amp;sensor=false&amp;key=${api_key}" type="text/javascript"></script>

<script>
function drawCircle(map)
{
    var center = map.getCenter();
    var centerLong = center.lng();
    var centerLat = center.lat();
    var circleColor = "#000000";
    var circlecHeight = "1";
    var circlecAlpha = "1";
    var diskColor = "#d0c730";
    var diskAlpha = "0.1";
    var latConv = center.distanceFrom(new GLatLng(centerLat+0.1, centerLong))/100;
    var lngConv = center.distanceFrom(new GLatLng(centerLat, centerLong+0.1))/100;
    var circle_points = [];
    var step = parseInt(360/180)||10;
    var radius = Math.pow(10,${accuracy}) * 0.001;
    for(var i=0; i<=360; i+=step)
    {
        var pint = new GLatLng(centerLat + (radius/latConv * Math.cos(i * Math.PI/180)), centerLong + (radius/lngConv * Math.sin(i * Math.PI/180)));
        circle_points.push(pint);
    }
    circlePolygon = new GPolygon(circle_points, circleColor, circlecHeight, circlecAlpha, diskColor, diskAlpha);
    map.addOverlay(circlePolygon);
}

function initialize() {
    var map = new GMap2(document.getElementById("map_canvas"));
    var point = new GLatLng(${latitude}, ${longitude});
    map.setCenter(point, 4);
    var marker = new GMarker(point);
    map.addOverlay(marker);
    GEvent.addListener(marker,'click', function(){
        marker.openInfoWindowHtml('<strong>${_id.upper()}</strong> (${species.capitalize()})<br />lat : ${latitude}  <br /> long : ${longitude}<br /><a href="${h.url(h.url_for('individual_trapping', id=_id))}">view more</a>');
    });

    //map.addControl(new GLargeMapControl());
    //map.addControl(new GScaleControl());
    //map.addControl(new GMapTypeControl());
    map.addMapType(G_PHYSICAL_MAP);
    //map.setMapType(G_HYBRID_MAP);
    drawCircle(map);
}

$('document').ready(function(){
    initialize();
    $('.download-list').hide();
});
$(window).unload(function() {
    GUnload();
});
</script>


