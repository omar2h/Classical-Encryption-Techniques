from collections import OrderedDict

def prepareText(text):
    plainText = ""
    for i in range(len(text)-1):
        if (((text[i] == text[i+1]) or ((text[i] == 'i' or text[i]=='j') and (text[i+1] == 'i' or text[i+1]=='j'))) and i%2==0):
            plainText += text[i] + 'x'
        else:
            plainText+=text[i]
    plainText += text[len(text) - 1] if len(plainText)%2 else text[len(text) - 1]+'x'
    plainText=plainText.replace("j","i")
    return plainText

def prepareMatrixKey(key):
    key = key.replace("j","i")
    matrix = "".join(OrderedDict.fromkeys(key))
    alphabet="abcdefghiklmnopqrstuvwxyz"
    for ch in alphabet:
        if matrix.find(ch) != -1:
            pass
        else:
            matrix+=ch
    return matrix
    
def encrypt(matrix, plain):
    cipher=""
    for i in range(0,len(plain)-1,2):
        a,b = matrix.find(plain[i]), matrix.find(plain[i+1])
        if (20<=a <=24 and 20<=b <=24) or (15<=a <=19 and 15<=b <=19) or (10<=a <=14 and 10<=b <=14) or (5<=a <=9 and 5<=b <=9) or (0<=a <=4 and 0<=b <=4):
            a += 1;
            b += 1
            if a % 5 == 0: a -= 5
            if b % 5 == 0: b -= 5
        elif(abs(a-b)%5==0):
            a+=5; b+=5
            if a>24: a-=25
            if b>24: b-=25
        else:
            x=a%5; y=b%5
            c=abs(x - y)
            if x<y:a+=c; b-=c;
            else: a-=c; b+=c
        cipher+=matrix[a]
        cipher+=matrix[b]
    return cipher

def playFair(key, text):
    return encrypt(prepareMatrixKey(key), prepareText(text))
