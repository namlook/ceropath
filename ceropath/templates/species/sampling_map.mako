<%inherit file="/species/show.mako" />
<%import math%>

<div class="unit on-4 columns" style="width:1200px;height:600px;">
    <div class="column span-3">
        <div id="map-wrapper"> 
            <div id="map" style="width:900px;height:600px;"></div> 
        </div> 
    </div> 
    <div class="container" style="height:600px;overflow-y:scroll;">
    <div class="fixed column">
        <div id="sidebar">
            <ul id="sidebar-list">
         </div>  
    </div>
    </div>
</div>


<script src="http://maps.google.com/maps?file=api&amp;v=2&amp;sensor=false&amp;key=ABQIAAAAiClKGB2tpgvoniYI51bh0hT2yXp_ZAY8_ufC3CFXhHIE1NvwkxRn7LzdwWy63Ckj31lQPzz-P6HPXA" type="text/javascript"></script>
<script>
var markers = [
    % for _id, (individual, site) in individuals.iteritems():
        % if site is not None and site['coord_wgs']['dll_lat'] and site['coord_wgs']['dll_long']:
        <%
            region = h.format_loc_name(site['region'])
            country = h.format_loc_name(site['country'])
            province = h.format_loc_name(site['province'])
            district = h.format_loc_name(site['district'])
            sub_district = h.format_loc_name(site['sub_district'])
            village = h.format_loc_name(site['village'])
            origin = individual['trapping_informations']['origin_how']
            accuracy = individual['trapping_informations']['trap_accuracy']
            if accuracy:
                accuracy = int(math.pow(10, accuracy))
            typo = site['eco_typology']['low']
            surrounding_landscape = site['surrounding_landscape']
        %>
        {
            'latitude': '${site['coord_wgs']['dll_lat'] or 0}',
            'longitude': '${site['coord_wgs']['dll_long'] or 0}',
            'individu': '${individual['_id'].upper()}',
            'description': 'Region: ${region}<br/>Country: ${country} <br/>Province: ${province} <br/>District: ${district} <br/>Sub-district: ${sub_district} <br/>Village: ${village} <br/>Origin How: ${origin} <br/>Accuracy: ${accuracy}m',
            'typo': '${typo}',
            'surrounding': '${surrounding_landscape}'
        },
        % endif
    % endfor
];

var map;
<!-- Localisation et Zoom de la localisation de la zone Cambodge / Thailande etc... -->
var startZoom = 6;
var centerlatitude = 16;
var centerlongitude = 103;
function initializePoint(pointData)
{
        <!-- On se localise à la latitude et la longitude du point pour y afficher le marker -->
        var point = new GLatLng(pointData.latitude, pointData.longitude);
        var marker = new GMarker(point);
        <!-- On crée la liste sur le volet droit on sera affiché tous les points et leur description -->
        var listItem = document.createElement('li');
        var listItemLink = listItem.appendChild(document.createElement('a'));
        listItemLink.href = "#";
        listItemLink.innerHTML = '<font color="#000000"><strong>' + pointData.individu + '</strong><br/><span>' + pointData.description + '</span></font>';
        
        <!-- Sur l'action du click, on va se pointer à la localisation du marker -->
        var focusPoint = function() 
        {
                marker.openInfoWindowHtml(pointData.individu + '<br/><strong>Landscape at the sampling point:</strong><br/>' + pointData.typo + '<br/><strong>Surrounding Landscape:</strong><br/>' + pointData.surrounding);
                map.panTo(point);
                return false;
        }
        GEvent.addListener(marker, 'click', focusPoint);
        listItemLink.onclick = focusPoint;
        document.getElementById('sidebar-list').appendChild(listItem);
        map.addOverlay(marker);
}
function windowHeight()
{
        if (self.innerHeight) return self.innerHeight;
        if (document.documentElement && document.documentElement.clientHeight) return y=document.documentElement.clientHeight;
        if (document.body) return document.body.clientHeight;
        return 0;
}
 
function handleResize()
{
        var height = windowHeight();
        document.getElementById('map').style.height = height+ 'px';
        document.getElementById('sidebar').style.height = height+ 'px';
}
function initialize() 
{
       if (GBrowserIsCompatible()) 
       {
        map = new GMap2(document.getElementById("map"));
        <!-- Type de carte : Hybrid (Le payasage et les routes en même temps, 'la plus complete') -->
        map.setMapType(G_HYBRID_MAP);
        <!-- Ajout des bouton de controle pour Zoomer, Se Deplacer etc... -->
        map.addControl(new GLargeMapControl());
        map.addControl(new GScaleControl());
        map.addControl(new GMapTypeControl());
        map.addMapType(G_PHYSICAL_MAP);
        map.setCenter(new GLatLng(centerlatitude, centerlongitude), startZoom);
        <!-- Pour tous les markers connues, on va les initialiser, et donc les afficher un par un sur la map ainsi que sur le volet sur le coté -->
        for (id in markers)
        {
                initializePoint(markers[id]);
        }
        //handleResize();
       }
}
$('document').ready(function(){
    initialize();
});
$(window).unload(function() {
    GUnload();
});
</script> 
