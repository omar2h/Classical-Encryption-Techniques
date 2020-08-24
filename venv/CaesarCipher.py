def caesar(key, text):
    cipher=""
    for ch in text:
        temp =  ((ord(ch) + key-97)%26+97)
        cipher += chr(temp)
    return cipher
