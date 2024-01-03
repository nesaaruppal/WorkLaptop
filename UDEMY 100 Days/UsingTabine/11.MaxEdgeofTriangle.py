def next_edge(side1, side2):
    max_range = (side1 + side2) - 1
    return max_range


print(next_edge(8, 10))
print(next_edge(5, 7))
print(next_edge(9, 2))
