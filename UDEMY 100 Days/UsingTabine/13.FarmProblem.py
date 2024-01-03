def count_legs(chicken_subtotal, cow_subtotal, pig_subtotal):
    # Calculate the total number of chickens
    chicken_count = chicken_subtotal // 2

    # Calculate the total number of cows
    cow_count = cow_subtotal // 4

    # Calculate the total number of pigs
    pig_count = pig_subtotal // 4

    # Calculate the total number of legs
    total_legs = chicken_count + cow_count + pig_count

    # Return the total number of legs
    return total_legs


print(count_legs(2, 3, 5))
print(count_legs(1, 2, 3))
print(count_legs(5, 2, 8))

# chickens = 2 legs
# cows = 4 legs
# pigs = 4 legs

##### SOLUTION #####


def animals(chicken, cow, pig):
    return chicken * 2 + (cow + pig) * 4
