import json
from datetime import date, timedelta

year = 2024 #date.today().year
current_date = date(year, 1, 1)
season_code = {1: 4, 2: 4, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2, 9: 3, 10: 3, 11: 3, 12: 4}

WeekEndSpring = []
WeekDaySpring = []
WeekEndSummer = []
WeekDaySummer = []
WeekEndFall = []
WeekDayFall = []
WeekEndWinter = []
WeekDayWinter = []

while current_date <= date(year, 12, 31):
    if season_code[current_date.month] == 1:
        if current_date.weekday() > 3:
            WeekEndSpring.append(current_date)
        else:
            WeekDaySpring.append(current_date)
    elif season_code[current_date.month] == 2:
        if current_date.weekday() > 3:
            WeekEndSummer.append(current_date)
        else:
            WeekDaySummer.append(current_date)
    elif season_code[current_date.month] == 3:
        if current_date.weekday() > 3:
            WeekEndFall.append(current_date)
        else:
            WeekDayFall.append(current_date)
    elif season_code[current_date.month] == 4:
        if current_date.weekday() > 3:
            WeekEndWinter.append(current_date)
        else:
            WeekDayWinter.append(current_date)

    current_date += timedelta(days=1)









with open('recipes.json', 'r') as file:
    database = json.load(file)
file.close()

winter = [recipe['title'] for recipe in database['recipes'] if set([0, 4]) & set(recipe['season_tag'])]
print("WINTER ................. : " + str(len(winter)))

winter_werktag = [recipe['title'] for recipe in database['recipes'] if set([0, 4]) & set(recipe['season_tag']) and 0 in recipe['time_tag']]
quotient = int(round((len(winter_werktag)/len(WeekDayWinter))*100, 0))
print("--- davon für  WOCHENTAGE: " + str(len(winter_werktag)) + " / " + str(len(WeekDayWinter)) + " = " + str(quotient) + " %")

winter_wochenende = [recipe['title'] for recipe in database['recipes'] if set([0, 4]) & set(recipe['season_tag']) and 2 in recipe['time_tag']]
quotient = int(round((len(winter_wochenende)/len(WeekEndWinter))*100, 0))
print("--- davon für WOCHENENDEN: " + str(len(winter_wochenende)) + " / " + str(len(WeekEndWinter)) + " = " + str(quotient) + " %")
print()


winter = [recipe['title'] for recipe in database['recipes'] if set([0, 1]) & set(recipe['season_tag'])]
print("FRÜHLING ............... : " + str(len(winter)))

winter_werktag = [recipe['title'] for recipe in database['recipes'] if set([0, 1]) & set(recipe['season_tag']) and 0 in recipe['time_tag']]
quotient = int(round((len(winter_werktag)/len(WeekDaySpring))*100, 0))
print("--- davon für  WOCHENTAGE: " + str(len(winter_werktag)) + " / " + str(len(WeekDaySpring)) + " = " + str(quotient) + " %")

winter_wochenende = [recipe['title'] for recipe in database['recipes'] if set([0, 1]) & set(recipe['season_tag']) and 2 in recipe['time_tag']]
quotient = int(round((len(winter_wochenende)/len(WeekEndSpring))*100, 0))
print("--- davon für WOCHENENDEN: " + str(len(winter_wochenende)) + " / " + str(len(WeekEndSpring)) + " = " + str(quotient) + " %")
print()



winter = [recipe['title'] for recipe in database['recipes'] if set([0, 2]) & set(recipe['season_tag'])]
print("SOMMER ................. : " + str(len(winter)))

winter_werktag = [recipe['title'] for recipe in database['recipes'] if set([0, 2]) & set(recipe['season_tag']) and 0 in recipe['time_tag']]
quotient = int(round((len(winter_werktag)/len(WeekDaySummer))*100, 0))
print("--- davon für  WOCHENTAGE: " + str(len(winter_werktag)) + " / " + str(len(WeekDaySummer)) + " = " + str(quotient) + " %")

