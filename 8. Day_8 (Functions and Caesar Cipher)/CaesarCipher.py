alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',  'l', 'm', 'n', 'o', 'p', 'q', 'r',
's', 't', 'u', 'v', 'w', 'x',   'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',  'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',   'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f','g',
'h', 'i', 'j', 'k',  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',   'y', 'z']

def encrypt(plain_text, shift_amount):
   cipher_text = ""
   for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      new_letter = alphabet[new_position]
      cipher_text += new_letter
   print(f"The encoded text is '{cipher_text}'.")
      
      
def decrypt(cipher_text, shift_amount):
   normal_text = ""
   for letter in cipher_text:
       position = alphabet.index(letter)
       new_position = position - shift_amount
       new_letter = alphabet[new_position]
       normal_text += new_letter
   print(f"The decoded text is '{normal_text}'.")
        
#if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
#else:
#   decrypt(cipher_text=text, shift_amount=shift)       