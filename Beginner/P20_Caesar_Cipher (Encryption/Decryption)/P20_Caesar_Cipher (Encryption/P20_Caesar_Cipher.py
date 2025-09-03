import string


ascii_chars = string.ascii_letters + string.digits + string.punctuation + " "

def encrypt(text, shift=1):
    encrypted = []
    for ch in text:
        if ch in ascii_chars:
            new_index = (ascii_chars.index(ch) + shift) % len(ascii_chars)
            encrypted.append(ascii_chars[new_index])
        else:
            encrypted.append(ch) 

    return "".join(encrypted)

def decrypt(text, shift=1):
    decrypted = []
    for ch in text:
        if ch in ascii_chars:
            new_index = (ascii_chars.index(ch) - shift) % len(ascii_chars)
            decrypted.append(ascii_chars[new_index])
        else:
            decrypted.append(ch)
    return "".join(decrypted)



text = "Hello, World!"
enc = encrypt(text, shift=9)
dec = decrypt(enc, shift=9)

print("Original:", text)
print("Encrypted:", enc)
print("Decrypted:", dec)

while True:
    try_it=input("Would You like to try (y/n)? ").lower()
    if try_it!="y":
        print("thanks for Using program")
        break
    else:
        your_text=input("Enter message: ")
        shifts=input("tell us the skips if nothing entered program will use default value:")
        if not shifts :
            shifts=5
        elif shifts.isnumeric():    
            shifts=int(shifts)
        else:
            print("Invalid Number")

        if your_text :
            enc=encrypt(your_text,shifts)   
            print("Encrypted: ",enc)
        
        else:
            print("Sorry Invalid Input")

            