winter_wochenende = [recipe['title'] for recipe in database['recipes'] if set([0, 2]) & set(recipe['season_tag']) and 2 in recipe['time_tag']]
quotient = int(round((len(winter_wochenende)/len(WeekEndSummer))*100, 0))
print("--- davon für WOCHENENDEN: " + str(len(winter_wochenende)) + " / " + str(len(WeekEndSummer)) + " = " + str(quotient) + " %")
print()









winter = [recipe['title'] for recipe in database['recipes'] if set([0, 3]) & set(recipe['season_tag'])]
print("HERBST ................. : " + str(len(winter)))

winter_werktag = [recipe['title'] for recipe in database['recipes'] if set([0, 3]) & set(recipe['season_tag']) and 0 in recipe['time_tag']]
quotient = int(round((len(winter_werktag)/len(WeekDayFall))*100, 0))
print("--- davon für  WOCHENTAGE: " + str(len(winter_werktag)) + " / " + str(len(WeekDayFall)) + " = " + str(quotient) + " %")

winter_wochenende = [recipe['title'] for recipe in database['recipes'] if set([0, 3]) & set(recipe['season_tag']) and 2 in recipe['time_tag']]
quotient = int(round((len(winter_wochenende)/len(WeekEndFall))*100, 0))
print("--- davon für WOCHENENDEN: " + str(len(winter_wochenende)) + " / " + str(len(WeekEndFall)) + " = " + str(quotient) + " %")
print()










wochentage = [recipe['title'] for recipe in database['recipes'] if 0 in recipe['time_tag']]
print('Insgesamt für WOCHENTAGE : ' + str(len(wochentage)))

wochenende = [recipe['title'] for recipe in database['recipes'] if 2 in recipe['time_tag']]
print('Insgesamt für WOCHENENDE : ' + str(len(wochenende)))






WeekEndSpring = []
WeekDaySpring = []
WeekEndSummer = []
WeekDaySummer = []
WeekEndFall = []
WeekDayFall = []
WeekEndWinter = []
WeekDayWinter = []

current_date = date(year, 1, 1)
while current_date <= date(year, 12, 31):
    if season_code[current_date.month] == 1:
        if current_date.weekday() > 3:
            WeekEndSpring.append(current_date)
        else:
            WeekDaySpring.append(current_date)
    elif season_code[current_date.month] == 2:
        if current_date.weekday() > 3:
            WeekEndSummer.append(current_date)
        else:
            WeekDaySummer.append(current_date)
    elif season_code[current_date.month] == 3:
        if current_date.weekday() > 3:
            WeekEndFall.append(current_date)
        else:
            WeekDayFall.append(current_date)
    elif season_code[current_date.month] == 4:
        if current_date.weekday() > 3:
            WeekEndWinter.append(current_date)
        else:
            WeekDayWinter.append(current_date)

    current_date += timedelta(days=1)
