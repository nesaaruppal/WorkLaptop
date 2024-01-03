def capital_indexes(string):
    indexes = []
    for index, char in enumerate(string):
        if char.isupper():
            indexes.append(index)
    return indexes

print(capital_indexes("Hello World!")) # Output: [0, 3, 6]
print(capital_indexes("hello world!")) # Output: [0, 3, 6]
print(capital_indexes("12345")) # Output: []
print(capital_indexes("1aBcdE")) # Output: [1, 3]