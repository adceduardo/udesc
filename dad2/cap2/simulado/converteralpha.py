alphabet = "abcdefghijklmnopqrstuvwxyz"

def decipher(text, displace):
    result = ""
    
    for letter in text:
        if letter.lower() in alphabet:
            pos = alphabet.index(letter.lower())
            new_pos = (pos - displace) % 26
            new_letter = alphabet[new_pos]

            if letter.isupper():
                result+= new_letter.upper()
            
            else:
                result += new_letter
        
        else:
            result += letter
        
    return result

text = "Gy otbktiuky ygu, yuhxkzaju, u xkyarzgju jk as zxghgrnu zkosuyu. Ygtzuy Jasutz."

output = decipher(text, 6)
print(f"\nSaída: {output}\n")