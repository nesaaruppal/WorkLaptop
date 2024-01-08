def capital_indexes(s):
    return [i for i, ltr in enumerate(s) if ltr.isupper()]


print(capital_indexes("Hello World!"))
