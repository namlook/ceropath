<%inherit file="/root.mako" />

<div class="unit on-6 columns" style="width:1200px;">
    <h1><i>${_id.capitalize()}</i> <small>(${author}, ${date})</small></h1>

    <div style="padding-bottom:10px;">
    <a href="#">Home</a> » <a href="${h.url(h.url_for('species_index'))}">Species</a> » ${_id.capitalize()}
    </div>

    <!-- the tabs --> 
    <ul class="css-tabs"> 
        <li><a href="${h.url(h.url_for('species_show', id=_id))}">General Informations</a></li> 
        <li><a href="${h.url(h.url_for('species_measurements', id=_id))}">Species measurements</a></li> 
    </ul> 

    ${self.body()}

</div>
