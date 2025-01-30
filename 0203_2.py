from datetime import datetime as d, date
dt1 = d(1995, 7, 14, 15, 30)
print(f"🕒 Data su laiku: {dt1:%Y-%m-%d %H:%M:%S}")
dt2 = date(2023, 1, 1)
print(f"📆 Tik data: {dt2}")
dienos = (date.today() - date(2000, 1, 1)).days
print(f"📅 Praėjo <{dienos}> dienų nuo 2000-01-01.")
