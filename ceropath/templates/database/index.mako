<%inherit file="/root.mako" />

<div class="span-18 colborder">
<center>
    <p>Use this form to upload all json files</p>
    <form action="${h.url(h.url_for('database_load'))}" method="post" enctype="multipart/form-data">
        <input type="file" name="jsonzip" />
        <input type="submit" />
    </form>
</center>
</div>

<div class="span-10 last">
<p>
    Only those files are supported:
</p>
<ul>
    <li>publication.json</li>
    <li>institute.json</li>
    <li>responsible.json</li>
    <li>trait.json</li>
    <li>organism_classification.json</li>
    <li>species_measurement.json</li>
    <li>site.json</li>
    <li>individual.json</li>
    <li>gene.json</li>
    <li>primer.json</li>
    <li>sequence.json</li>
    <li>rel_host_parasite.json</li>
</ul>
</div>

