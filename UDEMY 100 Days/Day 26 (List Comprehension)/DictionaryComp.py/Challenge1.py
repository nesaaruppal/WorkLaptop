sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
split_sentence = sentence.split()
for word in split_sentence:
    print(len(word))
print(split_sentence)

result = {word: len(word) for word in split_sentence}
print(result)