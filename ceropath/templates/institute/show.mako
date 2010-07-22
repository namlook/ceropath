<%inherit file="/root.mako" />

<h1>${institute['_id']}</h1>

<h3>${institute['name']}</h3>

<table>
    <tr><th>phone</th><td>${institute['phone']}</td></tr>
    <tr><th>fax</th><td>${institute['fax']}</td></tr>
    <tr><th>road</th><td>${institute['road']}</td></tr>
    <tr><th>building</th><td>${institute['building']}</td></tr>
    <tr><th>city</th><td>${institute['city']}</td></tr>
    <tr><th>zip code</th><td>${institute['zip_code']}</td></tr>
    <tr><th>country</th><td>${institute['country']}</td></tr>
</table>

