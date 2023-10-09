import pandas

data = pandas.read_csv(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day26.py\NATO_Alphabet\nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# MY CORRECT CODE (continuous loops NOT good)

#is_on = True
  
#while is_on:
#    try:
#        word = input("Enter a word: ").upper()
#        output_list = [phonetic_dict[letter] for letter in word]
#    except KeyError:
#        print("Sorry, only letters from the alphabet!")
#    else:
#        print(output_list)

# The function will only check for errors and will stop when the word contains all letters.

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet!")
        generate_phonetic()
    else:
        print(output_list)
        
generate_phonetic()