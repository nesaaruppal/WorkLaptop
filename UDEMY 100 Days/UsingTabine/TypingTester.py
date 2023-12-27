import time
import textwrap

def typing_test(text):
    start_time = time.time()
    correct = 0
    text_len = len(text)
    for i in range(text_len):
        char = text[i]
        user_input = input(f"{i+1}/{text_len}: {char}")
        if user_input == char:
            correct += 1
        else:
            print(f"Incorrect, the correct character was {char}.")
            break
    end_time = time.time()
    time_taken = end_time - start_time
    accuracy = correct/text_len
    print(f"You completed the test in {time_taken:.2f} seconds, with an accuracy of {accuracy:.2f}%.")

text = textwrap.dedent("""\
    This is a sample text that you will be typing.
    The text will be displayed one character at a time, and you will have to type it back in.
    Good luck!
    """)
typing_test(text)