import pandas
data = pandas.read_csv(r"C:\Users\NUppal\OneDrive - CBRE, Inc\CBRE\VSC\Python\UDEMY\UDEMY\Day26.py\NATO_Alphabet\nato_phonetic_alphabet.csv")

#{new_key, new_value for (index, row)in df.dict.iterrows()}
nato_dict = {row.letter: row.code for (letter, row) in data.iterrows()}
print(nato_dict)

word = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)


#name = user_name.split()
#for letter in name:
#    if letter == nato_dict.letter:
#        print(row.code)


#df = pandas.DataFrame(data_file)
#print(df)
#
#user_name = input("What is your name?").upper()
#user_name.split()
#for letter in user_name:    
#    print(df.code)