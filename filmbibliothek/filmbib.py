import csv
from datetime import datetime

f = open("filmbib_db.csv", newline='')
liste = []
reader = csv.reader(f, delimiter=",")
for a in reader:
    liste.append(a)
f.close()

for b in liste:
     b[0] = b[0].lower().replace("ä", "a").replace("ö","o").replace("ü","u").replace("ß","ss")
     b[1] = b[1].lower().replace("ä", "a").replace("ö","o").replace("ü","u").replace("ß","ss")

liste_sort = sorted(liste, key = lambda x: (x[0], x[1]))

indices = []

for c in liste_sort:
    index = liste.index(c)
    indices.append(index)

filme = []

f2 = open("filmbib_db.csv", newline='')
filme_reader = csv.reader(f2, delimiter=",")
for film in filme_reader:
    filme.append(film)
f2.close()

liste_final = []

for number in indices:
    liste_final.append(filme[number])

html_code_list = []

for d in liste_final:
    html_code_list.append("<tr><td style='border-bottom-width:2px; border-bottom-style:dashed; border-bottom-color:#000000; border-left-style:none; border-right-style:none'>" + d[0] + "</td><td style='border-bottom-width:2px; border-bottom-style:dashed; border-bottom-color:#000000; border-left-style:none; border-right-style:none'>" + d[1] + "</td><td style='border-bottom-width:2px; border-bottom-style:dashed; border-bottom-color:#000000; border-left-style:none; border-right-style:none'><center>" + d[2] + "</center></td></tr>")

html_code = "".join(html_code_list)


vorlage = open("vorlage.txt", "r")
vorlage_lines = []
for code in vorlage:
    vorlage_lines.append(code)
vorlage.close()

filmbib_code = []

datum = str(datetime.today().strftime('%d.%m.%Y')) + "</p>"

filmbib = open("filmbibliothek.html", "w")
for v_line in vorlage_lines:
    filmbib_line = v_line.replace("#DATUM</p>", datum).replace("#INHALT\n", html_code)
    filmbib_code.append(filmbib_line)

for code_line in filmbib_code:
    filmbib.write(code_line)

filmbib.close()