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

<h1> Pipeline configuration </h1>

<form action="${h.url(h.url_for('pipeline_update_config'))}" method="post">
    <ul id="programs" class="sortable" style="list-style-type: none;">
    % for no, program in enumerate(programs):
        <li>
        <fieldset style="background:#fff;"><legend>${program['name']}</legend>
            <div style="float:right;text-align:right;"><a href="#" class="liveremove">remove</a></div>
            <div style="float:left;padding-right:50px">
                <p>
                    <label>shell</label>
                    <input type="checkbox" name="${no}-shell" ${'required="required"' if program['shell'] else ''} />
                </p>
                <p>
                    <label>path</label>
                    <input type="text" name="${no}-path" value="${program['path']}" />
                </p>
                <p>
                    <label>name</label>
                    <input type="text" name="${no}-name" value="${program['name']}" />
                </p>
                <p>
                    <label>input</label>
                    <input type="text" name="${no}-input" value="${program['input']}" />
                </p>
                <p>
                    <label>output</label>
                    <input type="text" name="${no}-ouput" value="${program['output']}" />
                </p>
                <p>
                    <label>options</label>
                    <input type="text" name="${no}-options" value="${program['options']}" />
                </p>
            </div>
        </fieldset>
        </li>
    % endfor
    </ul>
    <p><a href="#" id="add-prog">Add a program</a></p>
    <div>
    <input type="submit" />
    </div>
</form>

<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/jquery-ui.min.js"></script>
<script>
$(".sortable").sortable({ 
    connectWith: 'ul',
});
index = ${no};
$('#add-prog').click(function(){
    index += 1;
    $('#programs').append('<li><fieldset style="background:#fff;"><legend>new program</legend> <div style="float:right;text-align:right;"><a href="#" class="liveremove">remove</a></div><div style="float:left;padding-right:50px"><p> <label>shell</label> <input type="checkbox" name="'+index+'-shell" /> </p> <p> <label>path</label> <input type="text" name="'+index+'-path" /> </p> <p> <label>name</label> <input type="text" name="'+index+'-name" /> </p> <p> <label>input</label> <input type="text" name="'+index+'-input" /> </p> <p> <label>output</label> <input type="text" name="'+index+'-ouput" /> </p> <p> <label>options</label> <input type="text" name="'+index+'-options" /> </p></div> </fieldset></li>' );
});
$('.liveremove').live('click', function(){
    $(this).parent().parent().parent().remove();
});


</script>


