# List Creation
# Indexing BEGINS at "0" with []
states_of_america = ["Delaware", "Pennsylvania", "New Jersey",
                     "Georgia", "Connecticut", "Massachusetts", "Maryland", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[3])
print(states_of_america[14])

# Negative numbers start counting from the end of the list
# "-1" will give you the last element in the list
print(states_of_america[-5])

# APPENDING A LIST
# Index the item and then append it to whatever you want it to be
states_of_america[0] = "DelllahWare"
print(states_of_america)

# Append()
# Will add a single item to the end of the list
states_of_america.append("United Kingdom")
print(states_of_america)

# Extend()
# Allows you to add multiple items to a list by adding a list to it
# Must be a function - Extend() and then a List []
states_of_america.extend(["Britain", "England", "Wales"])
print(states_of_america)
