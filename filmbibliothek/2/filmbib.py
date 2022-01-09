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
    html_code_list.append("<tr class='ro3'><td style='text-align:left;width:0.407cm; ' class='ce1'> </td><td style='text-align:left;width:4.193cm; ' class='ce1'> </td><td style='text-align:left;width:15.305cm; ' class='ce6'><p>"+d[0]+"</p></td><td style='text-align:left;width:14.55cm; ' class='ce6'><p>"+d[1]+"</p></td><td style='text-align:left;width:4.057cm; ' class='ce11'><p>"+d[2]+"</p></td><td style='text-align:left;width:7.999cm; ' class='ce1'> </td></tr>")

html_code = "".join(html_code_list)
html_code = html_code.replace(" & ","&amp;")

vorlage = open("vorlage.txt", "r")
vorlage_lines = []
for code in vorlage:
    vorlage_lines.append(code)
vorlage.close()

filmbib_code = []

datum = str(datetime.today().strftime('%d.%m.%Y'))

filmbib = open("filmbibliothek.xhtml", "w")
for v_line in vorlage_lines:
    filmbib_line = v_line.replace("#DATUM", datum).replace("#INHALT", html_code)
    filmbib_code.append(filmbib_line)

for code_line in filmbib_code:
    filmbib.write(code_line)

filmbib.close()