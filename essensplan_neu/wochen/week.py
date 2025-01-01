from datetime import date

# Heutiges Datum
heute = date(2027, 1, 1)

# ISO-Kalenderwoche berechnen
_, iso_week, _ = heute.isocalendar()

print(f"Wir befinden uns in der Kalenderwoche {iso_week}.")
