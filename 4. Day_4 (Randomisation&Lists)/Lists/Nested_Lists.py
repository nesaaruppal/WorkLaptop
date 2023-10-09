# Nested Lists
# This list contains fruits and vegetables
dirty_dozen = ["Strawberrys", "Spinach", "Kale", "Nectarines", "Apples",
               "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# It is possible to create two seperate lists to seperate these out
fruits = ["Strawberrys", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]


# Nested Lists can combine these
dirty_dozen2 = [fruits, vegetables]

print(dirty_dozen2)
print(dirty_dozen2[0])
