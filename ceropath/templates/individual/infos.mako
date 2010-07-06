<%inherit file="/individual/show.mako" />

<style>
table.measurements td{
    border:1px solid #E6E6E6;
    padding:10px;
}
</style>

<div class="column span-4">
    <div class="container" style="padding:10px;">

     <%
         theaders = [(_id, 'individual'), (species, 'species')]
         theaders.extend((i, 'pubref') for i in publications_list.keys())
     %>
    <table class="measurements">
        <tr><th></th>
        % for header in theaders:
            % if header[1] == 'pubref':
                ##<% author, date = h.author_date_from_citation(publications_list[header[0]]['reference']) %>
                <th>
                    Measurements in <a href="${h.url(h.url_for('publication_show', id=publications_list[header[0]]['_id']))}" title="${publications_list[header[0]]['reference']}">
                    ${h.author_date_from_citation(publications_list[header[0]]['reference'])}
                    </a>
                    for ${species.capitalize()} <small>(a)</small>
                 </th>
            % elif header[1] == 'species':
                <th>Ceropath measurements for ${header[0].capitalize()} <small>(a)</small></th>
            % else:
                <th>Measurements for ${header[0].upper()} (${age})</th>
            % endif
        % endfor
        </tr>
        <%
            # XXX skull -> head
            first_measures = ['Head & Body (mm)', 'Tail (mm)', 'Foot (mm)', 'Skull  (mm)', 'Ear (mm)', 'Weight (g)']
            last_measures = sorted(i.strip() for i in measures_infos if i not in first_measures)
        %>
        % for trait in first_measures + last_measures:
            <% measure = measures_infos[trait] %>
            <tr><th>${trait}</th>
                % for publication_id in theaders:
                    <%
                        publication_id = publication_id[0]
                        m = measure.get(publication_id)
                        if isinstance(m, dict):
                            if isinstance(m['n'], basestring):
                                m['n'] = int(float(m['n'].replace(',', '.'))) if m['n'] else 0
                            # measure shoud match the round of the measure. The
                            # measure of the individu is taken as root_measure
                            root_measure =  measures_infos[trait].get(_id)
                            if m['mean'] is not None and root_measure is not None:
                                if isinstance(m['mean'], unicode):
                                    m['mean'] = float(m['mean'].replace(',', '.'))
                                if ',' not in root_measure:
                                    m['mean'] = int(m['mean'])
                                else:
                                    splited_root = root_measure.split(',')
                                    if len(splited_root) < 2:
                                        round_number = 0
                                    else:
                                        round_number = len(splited_root[1])
                                    m['mean'] = round(m['mean'], round_number)
                    %>
                    <td>
                        <center>
                        % if isinstance(m, dict):
                            % if m['n']:
                               ${m['mean'] or 0} +/- ${m['sd'] or 'NAN'} (${m['n']})
                               <br />
                               ${m['min'] or 0} - ${m['max'] or 0}
                            % else:
                                ø
                            % endif
                        % else:
                            ${m or u'ø'}
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
</div>


<div class="fixed column">
    % if image_path:
        <a href="${image_path}" target="_blank"> <img style="padding-left:10px;padding-bottom:10px;" src="${image_path}" width="360px" /> </a>
        <p style="text-align:center;margin:0px;padding:0px;"><small>Click on the image to see skull measurments</small></p>
    % endif
    <fieldset><legend>General Informations</legend>
        <table style="width:360px">
            <tr><th>species</th><td><a href="${h.url(h.url_for('species_show', id=species))}">${species.capitalize()}</a></td></tr>
            <tr><th>sex</th><td>${sex}</td></tr>
            <tr><th>age</th><td>${age}</td></tr>
            <tr><th>dissection date</th><td>${dissection_date}</td></tr>
        </table>
    </fieldset>
    <fieldset><legend>Scientific fields</legend>
        ${h.ui.ModulesList(_id, root="individual")}
    </fieldset>
    <fieldset><legend>Trapping Informations</legend>
        <table style="width:360px">
            <tr><th>country</th><td>${h.format_loc_name(country)}</td></tr>
            <tr><th>province</th><td>${h.format_loc_name(province)}</td></tr>
            <tr><th>region</th><td>${h.format_loc_name(region)}</td></tr>
        </table>
        % if latitude and longitude:
            <div style="padding-top:10px">
                <div id="map_canvas" style="width:360px;height:400px;"></div>
            </div>
        % endif
    </fieldset>
    <fieldset><legend>Sequences produced by Ceropath</legend>
        <table style="width:360px">
            % for gene, seq in sequences.iteritems():
                <%
                    seq_disp = 'No'
                    if seq['sequence']:
                        seq_disp = 'Yes'
                %>
                <tr><th>${gene.upper()}</th>
                    <td>
                    ${seq_disp}
                    % if seq['internet_display']:
                        <button onclick="javascript:$(this).parent().find('.download-list').toggle();">download</button>
                        <ul class="download-list" style="list-style:none;">
                            <li> <a href="${h.url(h.url_for('individual_sequence', id=_id, gene=gene))}">consensus sequence</a></li>
                            ${h.ui.ChromatogramList(individual_id=_id, gene=gene.lower())}
                        </ul>
                    % endif
                    </td>
                </tr>
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


