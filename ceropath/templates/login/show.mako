<%inherit file="/root.mako" />

<center>
<h1 style="color:red">RESTRICTED AREA</h1>
<p>You are not allowed to perform this action. Please log in before continue.</p>
<p>Please, contact <a href="mailto:morand@isem.univ-montp2.fr">morand@isem.univ-montp2.fr</a> for more information</p>

<form action="${h.url(h.url_for('login_submit'))}" method="post">
    <table>
    <tr><th>user name</th><td><input type="text" name="username" /></td></tr>
    <tr><th>password</th><td><input type="password" name="password" /></td></tr>
    <tr><td></td><td><input type="submit" value="log in" /></td></tr>
    </table>
</form>
</center>
