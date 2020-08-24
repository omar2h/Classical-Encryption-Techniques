def repeating(key, text):
    i=0
    while(len(key) != len(text)):
        key += key[i]
        i = 0 if i == len(key) - 1 else i+1
    return key

def auto(key, text):
    for ch in text:
        if len(key) == len(text): break
        key += ch
    return key

def vigenere(key, text, flag):
    cipher = ""
    key = auto(key, text) if flag else repeating(key, text)
    for i in range(len(text)):
        cipher += chr((ord(text[i])-97 + ord(key[i])-97)%26+97)
    return cipher


