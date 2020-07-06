def sq_sum(a, *args):
    total = 0.0
    total += a ** 2
    for x in args:
        total += x ** 2
    return round(total, 2)

