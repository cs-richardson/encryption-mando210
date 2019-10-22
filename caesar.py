'''
This program asks the user for the key and the plain text that the user would
like to encrypt using Caesar’s cipher.

Precondition: the key must be a positive integer 

Postcondition: the printed value should be the encrypted line

Miki Ando
'''

# Gets the key and the plain text from the user
k = int(input("Key: "))
txt = str(input("Plain Text: "))

# sets the variable, cipher,  as blank 
cipher = ""

# it gets each letter in the plain text and encrypts each letter
for i in range(len(txt)):
    letter = txt[i]

    # encrypt uppercase characters in plain text using ASCII
    if letter.isupper():
        cipher = cipher + chr((ord(letter) + k - 65) % 26 + 65)
        
    # if there is a space, the encrypted value will still have space
    elif letter == " ":
        cipher = cipher + " "

    # encrypt lowercase characters in plain text using ASCII
    elif letter.islower():
        cipher = cipher + chr((ord(letter) + k - 97) % 26 + 97)

    # if the letter is not an alphabet or space, it will just print out itself
    else:
        cipher = cipher + letter
        
# prints the encrypted line
print ("Cipher Text: " + cipher)

