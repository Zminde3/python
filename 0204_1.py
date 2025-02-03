# from datetime import date, timedelta
# d1, d2 = date(2023, 1, 1), date(2024, 1, 1)
# print(f"📆 Dienų skirtumas: {(d2 - d1).days}")
# dabartine = date.today()
# print(f"📅 Data po 90 dienų: {dabartine + timedelta(days=90)}")
# skirtumas = date.today() - date(2000, 1, 1)
# print(f"🗓️ Dienų: {skirtumas.days}, ⏳ Valandų: {skirtumas.seconds}, ⏲️ Sekundžių: {int(skirtumas.total_seconds())}")

from datetime import datetime, date, timedelta
d1, d2 = date(2023, 1, 1), date(2024, 1, 1)
print(f"📆 Dienų skirtumas: {(d2 - d1).days}")
dabartine = date.today()
print(f"📅 Data po 90 dienų: {dabartine + timedelta(days=90)}")
dabar = datetime.now()
skirtumas = dabar - datetime(2000, 1, 1)
print(f"🗓️ Dienų: {skirtumas.days}, ⏳ Valandų: {skirtumas.seconds // 3600}, ⏲️ Sekundžių: {int(skirtumas.total_seconds())}")

