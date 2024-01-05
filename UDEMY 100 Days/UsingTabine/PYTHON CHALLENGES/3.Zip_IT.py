def zipLists(list1, list2):
    # Check if both lists have the same length
    if len(list1) != len(list2):
        # If not, ignore the extra values in the longer list
        if len(list1) > len(list2):
            list2 = list2[:len(list1)]
        else:
            list1 = list1[:len(list2)]

    # Zip the two lists together
    zipped_list = list(zip(list1, list2))

    # Return the zipped list
    return zipped_list


list1 = ['a', 'b', 'c', 'd']
list2 = ['e', 'f', 'g', 'h', 'i']

print(zipLists(list1, list2))
