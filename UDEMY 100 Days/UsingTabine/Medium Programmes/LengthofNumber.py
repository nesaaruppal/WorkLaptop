def get_length(num):
    length = 0
    while num > 0:
        num = num // 10
        length += 1
    return length


print(get_length(10))
print(get_length(5000))
print(get_length(1))