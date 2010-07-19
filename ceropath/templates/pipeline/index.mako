<%inherit file="/root.mako" />
<% import datetime %>

<style>
    .image{
        position:relative;
        left:-200px;
    }
    .image img{
        width:70%;
    }
    .input{
        position: relative;
        bottom: -20px;
        right: -100px;
    }
    textarea{
        height: 350px;
    }
</style>
    <div class="input" style="float:left;">
    <fieldset>
        <legend>Choose the file containing a sequence (fasta format)...</legend>
        <form action="${h.url(h.url_for('pipeline_phyloexplorer'))}" method="post" enctype="multipart/form-data">
            <div><b>Filename:</b> <input type="file" name="file" class="button" /></div>
            <div>
                select a pipeline : 
                <select class="pipeline-selection" name="pipeline_id">
                    % for pipeline in pipelines:
                        <option>${pipeline['_id']}</option>
                    % endfor
                </select>
                <a href="#" class="pipeline-infos">more infos</a>
            </div>
            <div>
            <input type="reset" class="button" value="Reset" />
            <input type="submit" />
            ## class="button" blockui="wait_progress" value="Upload & explore" />
            </div>
        </form>
    </fieldset>
    <br />
    <fieldset>
        <legend>... OR paste your sequence...</legend>
        <form action="${h.url(h.url_for('pipeline_phyloexplorer'))}" method="post" enctype="multipart/form-data">
            <div>
            <textarea rows="10" cols="80" name="paste" value=""></textarea><br />
            </div>

            <div>
                select a pipeline :
                <select class="pipeline-selection" name="pipeline_id">
                    % for pipeline in pipelines:
                        <option>${pipeline['_id']}</option>
                    % endfor
                </select>
                <a href="#" class="pipeline-infos">more infos</a>
            </div>
            <div>
            <input type="button" class="button" value="Reset" id="badreset"/>
            <input type="submit" />
            ##class="button" blockui="wait_progress" value="Upload & explore" />
            <span style="text-align:center;color:#FF9934;" >© CBGP 2010
                <% date = datetime.date.today().year %>
                % if date != 2010:
                    - ${date}
                % endif
            </span>
            </div>
        </form>
        </fieldset>
    </div>

    <div class="image" style="float:right;">
        <img src="/img/cadre_blast.png" />
    </div>

<script>
$('.pipeline-infos').click(function(){
    var pipeline_name = $(this).parent().parent().find('.pipeline-selection :selected').text();
    $(this).attr('href', '/data/pipeline/'+pipeline_name+'.html');
});
</script>
