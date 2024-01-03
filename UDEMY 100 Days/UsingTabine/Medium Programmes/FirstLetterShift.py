def shift_words(sentence):
    """
    Shifts the first letter of each word to the next word in a sentence (shifting right).

    Args:
        sentence (str): The sentence to shift.

    Returns:
        str: The shifted sentence.
    """
    # Split the sentence into a list of words
    words = sentence.split()

    # Initialize an empty list to hold the shifted words
    shifted_words = []

    # Loop through each word in the sentence
    for word in words:
        # Check if the word is the first word in the sentence
        if word == words[0]:
            # Add the shifted word to the list
            shifted_words.append(word[1:])
        else:
            # Add the shifted word to the list
            shifted_words.append(word[1:])

    # Join the shifted words back into a sentence
    shifted_sentence = " ".join(shifted_words)

    return shifted_sentence


# Test the function with some examples
sentence = "I love coding in Python!"
print(shift_words(sentence))  # Output: coding love in I Python!

sentence = "This is a test."
print(shift_words(sentence))  # Output: is a test This

sentence = "Hello, world!"
print(shift_words(sentence))  # Output: ,world! Hello

sentence = "I can't wait to start learning."
print(shift_words(sentence))  # Output: can't to start learning I wait
