import csv

f1 = open("essensplan_DB.csv", "r")
reader = csv.DictReader(f1, delimiter=",")
rID = []
for line in reader:
    rID.append(line)
f1.close()

f2 = open("rezepte_DB.csv", "r")
reader = csv.reader(f2, delimiter=",")
rezepte = []
for line in reader:
    rezepte.append(line)
f2.close()

html = []
html_code = []

for id in rID:
    day = id["Tag"]
    id = int(id["ID"])

    gericht = rezepte[id][1]
    if rezepte[id][3] != "":
        ort = rezepte[id][2] + " (" + rezepte[id][3] + ")"
    else:
        ort = rezepte[id][2]

    # Zutaten
    ind = -1
    while rezepte[id][ind] == "":
        ind = ind - 1
    if ind == -1:
        ind = len(rezepte[id])
    else:
        ind = ind + 1
    zutaten_raw = rezepte[id][5:ind]
    zutaten = []
    menge = []
    zutat = []

    for i in range(0,len(zutaten_raw)):
        if i % 2 == 0:
            menge.append(i)
        if i % 2 == 1:
            zutat.append(i)

    for x, y in zip(menge, zutat):
        zutaten.append(zutaten_raw[x] + " " + zutaten_raw[y])
    entry = []
    entry.append(day)
    entry.append(gericht)
    entry.append(ort)
    entry.append(zutaten)
    html.append(entry)


for code in html:
    code_zutaten = ""
    for i in code[3]:
        code_zutaten = str(code_zutaten) + "<li>"+i+"</li>"

    html_line = "<article id='"+code[0]+"' class='panel'><header><h2>DATUM FEHLT!</h2></header><h3>"+code[1]+"</h3><b>"+code[2]+"</p>Zutaten:<ul>"+code_zutaten+"</ul></b></article>\n"
    html_code.append(html_line)

html_code_string = "".join(html_code)
html_code_string = html_code_string.replace(" & "," &amp; ")

f3 = open("html5/vorlage.html", "r")
f3_code = []
for line in f3:
    line = line.replace("#INHALT", html_code_string)
    f3_code.append(line)
f3.close()

f4 = open("html5/index.html", "w")
for line in f3_code:
    f4.write(line)
f4.close()