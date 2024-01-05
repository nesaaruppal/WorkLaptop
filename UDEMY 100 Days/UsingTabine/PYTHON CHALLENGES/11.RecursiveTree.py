def three_branched_tree(level):
    if level == 0:
        return
    node = [None] * 3
    for i in range(3):
        node[i] = three_branched_tree(level - 1)
    return node


print(three_branched_tree(3))
