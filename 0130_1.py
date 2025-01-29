def dalinti(a, b):
    try: return a / b
    except ZeroDivisionError: return "Dalyba iš nulio negalima."
print(dalinti(10, 2), dalinti(5, 0), dalinti(8, 4))
