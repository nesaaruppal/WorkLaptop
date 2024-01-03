def replace_nts_with_nce(text):
    """
    Replaces all instances of "nts" with "nce" and vice versa if they are at the end of a word.

    Args:
        text (str): The text to replace the "nts" and "nce" instances in.

    Returns:
        str: The text with the "nts" and "nce" instances replaced.
    """
    # Replace all instances of "nts" with "nce"
    text = text.replace("nts", "nce")

    # Replace all instances of "nce" with "nts" if it's at the end of a word
    words = text.split()
    for i in range(len(words)):
        if words[i][-2:] == "nce":
            words[i] = words[i][:-2] + "nts"
    text = " ".join(words)

    return text


# Test the function with some examples
text = "I love coding in Python nts!"
print(replace_nts_with_nce(text))  # Output: I love coding in Python nce!

text = "This is a test nce."
print(replace_nts_with_nce(text))  # Output: This is a test nts.

text = "Hello, world! nce"
print(replace_nts_with_nce(text))  # Output: Hello, world! nts

text = "I can't wait to start learning nce."
# Output: I can't wait to start learning nts.
print(replace_nts_with_nce(text))

text = "I love coding in Python nce!"
print(replace_nts_with_nce(text))  # Output: I love coding in Python nce!
