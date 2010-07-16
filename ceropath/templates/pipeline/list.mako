<%inherit file="/root.mako" />

<style>
fieldset {
    border:1px dashed #CCC;
    padding:10px;
}
legend {
    font-family:Arial, Helvetica, sans-serif;
    font-size: 90%;
    letter-spacing: -1px;
    font-weight: bold;
    line-height: 1.1;
    color:#fff;
    background: #666;
    border: 1px solid #333;
    padding: 2px 6px;
}
h1 {
    font-family:Arial, Helvetica, sans-serif;
    font-size: 175%;
    letter-spacing: -1px;
    font-weight: normal;
    line-height: 1.1;
    color:#333;
}
label {
    float:left; /* Take out of flow so the input starts at the same height */
    width:10em; /* Set a width so the inputs line up */
}

</style>

<h1> Pipelines configurations </h1>

<a href="${h.url(h.url_for('pipeline_new'))}">new pipeline</a>

<ul>
% for pipeline_id in pipelines:
    <li><a href="${h.url(h.url_for('pipeline_edit', id=pipeline_id))}">${pipeline_id}</a></li>
% endfor
</ul>

