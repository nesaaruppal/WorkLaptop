sentence = input("What is the Airspeed Velocity of an Unladen Swallow")
sentence.tolist()

sentence_dict = {w:sentence for w:len(w) in sentence}
print(sentence_dict)