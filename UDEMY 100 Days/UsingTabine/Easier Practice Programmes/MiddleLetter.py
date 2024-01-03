def mid(string):
    if len(string) % 2 == 0:
        return string[(len(string) // 2) - 1 : (len(string) // 2)]
    else:
        return string[(len(string) // 2)]
    
print(mid("abc")) # Output: b
print(mid("aaaa")) # Output: 
print(mid("python")) # Output: o
print(mid("hello")) # Output: l
