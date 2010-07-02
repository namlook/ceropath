<html>
<head>
    ##<link rel="stylesheet" type="text/css" href="/css/tabs.css" /> 
    <link rel="stylesheet" type="text/css" href="/css/tabs-no-images.css" /> 
    ##<link rel="stylesheet" href="/css/blueprint/screen.css" type="text/css" media="screen, projection">
    <link rel="stylesheet" href="/css/elastic.css" />
    ##<script src="http://flowplayer.org/tools/download/combine/1.2.3/jquery.tools.min.js?select=full&debug=true"></script>
    <script src="http://cdn.jquerytools.org/1.2.3/jquery.tools.min.js"></script>
    <script type="text/javascript" src="/js/elastic.js" charset="utf-8"></script> 
    <style> 
        /* tab pane styling */
        .panes div {
            display:none;       
            padding:15px 10px;
            border-top:0;
            height:100px;
            font-size:14px;
            background-color:#fff;
        }
        table th{
            background-color: #FD9834;
        }
    </style> 
</head>
<body>
    <div class="unit on-1 columns">
        <div class="column">
            <a href="${h.url(h.url_for('species_index'))}"><img src="/img/header.jpg" width="1200" alt="Home" /></a>
        </div>
        ${next.body()}
    </div>
</body>
</html>
