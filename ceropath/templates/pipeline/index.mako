<%inherit file="/root.mako" />
<% import datetime %>

<style>
    .image img{
        position: relative;
        right:0px;
        width:70%;
    }
    .input{
        position: relative;
        bottom: -20px;
        right: -200px;
        padding-bottom:20px;
    }
    textarea{
        height: 350px;
    }
</style>
    <div class="input" style="float:left;">
    <fieldset>
        <legend>Choose the file containing a sequence (fasta format)...</legend>
        <form action="${h.url(h.url_for('pipeline_result'))}" method="post" enctype="multipart/form-data">
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
            <a href="#" id="show-example">paste an example</a>
            <form action="${h.url(h.url_for('pipeline_result'))}" method="post" enctype="multipart/form-data">
            <div id="example">>user1
CAAATCTACAATGTAATTGTCACAGCCCATGCATTCGTAATAATTTTCTTTATAGTTATGCCAATAATGATTGGTGGTTTCGGAAACTGATTAGTCCCCTTAATAATTGGAGCCCCTGATATAGCATTTCCACGAATAAATAATATAAGCTTTTGACTCCTTCCACCATCATTCCTTCTTCTGTTAGCATCTTCTATGGTAGAAGCCGGAGCAGGAACAGGATGAACAGTATACCCACCATTAGCTGGAAATTTAGCCCACGCTGGAGCATCAGTAGACCTAACCATTTTCTCCCTCCACCTGGCTGGGGTATCCTCTATTTTAGGGGCTATTAACTTTATTACTACTATTATTAATATGAAACCACCCGCTATAACTCTATGG
>user2
GGACAACCAGGTGCACTTCTAGGAGATGACCAAATTTATAATGTTATTGTAACTGCCCATGCATTCGTAATAATTTTTTTTATAGTTATACCAATAATAATTGGAGGCTTCGGAAACTGACTTGTACCACTAATAATTGGAGCCCCAGATATAGCATTTCCACGAATAAATAATATAAGCTTTTGACTACTTCCCCCATCTTTCCTCCTTCTTCTAGCATCATCTATAGTAGAAGCAGGAGCAGGAACGGGATGAACAGTTTACCCCCCTCTAGCTGGAAATTTAGCTCATGCAGGAGCATCAGTAGACCTAACAATTTTCTCCCTCCATTTAGCTGGTGTTTCATCTATTCTAGGTGCAATCAACTTTATTACTACAATTATTAACATAAAACCCCCAGCTATAACTCAATATCAAACCCCGCTATTTGTTTGATCAGTACTAATTACTGCCGTATTACTTTTACTATCCCTACCAGTTCTAGCTGCAGGAATTACTATACTGCTAACAGACCGTAACCTTAATACAACTTTCTTTG
>user3
GGACAGCCAGGCGCACTACTAGGAGATGACCAAATTTATAATGTTATTGTTACCGCCCATGCATTTGTTATAATCTTTTTTATAGTAATGCCAATAATAATCGGAGGTTTCGGAAACTGACTTGTACCACTAATAATTGGAGCCCCAGATATAGCATTCCCACGAATAAATAATATAAGTTTTTGACTACTTCCCCCATCATTTCTTCTCCTATTAGCATCATCAATAGTAGAAGCTGGGGCAGGAACAGGATGAACAGTCTACCCACCTCTAGCCGGAAATTTAGCCCATGCAGGAGCATCTGTAGATTTAACAATTTTTTCTCTACATTTAGCCGGTGTCTCATCTATTTTAGGTGCAATCAACTTTATTACAACAATTATTAATATAAAACCCCCAGCTATAACTCAGTATCAAACCCCACTATTTGTCTGATCCGTATTAATTACAGCTGTATTACTTTTATTATCACTGCCGGTATTAGCTGCAGGAATTACTATACTATTAACAGACCGAAATCTTAATACAACTTTCTTTG
            </div>

            <div>
            <textarea rows="10" cols="80" name="paste" id="sequence"></textarea><br />
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
            <input type="reset" />
            <input type="submit" />
            ##class="button" blockui="wait_progress" value="Upload & explore" />
            </div>
        </form>
        </fieldset>
    </div>

    <div class="image" style="float:right;">
        <img src="/img/cadre_blast.png" />
    </div>

<script>
$(document).ready(function(){
    $('#example').hide();
    $('.pipeline-infos').click(function(){
        var pipeline_name = $(this).parent().parent().find('.pipeline-selection :selected').text();
        $(this).attr('href', '/rdbsea/pipeline/infos/'+pipeline_name+'.txt');
    });
    $('#show-example').click(function(){
        $('#sequence').text($('#example').text());
    });
});
</script>
