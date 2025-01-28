from random import randint, choice
import datetime as dt
print(f"Atsitiktinis skaičius: {randint(1, 10)}")
print(f"Atsitiktinis vaisius: {choice(['obuolys', 'bananas', 'kriaušė', 'vyšnia'])}")
print(f"Dabartinė data ir laikas: {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
