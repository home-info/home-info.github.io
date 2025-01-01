import json
from datetime import date, timedelta
import random
import os

full_recipe_list = []

for filename in os.listdir('wochen/'):
    if filename.startswith("woche-"):
        os.remove('wochen/'+filename)

with open('recipes.json', 'r') as file:
    database = json.load(file)
file.close()

year = 2025  # date.today().year
current_date = date(year, 1, 1)
weekday_names = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
season_code = {1: 4, 2: 4, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2, 9: 3, 10: 3, 11: 3, 12: 4}

with open('index.html', 'w') as html:
    # html.write("<!DOCTYPE HTML><html><head><title>Essensplan</title>  <meta charset='utf-8'/>  <meta name='viewport' content='width=device-width, initial-scale=1, user-scalable=no'/>  <link rel='stylesheet' href='assets/css/main.css'/>  <noscript>    <link rel='stylesheet' href='assets/css/noscript.css'/>  </noscript></head><body class='is-preload'><div id='wrapper' class='fade-in'>  <div id='intro'><h1>Essensplan</h1>    <ul class='actions'>      <li><a href='#header' class='button icon solid solo fa-arrow-down scrolly'>Continue</a></li>    </ul>  </div>  <header id='header'><a href='index.html' class='logo'>Essensplan</a></header>  <nav id='nav'>    <ul class='links'>      <li class='active'><a href='#'>Übersicht</a></li> <li><div id='speiseplan-link'>Lade aktuellen Speiseplan...</div></li>  </ul>  </nav>  <div id='main'>    <section class='post'>      <header class='major'>        <span class='date'>Plan für das Jahr " + str(year) + "</span>        <h1>Übersicht</h1>        <p>Der Plan für die aktuelle Woche kann im Menü aufgerufen werden.</p>      </header>")
    html.write(
        "<!DOCTYPE HTML><html><head><title>Essensplan</title>  <meta charset='utf-8'/>  <meta name='viewport' content='width=device-width, initial-scale=1, user-scalable=no'/>  <link rel='stylesheet' href='assets/css/main.css'/>  <noscript>    <link rel='stylesheet' href='assets/css/noscript.css'/>  </noscript></head><body class='is-preload'><div id='wrapper' class='fade-in'>  <div id='intro'><h1>Essensplan</h1>    <ul class='actions'>      <li><a href='#header' class='button icon solid solo fa-arrow-down scrolly'>Continue</a></li>    </ul>  </div>  <header id='header'><a href='index.html' class='logo'>Essensplan</a></header>  <nav id='nav'>    <ul class='links'>      <li class='active'><a href='#'>Übersicht</a></li> <li><a href='./wochen/wochenansicht.html'>Wochenansicht</a></li>  </ul>  </nav>  <div id='main'>    <section class='post'>      <header class='major'>        <span class='date'>Plan für das Jahr " + str(
            year) + "</span>        <h1>Übersicht</h1>        <p>Der Plan für die aktuelle Woche kann im Menü aufgerufen werden.</p>      </header>")
    html.close()

last_meals_memory = []
kalenderwoche_int = 0
kalenderwoche = 0
while current_date <= date(year, 12, 31):
    season_filter = [0, season_code[current_date.month]]
    time_filter = [1, 2] if current_date.weekday() > 3 else [0]
    filtered_recipes = [recipe for recipe in database['recipes'] if
                        set(season_filter) & set(recipe['season_tag']) and set(time_filter) & set(recipe['time_tag'])]

    random_recipe = filtered_recipes[random.randint(0, len(filtered_recipes) - 1)]
    while random_recipe in last_meals_memory:
        random_recipe = filtered_recipes[random.randint(0, len(filtered_recipes) - 1)]

    if current_date.weekday() == 4:
        kalenderwoche_int = int(current_date.strftime("%V")) + 1
        kalenderwoche = str(kalenderwoche_int).zfill(2)

    if not os.path.exists('wochen/woche-' + str(kalenderwoche) + '.html'):
        with open('wochen/woche-' + str(kalenderwoche) + '.html', 'w') as week_file:
            week_file.write("<header class='major'>   <h1>" + str(kalenderwoche_int) + ". Woche</h1>  </header>")
    with open('wochen/woche-' + str(kalenderwoche) + '.html', 'a') as week_file:
        week_file.write(
            "<h3>" + weekday_names[current_date.weekday()] + ", " + current_date.strftime("%d.%m.%Y") + "</h3>")
        week_file.write("<b>" + random_recipe['title'] + "</b><br>")
        week_file.write("<i>" + random_recipe['source'] + "</i>")
        week_file.write("<details><summary>Zutaten für " + str(random_recipe['servings']) + " Personen</summary><ul>")
        for ingredient in random_recipe['ingredients']:
            week_file.write("<li>" + ingredient + "</li>")
        week_file.write("</ul></details><hr>")

    with open('index.html', 'a') as html:
        html.write("<h3>" + weekday_names[current_date.weekday()] + ", " + current_date.strftime("%d.%m.%Y") + "</h3>")
        html.write("<b>" + random_recipe['title'] + "</b><br>")
        html.write("<i>" + random_recipe['source'] + "</i>")
        html.write("<details><summary>Zutaten für " + str(random_recipe['servings']) + " Personen</summary><ul>")
        for ingredient in random_recipe['ingredients']:
            html.write("<li>" + ingredient + "</li>")
        html.write("</ul></details><hr>")

    last_meals_memory.append(random_recipe)
    if len(last_meals_memory) >= 28:
        del last_meals_memory[0]

    current_date += timedelta(days=1)

    full_recipe_list.append(random_recipe['title'])

with open('index.html', 'a') as html:
    html.write(
        "<footer id='footer'></footer>      <div id='copyright'>        <ul><!---<li>&copy; Untitled</li>-->          <!--          <li>Design: <a href=''>HTML5 UP</a></li>-->        </ul>      </div>  </div>  <script src='assets/js/jquery.min.js'></script>  <script src='assets/js/jquery.scrollex.min.js'></script>  <script src='assets/js/jquery.scrolly.min.js'></script>  <script src='assets/js/browser.min.js'></script>  <script src='assets/js/breakpoints.min.js'></script>  <script src='assets/js/util.js'></script>  <script src='assets/js/main.js'></script><!--<script src='current_week.js'></script>--></body></html>")

    # for filename in os.listdir('wochen/'):
    #     if filename.startswith("woche-"):
    #         with open("wochen/"+filename, 'a') as file:
    #             file.write("<footer id='footer'></footer>      <div id='copyright'>        <ul><!---<li>&copy; Untitled</li>-->          <!--          <li>Design: <a href=''>HTML5 UP</a></li>-->        </ul>      </div>  </div>  <script src='../assets/js/jquery.min.js'></script>  <script src='../assets/js/jquery.scrollex.min.js'></script>  <script src='../assets/js/jquery.scrolly.min.js'></script>  <script src='../assets/js/browser.min.js'></script>  <script src='../assets/js/breakpoints.min.js'></script>  <script src='../assets/js/util.js'></script>  <script src='../assets/js/main.js'></script><script src='current_week.js'></script></body></html>")

with open('statistics.csv', 'w') as stat_file:
    with open('recipes.json', 'r') as file:
        database = json.load(file)
    file.close()
    stat_file.write('Rezept;Häufigkeit\n')
    for recipe in database['recipes']:
        stat_file.write(recipe['title'] + ";" + str(full_recipe_list.count(recipe['title'])) + '\n')
stat_file.close()