import random

# Define a list of possible nouns
noun = ["cat", "dog", "mouse", "fish"]
nouns = random.choice(noun)

# Define a list of possible verbs
verb = ["ran", "barked", "meowed", "swam"]
verbs = random.choice(verb)

# Define a list of possible adjectives
adjective = ["cute", "adorable", "fluffy", "slimy"]
adjective
# Define a list of possible adverbs
adverbs = ["happily", "sadly", "silently", "quickly"]

# Prompt the user to enter a subject
subject = input("Enter a subject: ")

# Prompt the user to enter an object
object = input("Enter an object: ")

# Generate a random index for each list
noun_index = random.randint(0, len(nouns) - 1)
verb_index = random.randint(0, len(verbs) - 1)
adjective_index = random.randint(0, len(adjectives) - 1)
adverb_index = random.randint(0, len(adverbs) - 1)

# Replace the placeholders in the mad lib sentence
mad_lib_sentence = f"My {subject} {verbs} an {adjectives} {adverbs} {object}."

# Print the mad lib sentence
print(mad_lib_sentence)
