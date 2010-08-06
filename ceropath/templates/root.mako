<html>
<head>
    <title>${title} | CERoPath - Barcoding Rodent South East Asia</title>
    <link rel="stylesheet" type="text/css" href="/css/tabs-no-images.css" /> 
    <link rel="stylesheet" href="/css/blueprint.1200.compressed.css" type="text/css" media="screen, projection">
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
    <script src="http://cdn.jquerytools.org/1.2.3/jquery.tools.min.js"></script>
    <link rel="stylesheet" href="/css/demo_table.css" />
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
            background-color: #D8EAA8;
        }
        img {
           border: none;
        }
        /*------------------------------------------*/
        /*                   PIED PAGE              */
        /*------------------------------------------*/
        #footer-text{
            position: relative;
            top: -44px;
            left:300px;
            color: #fff;
        }
        #footer-text p {
            font-family:Verdana, Arial, Helvetica, sans-serif;
            padding-top:15px;
            font-weight:bold;
            background:none;
            color: #fff;
        }
        #footer-text a {
            text-decoration:none;
            color:#fff;
        }
        #footer-text a:hover {
            text-decoration:underline;
        }
    </style> 
</head>
<body>
    <div class="container">
        <div class="span-30" style="text-align:right;">
            <a href="${h.url(h.url_for('species_index'))}"><img  src="/img/header-final.jpg" width="100%" alt="Home" /></a>
            <img src="/img/border-top.jpg" />
        </div>
        <div class="flash-message">
            <%
                message = h.failure_flash.pop_messages()
                flash_color = "red"
                if not message:
                    message = h.success_flash.pop_messages()
                    flash_color = "green"
            %>
            % if message:
                <div style="text-decoration:bold;color:${flash_color}">${message[0]}</div>
            % endif
        </div>
        ${next.body()}
        ${self.footer()}
    </div>
</body>
</html>
<%def name="footer()">
    <div id="baspage">
        <img src="/img/bg_piedPage.png" />
         <p id="footer-text">© CBGP/ISEM 2010
            <% import datetime %>
            <% date = datetime.date.today().year %>
            % if date != 2010:
                - ${date}
            % endif
         - All rights reserved - <a href="/disclaimer_stating" target="_self">Disclaimer stating</a> -<a href="/disclaimer_stating/contact_us" target="_self"> Contact</a></p>
    </div>
</%def>
