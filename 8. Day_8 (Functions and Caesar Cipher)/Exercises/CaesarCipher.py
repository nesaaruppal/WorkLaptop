from logo import logo
print("Welcome to the Caesar Cipher!")
print(logo)

def caesar(start_text, shift_amount):
    end_text = ""
    for char in start_text:
      if char in alphabet:
        position = alphabet.index(char)
        if direction == "encode":
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
        elif direction == "decode":
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
      else:
        end_text += char
    print(f"The {direction}d text is '{end_text}'.")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',  'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x',   'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',  'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',   'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k',  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',   'y', 'z']

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' todecrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))   
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift)
  
  go_again = input("Would you like to encode/decode more messages? Type 'Y' for yes and 'N' for no.")
  if go_again == "N":
    should_continue == False
    
        



        

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
