def fib_gen(qty=None):
    a, b = 0, 1
    count = 0

    while True:
        if qty is not None and count >= qty:
            break
        yield a
        a, b = b, a + b
        count += 1


fib_Numbers = list(fib_gen(10))
print(fib_Numbers)
