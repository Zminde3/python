from random import randint, choice
import datetime as dt
print(f"Atsitiktinis skaičius: {randint(1, 10)}")
print(f"Atsitiktinis vaisius: {choice(['obuolys', 'bananas', 'kriaušė', 'vyšnia'])}")
print(f"Dabartinė data ir laikas: {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

from datetime import datetime
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

from datetime import datetime as d
print(d.now().strftime("%F %T"))


