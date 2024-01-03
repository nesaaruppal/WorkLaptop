def cubes(n):
    if n == 0:
        return 1
    else:
        return n**3


print(f"cubes({3}) = {cubes(3)}")
print(f"cubes({5}) = {cubes(5)}")
print(f"cubes({10}) = {cubes(10)}")
