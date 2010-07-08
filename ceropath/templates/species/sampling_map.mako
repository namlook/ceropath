<%inherit file="/species/show.mako" />
<%import math%>

<div class="span-23">
    <div id="map-wrapper"> 
        <div id="map" style="height:600px;"></div> 
    </div> 
</div>
<div class="span-7 last" style="height:600px;overflow-y:scroll;">
    <div id="sidebar">
        <ul id="sidebar-list">
     </div>  
</div>


<script src="http://maps.google.com/maps?file=api&amp;v=2&amp;sensor=false&amp;key=${api_key}" type="text/javascript"></script>
<script>
var markers = [
    % for _id in sorted(individuals):
        <% individual, site = individuals[_id] %>
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
            typo = individual['trapping_informations']['eco_typology']
            surrounding_landscape = site['surrounding_landscape']
        %>
        {
            'latitude': '${site['coord_wgs']['dll_lat'] or 0}',
            'longitude': '${site['coord_wgs']['dll_long'] or 0}',
            'individu': '${individual['_id'].upper()}',
            'description': 'Region: ${region}<br/>Country: ${country} <br/>Province: ${province} <br/>District: ${district} <br/>Sub-district: ${sub_district} <br/>Village: ${village} <br/>Origin How: ${origin} <br/>Accuracy: ${accuracy}m',
            'typo': '<ul><li>${typo['low']}</li><li>${typo['medium']}</li><li>${typo['high']}</li></ul>',
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
        listItem.id = pointData.individu;
        var listItemLink = listItem.appendChild(document.createElement('a'));
        listItemLink.href = "#";
        listItemLink.innerHTML = '<font color="#000000"><strong>' + pointData.individu + '</strong>';
        var listItemSpan = listItem.appendChild(document.createElement('span'));
        listItemSpan.innerHTML = '<br/><span>' + pointData.description + '</span></font>';
        
        <!-- Sur l'action du click, on va se pointer à la localisation du marker -->
        var focusPoint = function() 
        {
                marker.openInfoWindowHtml('<strong><a href="/individual/'+pointData.individu.toLowerCase()+'">'+pointData.individu + '</a></strong><br/><strong>Landscape at the sampling point:</strong>' + pointData.typo + '<strong>Surrounding Landscape:</strong><br/>' + pointData.surrounding+'<br/> <a href="#'+pointData.individu+'">set up to top of list</a>');
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
