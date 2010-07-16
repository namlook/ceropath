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

<h1> New pipeline </h1>

<form action="${h.url(h.url_for('pipeline_create'))}" method="post">
    <div><label>pipeline's name :</label> <input type="text" name="name" /></div>
    <ul id="programs" class="sortable" style="list-style-type: none;">
    </ul>
    <p><a href="#" id="add-prog">Add a program</a></p>
    <div>
    <input type="submit" value="save" />
    </div>
</form>

<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/jquery-ui.min.js"></script>
<script>
$(".sortable").sortable({ 
    connectWith: 'ul',
});
index = 0;
$('#add-prog').click(function(){
    index += 1;
    $('#programs').append('<li><fieldset style="background:#fff;"><legend><input type="text" name="'+index+'-name" /></legend> <div style="float:right;text-align:right;"><a href="#" class="liveremove">remove</a></div><div style="float:left;padding-right:50px"> <p> <label>cmd</label> <textarea name="'+index+'-cmd" style="width:800px;height:100px;"></textarea </p> <p> <label>output extension</label> <input type="text" name="'+index+'-output_ext" /> </p><p> <label>use stdin</label> <input type="checkbox" name="'+index+'-use_stdin" /> </p></div> </fieldset></li>' );
});
$('.liveremove').live('click', function(){
    $(this).parent().parent().parent().remove();
});


</script>


