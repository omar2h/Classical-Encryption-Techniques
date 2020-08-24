def twobytwoMatrix(key, text, textList, cipher):
    if len(text) % 2: text += 'x'
    for ch in text:
        textList.append(ord(ch) -65)
    for i in range(0,len(textList),2):
        cipher += chr(((key[0]*textList[i] + key[2]*textList[i+1])%26)+65)
        cipher += chr(((key[1]*textList[i] + key[3]*textList[i+1])%26)+65)
    return cipher

def threebythreeMatrix(key, text, textList, cipher):
    if len(text) % 3: text += 'x'
    if len(text) % 3: text += 'x'
    for ch in text:
        textList.append(ord(ch) -65)
    for i in range(0,len(textList),3):
        cipher += chr(((key[0]*textList[i] + key[1]*textList[i+1] + key[2]*textList[i+2])%26)+65)
        cipher += chr(((key[3]*textList[i] + key[4]*textList[i+1] + key[5]*textList[i+2])%26)+65)
        cipher += chr(((key[6]*textList[i] + key[7]*textList[i+1] + key[8]*textList[i+2])%26)+65)
    return cipher

def hillCipher(key, text):
    textList = []
    cipher = ""
    return twobytwoMatrix(key, text, textList, cipher) if len(key) == 4 else threebythreeMatrix(key, text, textList, cipher)