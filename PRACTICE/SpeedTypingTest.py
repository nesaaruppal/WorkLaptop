import time


def speed_test(words):
    start_time = time.time()
    for word in words:
        time.sleep(0.25)
        print(word, end='')
    print()
    end_time = time.time()
    return end_time - start_time


if __name__ == '__main__':
    words = input("Enter a list of words separated by spaces: ").split()
    time_taken = speed_test(words)
    print(f"Time taken: {time_taken:.2f} seconds")
