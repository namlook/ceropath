<%inherit file="/root.mako" />

<script type="text/javascript" language="javascript">
<!--
// Email obfuscator script 2.1 by Tim Williams, University of Arizona
// Random encryption key feature by Andrew Moulden, Site Engineering Ltd
// This code is freeware provided these four comment lines remain intact
// A wizard to generate this code is at http://www.jottings.com/obfuscator/
$(document).ready(function(){
  coded = "C7eu7.2werXK@UX8x-2wX6Vp.He"
  key = "1kGCJD93WHUcvtpdohgbZemyqT8YRaS4nzP5FMsx6VKwfuNQ72OABIl0rELXji"
  shift=coded.length
  link=""
  for (i=0; i<coded.length; i++) {
    if (key.indexOf(coded.charAt(i))==-1) {
      ltr = coded.charAt(i)
      link += (ltr)
    }
    else {     
      ltr = (key.indexOf(coded.charAt(i))-shift+key.length) % key.length
      link += (key.charAt(ltr))
    }
  }
  $('#email-serge').attr('href', 'mailto:'+link);
//document.write("<a href='mailto:"+link+"'>Serge Morand</a>")
});

//-->
</script><noscript>Sorry, you need Javascript on to contact Serge Morand.</noscript>

<center>
<h1 style="color:red">RESTRICTED AREA</h1>
<p>You are not allowed to perform this action. Please log in before continue.</p>
<p>Please, contact <a id="email-serge" href="">Serge Morand</a> for more information</p>

<form action="${h.url(h.url_for('login_submit'))}" method="post">
    <table>
    <tr><th>user name</th><td><input type="text" name="username" /></td></tr>
    <tr><th>password</th><td><input type="password" name="password" /></td></tr>
    <tr><td></td><td><input type="submit" value="log in" /></td></tr>
    </table>
</form>
</center>
