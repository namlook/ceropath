<%inherit file="/root.mako" />

<h1>${_id.capitalize()}</h1>
<h4>(${author}, ${date})</h4>


<!-- the tabs --> 
<ul class="tabs"> 
    <li><a href="${h.url(h.url_for('species_infos', id=_id))}">General Informations</a></li> 
    <li><a href="${h.url(h.url_for('species_measurements', id=_id))}">Species measurements</a></li> 
</ul> 

<!-- tab "panes" --> 
<div class="panes"> 
    <div style="display:block"></div> 
</div>
<%doc>
    <!--- General Informations -->
    <div>
    </div> 
    <!--- Species measurements -->
    <div>
    </div> 
</div> 
</%doc>


<!-- This JavaScript snippet activates those tabs --> 
<script> 
// perform JavaScript after the document is scriptable.
$(function() {
    // setup ul.tabs to work as tabs for each div directly under div.panes
    $("ul.tabs").tabs("div.panes > div", {effect: 'ajax'});//, history: true});
});
</script> 
