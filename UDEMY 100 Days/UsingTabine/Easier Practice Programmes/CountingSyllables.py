def count(word):
    count = 0
    for char in word.split("-"):
        if char.isalpha():
            count += 1
    return count


print(count("ho-tel")) # Output: 2
print(count("cat")) # Output: 1
print(count("met-a-phor")) # Output: 3
print(count("ter-min-a-tor")) # Output: 4