#
# with open('statistics.csv', 'w') as stat_file:
#     with open('recipes.json', 'r') as file:
#         database = json.load(file)
#     file.close()
#
#     winter = [recipe['title'] for recipe in database['recipes'] if set([0, 4]) & set(recipe['season_tag'])]
#     stat_file.write('WINTER;' + str(len(winter)) + '\n')
#
#     winter_werktag = [recipe['title'] for recipe in database['recipes'] if
#                       set([0, 4]) & set(recipe['season_tag']) and 0 in recipe['time_tag']]
#     quotient = int(round((len(winter_werktag) / len(WeekDayWinter)) * 100, 0))
#     stat_file.write('davon für WOCHENTAGE;' + str(len(winter_werktag)) + ';' + str(len(WeekDayWinter)) + ';' + str(
#         quotient) + " %\n")
#
#     winter_wochenende = [recipe['title'] for recipe in database['recipes'] if
#                          set([0, 4]) & set(recipe['season_tag']) and 2 in recipe['time_tag']]
#     quotient = int(round((len(winter_wochenende) / len(WeekEndWinter)) * 100, 0))
#     stat_file.write('davon für WOCHENENDEN;' + str(len(winter_wochenende)) + ';' + str(len(WeekEndWinter)) + ';' + str(
#         quotient) + " %\n")
#
#     winter = [recipe['title'] for recipe in database['recipes'] if set([0, 1]) & set(recipe['season_tag'])]
#     stat_file.write('FRÜHLING;' + str(len(winter)) + '\n')
#
#     winter_werktag = [recipe['title'] for recipe in database['recipes'] if
#                       set([0, 1]) & set(recipe['season_tag']) and 0 in recipe['time_tag']]
#     quotient = int(round((len(winter_werktag) / len(WeekDaySpring)) * 100, 0))
#     stat_file.write('davon für WOCHENTAGE;' + str(len(winter_werktag)) + ';' + str(len(WeekDaySpring)) + ';' + str(
#         quotient) + " %\n")
#
#     winter_wochenende = [recipe['title'] for recipe in database['recipes'] if
#                          set([0, 1]) & set(recipe['season_tag']) and 2 in recipe['time_tag']]
#     quotient = int(round((len(winter_wochenende) / len(WeekEndSpring)) * 100, 0))
#     stat_file.write('davon für WOCHENENDEN;' + str(len(winter_wochenende)) + ';' + str(len(WeekEndSpring)) + ';' + str(
#         quotient) + " %\n")
#
#     winter = [recipe['title'] for recipe in database['recipes'] if set([0, 2]) & set(recipe['season_tag'])]
#     stat_file.write('SOMMER;' + str(len(winter)) + '\n')
#
#     winter_werktag = [recipe['title'] for recipe in database['recipes'] if
#                       set([0, 2]) & set(recipe['season_tag']) and 0 in recipe['time_tag']]
#     quotient = int(round((len(winter_werktag) / len(WeekDaySummer)) * 100, 0))
#     stat_file.write('davon für WOCHENTAGE;' + str(len(winter_werktag)) + ';' + str(len(WeekDaySummer)) + ';' + str(
#         quotient) + " %\n")
#
#     winter_wochenende = [recipe['title'] for recipe in database['recipes'] if
#                          set([0, 2]) & set(recipe['season_tag']) and 2 in recipe['time_tag']]
#     quotient = int(round((len(winter_wochenende) / len(WeekEndSummer)) * 100, 0))
#     stat_file.write('davon für WOCHENENDEN;' + str(len(winter_wochenende)) + ';' + str(len(WeekEndSummer)) + ';' + str(
#         quotient) + " %\n")
#
#     winter = [recipe['title'] for recipe in database['recipes'] if set([0, 3]) & set(recipe['season_tag'])]
#     stat_file.write('HERBST;' + str(len(winter)) + '\n')
#
#     winter_werktag = [recipe['title'] for recipe in database['recipes'] if
#                       set([0, 3]) & set(recipe['season_tag']) and 0 in recipe['time_tag']]
#     quotient = int(round((len(winter_werktag) / len(WeekDayFall)) * 100, 0))
#     stat_file.write('davon für WOCHENTAGE;' + str(len(winter_werktag)) + ';' + str(len(WeekDayFall)) + ';' + str(
#         quotient) + " %\n")
#
#     winter_wochenende = [recipe['title'] for recipe in database['recipes'] if
#                          set([0, 3]) & set(recipe['season_tag']) and 2 in recipe['time_tag']]
#     quotient = int(round((len(winter_wochenende) / len(WeekEndFall)) * 100, 0))
#     stat_file.write('davon für WOCHENENDEN;' + str(len(winter_wochenende)) + ';' + str(len(WeekEndFall)) + ';' + str(
#         quotient) + " %\n")
#     stat_file.write('\n')
#
#     wochentage = [recipe['title'] for recipe in database['recipes'] if 0 in recipe['time_tag']]
#     stat_file.write('Insgesamt für WOCHENTAGE;' + str(len(wochentage)) + '\n')
#
#     wochenende = [recipe['title'] for recipe in database['recipes'] if 2 in recipe['time_tag']]
#     stat_file.write('Insgesamt für WOCHENENDE;' + str(len(wochenende)) + '\n\n')

