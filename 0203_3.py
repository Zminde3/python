# from datetime import datetime as d
# while True:
#     try:
#         ivestis = input("📆 Įveskite datą (YYYY-MM-DD): ")
#         dt = d.strptime(ivestis, "%Y-%m-%d")
#         print(f"✅ Teisinga data: {dt}")
#         break
#     except ValueError:
#         print("❌ Klaida: įveskite datą teisingu formatu!")
# dt2 = d(2022, 12, 31, 23, 59, 59)
# print(f"📅 {dt2.strftime('%d/%m/%Y %H:%M:%S')}")
# print(f"📆 {dt2.strftime('%Y metų %B %d diena')}")


# from datetime import datetime as d
# menesiai = {
#     "January": "sausio", "February": "vasario", "March": "kovo",
#     "April": "balandžio", "May": "gegužės", "June": "birželio",
#     "July": "liepos", "August": "rugpjūčio", "September": "rugsėjo",
#     "October": "spalio", "November": "lapkričio", "December": "gruodžio"
# }
# while True:
#     try:
#         ivestis = input("📆 Įveskite datą (YYYY-MM-DD, pvz., 2024-02-03): ")
#         dt = d.strptime(ivestis, "%Y-%m-%d")
#         print(f"✅ Teisinga data: {dt}")
#         break
#     except ValueError:
#         print("❌ Klaida: įveskite datą teisingu formatu!")
# dt2 = d(2022, 12, 31, 23, 59, 59)
# angliskas_menesio_pavadinimas = dt2.strftime("%B")
# lietuviskas_menesio_pavadinimas = menesiai.get(angliskas_menesio_pavadinimas, angliskas_menesio_pavadinimas)
# print(f"📅 {dt2.strftime('%d/%m/%Y %H:%M:%S')}")
# print(f"📆 {dt2.strftime('%Y metų')} {lietuviskas_menesio_pavadinimas} {dt2.strftime('%d')} diena")

from datetime import datetime as d
menesiai = {
    "January": "sausio", "February": "vasario", "March": "kovo",
    "April": "balandžio", "May": "gegužės", "June": "birželio",
    "July": "liepos", "August": "rugpjūčio", "September": "rugsėjo",
    "October": "spalio", "November": "lapkričio", "December": "gruodžio"
}
def gauti_teisinga_data():
    while True:
        try:
            ivestis = input("📆 Įveskite datą (YYYY-MM-DD, pvz., 2024-02-03): ").strip()
            dt = d.strptime(ivestis, "%Y-%m-%d")
            return dt
        except ValueError:
            print("❌ Klaida: įveskite datą teisingu formatu!")
dt1 = gauti_teisinga_data()
print(f"✅ Teisinga data: {dt1}")
dt2 = d(2022, 12, 31, 23, 59, 59)
menesio_pavadinimas = menesiai.get(dt2.strftime("%B"), dt2.strftime("%B"))
print(f"📅 {dt2.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"📆 {dt2.strftime('%Y metų')} {menesio_pavadinimas} {dt2.strftime('%d')} diena")

