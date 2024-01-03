# def count_insults(insults):
#     # Initialize the total insult count to 0
#     total_insults = 0

#     # Loop through each insult in the dictionary
#     for insult in insults:
#         # Increment the total insult count by the number of times the insult is used
#         total_insults += insults[insult]

#     # Return the total insult count
#     return total_insults


# insults = {"stupid": 3, "idiot": 2, "moron": 1}
# print(count_insults(insults))  # Output: 6

# insults = {}
# print(count_insults(insults))  # Output: 0


def count_insults(insults):
    # Initialize the total insult count to 0
    total_insults = 0

    # Loop through each insult in the dictionary
    for insult in insults:
        # Increment the total insult count by the number of times the insult is used
        total_insults += insults[insult]

    # Format the output as "total_amount_adjectives({ "a": "moron" }) ➞ 1"
    output = f"total_amount_adjectives({insults!r}) ➞ {total_insults}"

    # Return the formatted output
    return output
