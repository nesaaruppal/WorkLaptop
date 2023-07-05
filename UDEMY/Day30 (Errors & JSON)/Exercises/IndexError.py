fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.

try:
    def make_pie(index):
        fruit = fruits[index]
        print(fruit + " pie")
        
except NameError ("'Index' not defined!"):
    def make_pie(fruits):
        fruit = fruits[fruit]
        print(fruit + " pie")

except IndexError:
    def make_pie(fruits):
        fruit = [fruit for fruit in fruits]
        print(fruit + "pie")
        
except UnboundLocalError:
    def make_pie(fruits):
        fruit = [fruit for fruit in fruits]
        print(fruit + "pie")
        
except TypeError:
    def make_pie(fruits):
        fruit = [fruit for fruit in fruits]
        print(fruit + "Pie")
        
    

# CORRECT CODE
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + " pie")



make_pie(4)
