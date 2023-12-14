
                ##### LIST COMPREHENSION #####
    ##### 'new_list' = ['new_item' for 'item' in 'list'] #####
    
    
# Create a new list from a previous list 
    # Instead of a FOR loop
    # E.G.
        # numbers = [1, 2, 3]
        # new_list = []
        # for n in numbers:
            # add_1 = n + 1
            #new_list.append(add_1)
            
# 'new_list' = ['new_item' for 'item' in 'list']

# Can then replace each item:
# Using above example
    # 'list' = numbers
        ## 'new_list' = [new_item for item in 'numbers']
    # 'item' = n
        ## new_list = [new_item for 'n' in 'numbers']
    # 'new_item' = n+1
        ## new_list = ['n + 1' for 'n' in 'numbers']
        
# LIST COMPREHENSION:
##### new_list = [n+1 for n in numbers] #####


# List Comprehension with Strings
    # name = "Nesaar"
    # new_list = [letter for letter in name]
    # print(new_list)
    
    
# SEQUENCES
    # list
    # range
    # string 
    # tuple
    
# CONDITIONAL List Comprehension
    # new_list = [new_item for item in list IF test]