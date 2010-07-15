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
            <br/>
            <b>Filename:</b> <input type="file" name="file" class="button" /><br />
            <input type="reset" class="button" value="Reset" />
            <input type="submit" />
            ## class="button" blockui="wait_progress" value="Upload & explore" />
        </form>
    </fieldset>
    <br />
    <fieldset>
        <legend>... OR paste your sequence...</legend>
        <form action="${h.url(h.url_for('pipeline_phyloexplorer'))}" method="post" enctype="multipart/form-data">
            <textarea rows="10" cols="80" name="paste" value=""></textarea><br />

            ##<span class="example_button" id="nexus">nexus example </span> &nbsp
            ##<span class="example_button" id="newick"> newick example </span><br/><br/>
            <input type="button" class="button" value="Reset" id="badreset"/>
            <input type="submit" />
            ##class="button" blockui="wait_progress" value="Upload & explore" />
        </form>
        <div style="text-align:center;color:#FF9934;" >
            <span>© CBGP 2010
                <% date = datetime.date.today().year %>
                % if date != 2010:
                    - ${date}
                % endif
            </span>
        </div>
    </fieldset>
    </div>

    <div class="image" style="float:right;">
        <img src="/img/cadre_blast.png" />
    </div>
