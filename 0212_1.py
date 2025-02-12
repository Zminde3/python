def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
def filtruoti_lyginius(seka):
    for skaicius in seka:
        if skaicius % 2 == 0:
            yield skaicius

n = 20
fib_seka = list(fib_generator(n))
lyginiu_fib = list(filtruoti_lyginius(fib_seka))

print(f"Pirmi {n} Fibonacci skaičiai: {fib_seka}")
print(f"Lyginiai Fibonacci skaičiai: {lyginiu_fib}")
