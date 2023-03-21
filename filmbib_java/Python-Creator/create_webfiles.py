import csv
import datetime

# Create a sorted Database (list)
# ========================
database_raw = []
with open('../database_export.csv', 'r') as database_file:
    reader = csv.reader(database_file, delimiter=';')
    for row in reader:
        database_raw.append(list(row))
database_file.close()
database = sorted(database_raw, key=lambda x: [x[0].lower().replace("ö", "o").replace("ä", "a").replace("ü", "u"), x[1].lower().replace("ö", "o").replace("ä", "a").replace("ü", "u")])

# Create index.html
# =================

get_date = datetime.datetime.now()
updated = get_date.strftime("%d.%m.%Y")

with open('../index.html', 'w') as new_empty_index:
    pass
new_empty_index.close()

with open('../index.html', 'a') as index_file:
    start_index = "<!DOCTYPE HTML><html><head><title>Filmbibliothek</title><meta charset='utf-8' /><meta name='viewport' content='width=device-width, initial-scale=1, user-scalable=no' /><link rel='stylesheet' href='assets/css/main.css' /><noscript><link rel='stylesheet' href='assets/css/noscript.css' /></noscript></head><body class='is-preload'><div id='wrapper' class='fade-in'><div id='intro'><h1>Die Film<br />bibliothek</h1><ul class='actions'><li><a href='#header' class='button icon solid solo fa-arrow-down scrolly'>Continue</a></li></ul></div><header id='header'><a href='index.html' class='logo'>Filmbibliothek</a></header><nav id='nav'><ul class='links'><li class='active'><a href='#'>Filme</a></li><li><a href='./suche_java.html'>Suchen</a></li></ul></nav><div id='main'><section class='post'><header class='major'><span class='date'>##date##</span><h1>Die Filme</h1><p>Nutzen Sie bitte die Suchfunktion im Menü.</p></header><div class='table-wrapper'><table><thead><tr><th>Titel</th><th>Info</th><th>Nr.</th></tr></thead><tbody>"
    end_index = "</tbody></table></div><footer id='footer'></footer><div id='copyright'><ul><!---<li>&copy; Untitled</li>--><li>Design: <a href=''>HTML5 UP</a></li></ul></div></div><script src='assets/js/jquery.min.js'></script><script src='assets/js/jquery.scrollex.min.js'></script><script src='assets/js/jquery.scrolly.min.js'></script><script src='assets/js/browser.min.js'></script><script src='assets/js/breakpoints.min.js'></script><script src='assets/js/util.js'></script><script src='assets/js/main.js'></script></body></html"
    index_file.write(start_index.replace("##date##", str(updated)))
    for entry in database:
        index_file.write("<tr><td>" + entry[0] + "</td><td>" + entry[1] + "</td><td>" + entry[2].replace(' ', '&nbsp;') + "</td></tr>")
    index_file.write(end_index)
index_file.close()


# Create

with open('../suche_java.html', 'w') as new_empty_java:
    pass
new_empty_java.close()

with open('../suche_java.html', 'a') as java_file:
    start_java = "<!DOCTYPE HTML><html>	<head>		<title>Filmbibliothek</title>		<meta charset='utf-8' />		<meta name='viewport' content='width=device-width, initial-scale=1, user-scalable=no' />		<link rel='stylesheet' href='assets/css/main.css' />		<noscript><link rel='stylesheet' href='assets/css/noscript.css' /></noscript>	</head>	<body class='is-preload'>		<!-- Wrapper -->			<div id='wrapper' class='fade-in'>				<!-- Intro -->					<div id='intro'>						<h1>Die Film<br />bibliothek</h1>						<ul class='actions'>							<li><a href='#header' class='button icon solid solo fa-arrow-down scrolly'>Continue</a></li>						</ul>					</div>				<!-- Header -->					<header id='header'>						<a href='index.html' class='logo'>Filmbibliothek</a>					</header>				<!-- Nav -->					<!-- Nav -->					<nav id='nav'>						<ul class='links'>							<li><a href='./index.html'>Filme</a></li>							<li class='active'><a href='#'>Suchen</a></li><!---							<li><a href='elements.html'>Elements Reference</a></li>-->						</ul>					</nav>				<!-- Main -->					<div id='main'>						<!-- Post -->							<section class='post'>								<header class='major'>									<span class='date'>##date##</span>									<h1>Suchen &amp; Finden</h1>								</header><section><label id='aufforderung' for='name'>Suchbegriff eingeben</label><input type='text' id='search-input' placeholder=''></input> <br><button id='searchbutton' onclick='search()'>Suche starten</button><br><br><br></section>										<!-- Results Table --><div class='table-wrapper'>	<table>		<thead>			<tr>				<th>Titel</th><th>Info</th><th>Nr.</th>			</tr>		</thead>		<tbody id='results'>		</tbody>	</table>"
    end_java = ''

    java_file.write(start_java.replace("##date##", str(updated)))
    java_file.write("<script>\nvar all_films = [\n")

    for entry in database:
        java_file.write("{title: '" + entry[0].replace("'", "&apos;") + "', info: '" + entry[1].replace("'", "&apos;") + "', loc: '" + entry[2].replace(' ', '&nbsp;') + "'},\n")

    with open('java_end.txt', 'r') as java_end:
        for line in java_end:
            java_file.write(line)
    java_end.close()

java_file.close()