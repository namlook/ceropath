<%inherit file="/individual/show.mako" />

<style>
table.measurements td{
    border:1px solid #E6E6E6;
    padding:10px;
}
</style>

<div class="span-20">
    %if measurements:
        ${h.ui.Measurements(_id, publications_list, measures_infos, traits, full=False, species=species, age=age)}
    %else:
        no measurements found
    % endif
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
    $('.download-list').hide();
    initialize();
});
$(window).unload(function() {
    GUnload();
});
</script>


