    <style> 
    /* navigation */
    #nav {
        /*background:#ddd url(http://static.flowplayer.org/img/global/gradient/h300_reverse.png);*/
        border-bottom:1px solid #CCCCCC;
        height:156px;   
        width:1200;
    }
    
    #nav ul {   
        overflow-x:hidden;
        overflow-y:scroll;
        height:170px;
        width:1200px;
        margin:0 auto;  
    }
    
    #nav li {   
        border-right:1px solid #ddd;
        float:left;
        padding-left:1px;
        width:175px;
        list-style-type:none;
        text-align:center;
        margin-top:0px;
    }
    
    #nav a {
        color:#333333;
        display:block;
        padding:17px;
        position:relative;
        word-spacing:-2px;
        font-size:11px;     
        height:122px;
        text-decoration:none;
    }   
    
    #nav a.current {
        background:url(http://static.flowplayer.org/tools/img/tabs/down_large.jpg); 
    }
    
    #nav img {
        background-color:#fff;
        margin:3px 0 5px 27px;
        padding:4px;        
        display:block;
    }
    
    #nav strong {
        display:block;      
        font-size:13px;
    }
    
    /* panes */
    #panes {
        /*background:#fff url(http://static.flowplayer.org/img/global/gradient/h300_reverse.png) repeat scroll 0 0;*/
        width:1200;    
        height:255px;
        margin-bottom:-20px;
        padding-bottom:20px;
        
        /* must be relative so the individual panes can be absolutely positioned */
        position:relative;
    }
    
    /* crossfading effect needs absolute positioning from the elements */
    #panes div {
        display:none;       
        position:absolute;
        top:20px;
        left:20px;
        font-size:13px;
        color:#444; 
        width:1150px; 
        text-align:center;
    }
    
    #panes img {
        margin-right:20px;      
    }
    
    #panes p {
        font-size:13px;
        text-align:left;
    }
    
    #panes h3 {
        margin:0 0 -5px 0;
        font-size:22px;
        font-weight:normal;
    }
    
    .overlay {
        display:none;
        width:500px;
        padding:20px;
        background-color:#ddd;
    }
    </style> 

<!-- navigator --> 
<div id="nav"> 
    <ul> 
        % for file_name in files_list:
        <li> 
            <a href="#1"> 
                <img src="${data_path}/${file_name}" style="width:100px;" />        
                <strong>${files_list[file_name]}</strong> 
            </a> 
        </li> 
        % endfor
    </ul> 
</div> 
 
<!-- tab panes --> 
<div id="panes"> 
    % for file_name in sorted(files_list):
        <% print file_name %>
 
    <div>
        <a href="${data_path}/${file_name}" target="_blank">
            <img src="${data_path}/${file_name}" style="max-width:1150px;" />        
        </a>
        
        <h3>${files_list[file_name]}</h3> 
 
        <p> 
            ${legends}
        </p>
    </div> 
    % endfor
    
<br clear="all" /> 
 
<script> 
$(function() {
    
    
    $("#nav ul").tabs("#panes > div", {effect: 'fade', fadeOutSpeed: 400});
});
</script> 
 
