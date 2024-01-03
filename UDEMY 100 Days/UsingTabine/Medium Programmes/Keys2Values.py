def invert_dict(d):
    return {v: k for k, v in d.items()}

invert_dict({'z': 'q', 'w': 'f'})

print(invert_dict({'z': 'q', 'w': 'f'}))

invert_dict({1: "a", 2: "b", 3: "c"})
print(invert_dict({1: "a", 2: "b", 3: "c"}))