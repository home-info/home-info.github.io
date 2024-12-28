import datetime
from datetime import timedelta
from telegram import Bot
from telegram import InputFile
def osterdatum(jahr):
    a = jahr % 19
    b = jahr // 100
    c = jahr % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    monat = (h + l - 7 * m + 114) // 31
    tag = ((h + l - 7 * m + 114) % 31) + 1
    return datetime.date(jahr, monat, tag)

ostern1 = osterdatum(2024)
ostern2 = osterdatum(2025)

diff = (ostern2 - ostern1).days
DaysPerSaw = diff / 52
DaysPerSaw = timedelta(days=DaysPerSaw)
print(DaysPerSaw)

interdays = []
interdays.append(ostern1)
current = ostern1
while current < ostern2:
    current = current + DaysPerSaw
    interdays.append(current)
print(len(interdays))


# date_calculation_t0 = datetime.datetime.now()
# heute = datetime.datetime.now().date()
# this_year = datetime.datetime.now().year
# next_year = this_year + 1
# prev_year = this_year - 1
#
# this_year_easter = osterdatum(this_year)
# next_year_easter = osterdatum(next_year)
# last_year_easter = osterdatum(prev_year)
#
# week_dates = []
# date_calculation_t1 = datetime.datetime.now()
# date_calculation_time = date_calculation_t1 - date_calculation_t0
# date_calculation_time = round(date_calculation_time.total_seconds() * 1000, 3)
# print(f'Calculation of Easter Dates:              {date_calculation_time} ms')
#
#
# create_week_date_list_t0 = datetime.datetime.now()
# if this_year_easter <= heute:
#     easter_year = next_year_easter - this_year_easter
#     week_intervall = round(easter_year.days/52)
#     running_week_date = this_year_easter
#     for i in range(0, 52):
#         week_dates.append(running_week_date)
#         running_week_date = running_week_date + timedelta(days=week_intervall)
#
# if this_year_easter > heute:
#     easter_year = this_year_easter - last_year_easter
#     week_intervall = round(easter_year.days/52)
#     running_week_date = last_year_easter
#     for i in range(0, 52):
#         week_dates.append(running_week_date)
#         running_week_date = running_week_date + timedelta(days=week_intervall)
#         if running_week_date == this_year_easter:
#             half_diff = round(week_intervall/2)
#             running_week_date = running_week_date - timedelta(days=half_diff)
# create_week_date_list_t1 = datetime.datetime.now()
# create_week_date_list_time = create_week_date_list_t1 - create_week_date_list_t0
# create_week_date_list_time = round(create_week_date_list_time.total_seconds() * 1000, 3)
# print(f'Calculation and Appending of Week Dates:  {create_week_date_list_time} ms')
#
# send_message_t0 = datetime.datetime.now()
# if heute in week_dates:
#     wochenspruch = week_dates.index(heute) + 1
#     wochenspruch_formatted = str(wochenspruch).zfill(3)
#     spruch_file = '/home/SoulmateCal/seelenkalender/spruch/spruch.' + str(wochenspruch_formatted) + '.png'
#
#     TELEGRAM_TOKEN = "6959209073:AAFlqQS1LJF30nEt9BQUMI8qnVy9s8QwBBg"
#     CHANNEL_ID = "-1002001610359" # Kanal "Seelenkalender"
#     #CHANNEL_ID = "262015236" # Hannes
#     bot = Bot(token=TELEGRAM_TOKEN)
#
#     with open(spruch_file, 'rb') as image_file:
#         next_week = week_dates[wochenspruch]
#         caption = '<b><u>Wochenspruch Nr. ' + str(wochenspruch) + '</u></b>\n' + heute.strftime('%d.%m.%Y') + ' — ' + next_week.strftime('%d.%m.%Y')
#         bot.send_photo(chat_id=CHANNEL_ID, photo=InputFile(image_file), caption=caption, parse_mode='HTML')
# else:
#     pass
#
# send_message_t1 = datetime.datetime.now()
# send_message_time = send_message_t1 - send_message_t0
# send_message_time = round(send_message_time.total_seconds() * 1000, 3)
# print(f'Sending Telegram Message if due:        {send_message_time} ms')