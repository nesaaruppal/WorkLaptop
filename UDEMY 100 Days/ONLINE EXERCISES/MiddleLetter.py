def mid(s):
    if len(s) % 2 == 0:
        return s[(len(s) // 2):(len(s) // 2) + 1]
    else:
        return s[(len(s) // 2) - 1]


print(mid("abc"))
print(mid("aaaa"))
