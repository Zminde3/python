# import datetime as dt
# from datetime import datetime, timedelta
#
# # Dabartinė data ir laikas
# now = datetime.now()
# print(f"📅 Dabartinė data ir laikas: {now.strftime('%Y-%m-%d %H:%M:%S')}")
#
# # Tik šiandienos data
# print(f"📆 Tik data: {dt.date.today()}")

# # Tik valandos, minutės, sekundės
# print(f"⏰ Laikas: {now.hour}:{now.minute}:{now.second}")
#
# # Sukuriame konkrečią datą ir laiką
# custom_date = datetime(2025, 12, 31, 23, 59, 59)
# print(f"🎯 Sukurta data: {custom_date}")
#
# # Laiko formatavimas (pvz., norint rodymo su savaitės diena)
# print(f"📌 Formatuota data: {now.strftime('%A, %d %B %Y')}")
#
# # Konvertuojame tekstą į `datetime`
# str_data = "2025-12-31 23:59:59"
# converted = datetime.strptime(str_data, "%Y-%m-%d %H:%M:%S")
# print(f"🔄 Konvertuota iš string: {converted}")
#
# # Laiko skirtumai (`timedelta`)
# po_7_dienu = now + timedelta(days=7)
# print(f"⏳ Data po 7 dienų: {po_7_dienu}")
#
# # UNIX timestamp į `datetime`
# timestamp = 1707000000
# print(f"🕰️ UNIX į normalų formatą: {datetime.fromtimestamp(timestamp)}")


from datetime import datetime as d
print(f"🕒 Dabar yra {d.today().strftime('%H:%M')}, {d.today().strftime('%d-%m-%Y')}")

