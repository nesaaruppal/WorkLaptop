def power(base, exponent):
    if exponent == 0:
        return 1
    result = base
    while exponent > 1:
        if exponent % 2 == 1:
            result = result * base
        exponent = exponent // 2
        base = base * base
    return result

print(power(4,3))

