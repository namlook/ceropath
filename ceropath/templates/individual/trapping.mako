<%inherit file="/individual/show.mako" />

<script src="http://maps.google.com/maps?file=api&amp;v=2&amp;sensor=false&amp;key=ABQIAAAAiClKGB2tpgvoniYI51bh0hT2yXp_ZAY8_ufC3CFXhHIE1NvwkxRn7LzdwWy63Ckj31lQPzz-P6HPXA" type="text/javascript"></script>

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
    map.setCenter(point, 15);
    var marker = new GMarker(point);
    map.addOverlay(marker);
    GEvent.addListener(marker,'click', function(){
        marker.openInfoWindowHtml('<strong>${_id.upper()}</strong> (${species.capitalize()})<br />lat : ${latitude}  <br /> long : ${longitude}<br /><a href="#">view more</a>');
    });

    //map.addControl(new GLargeMapControl());
    //map.addControl(new GScaleControl());
    //map.addControl(new GMapTypeControl());
    map.addMapType(G_PHYSICAL_MAP);
    map.setMapType(G_HYBRID_MAP);
    drawCircle(map);
    map.setUIToDefault();
}

$('document').ready(function(){
    initialize();
    $("img[rel]").overlay({mask: '#789'});
});
$(window).unload(function() {
    GUnload();
});
</script>

<style> 
    /* some styling for triggers */
    #triggers {
        text-align:center;
    }
    
    #img {
        cursor:pointer;
        margin:0 5px;
        background-color:#fff;
        border:1px solid #ccc;
        padding:2px;
    
        -moz-border-radius:4px;
        -webkit-border-radius:4px;
        
    }
    
    
    
    /* styling for elements inside overlay */
    .details {
        position:absolute;
        top:15px;
        right:15px;
        font-size:11px;
        color:#fff;
        width:150px;
    }
    
    .details h3 {
        color:#aba;
        font-size:15px;
        margin:0 0 -10px 0;
    }

    /* the overlayed element */
    .simple_overlay {
        
        /* must be initially hidden */
        display:none;
        
        /* place overlay on top of other elements */
        z-index:10000;
        
        /* styling */
        background-color:#333;
        
        width:800px;    
        min-height:200px;
        border:1px solid #666;
        
        /* CSS3 styling for latest browsers */
        -moz-box-shadow:0 0 90px 5px #000;
        -webkit-box-shadow: 0 0 90px #000;  
    }

    /* close button positioned on upper right corner */
    .simple_overlay .close {
        background-image:url(/img/close.png);
        position:absolute;
        right:0px;
        top:0px;
        cursor:pointer;
        height:35px;
        width:35px;
}

</style> 
<div class="column span-4">
    <h2>Site in ${h.format_loc_name(province)} where ${_id.upper()} was trapped</h2>
    <div class="container" style="padding:10px">
        <div id="map_canvas" style="width: 780;height:600;"></div>
    </div>
</div>

<div class="fixed column">
    <fieldset><legend>Trapping Informations</legend>
        <table style="width:360px;">
            <tr><th>site id</th><td>${h.format_loc_name(_id.upper())}</td></tr>
            <tr><th>region</th><td>${h.format_loc_name(region)}</td></tr>
            <tr><th>country</th><td>${h.format_loc_name(country)}</td></tr>
            <tr><th>province</th><td>${h.format_loc_name(province)}</td></tr>
            <tr><th>district</th><td>${h.format_loc_name(district)}</td></tr>
            <tr><th>sub distict</th><td>${h.format_loc_name(sub_district)}</td></tr>
            <tr><th>village</th><td>${h.format_loc_name(village)}</td></tr>
            ##<tr><th>surrounding lanscape</th><td>${surrounding_landscape}</td></tr>
            <tr><th>house presence</th><td>${'yes' if house_presence else 'no'}</td></tr>
            <tr><th>house number</th><td>about ${house_number}</td></tr>
            <tr><th>house distance</th><td>about ${house_distance}m</td></tr>
            <tr><th>latitude</th><td>${latitude}</td></tr>
            <tr><th>longitude</th><td>${longitude}</td></tr>
        </table>
    </fieldset>
    % if image_paths:
        <fieldset><legend>Trapping Site Photos</legend>
            % for index, image_path in enumerate(image_paths):
                <div><img src="${image_path}" width="360px" rel="#${index}" /></div>
                <div class="simple_overlay" id="${index}"><img src="${image_path}" /></div>
            % endfor
        </fieldset>
    % endif
</div>
