def vernam(key, text):
    cipher = ""
    for i in range(len(text)):
        cipher += chr((ord(text[i])-65 + ord(key[i])-65)%26+65)
    return cipher