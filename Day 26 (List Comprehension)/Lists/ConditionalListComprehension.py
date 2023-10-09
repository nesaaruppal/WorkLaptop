#new_list = ['new_item' for 'item' in 'list' 'if test']

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)


#name.upper()
upper_case_names = [name.upper() for name in names if len(name) > 5]
print(upper_case_names)