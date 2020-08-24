import os
from CaesarCipher import caesar
from PlayFairCipher import playFair
from hillCipher import hillCipher
from vigenereCipher import vigenere
from vernamCipher import vernam

def printCipherCaesarPlayfair(input, out, key, func):
    lines = input.readlines()
    for i in key:
        for line in lines:
            line = line[:-1]
            out.write(func(i, line))
            out.write('\n')
        out.write('\n')
    return
def printHill(input, out, key, func):
    lines = input.readlines()
    for line in lines:
        line = line[:-1]
        out.write(func(key, line))
        out.write('\n')
    out.write('\n')
    return
def printVigenere(input, out, key, bool, func):
    lines = input.readlines()
    for line in lines:
        line = line[:-1]
        out.write(func(key, line, bool))
        out.write('\n')
    out.write('\n')
    return

def main():
    while True:
        choice = int()
        while True:
            try:
                print("Hi, This is Classical Encryption Techniques project")
                print("1: Implementing the five techniques on input files (The short road)")
                print("2: Implementing the five techniques on  new user input (The long road)")
                print("0: Exit")
                choice = int(input("Your choice:"))
            except ValueError:
                print("Come On You Can Do It")
                continue

            if choice != 1 and choice != 2 and choice != 0:
                print("Come On You Can Do It")
                continue
            else: break

        if choice == 1:
            directory = 'Output Files'
            if not os.path.exists(directory):
                os.makedirs(directory)
            caesarIn = open("Input Files/Caesar/caesar_plain.txt", "r")
            caesarOut = open("Output Files/caesar_cipher.txt","w")
            playFairIn = open("Input Files/PlayFair/playfair_plain.txt", "r")
            playFairOut = open("Output Files/playfair_cipher.txt", "w")
            hillIn2x2 = open("Input Files/Hill/hill_plain_2x2.txt", "r")
            hillIn3x3 = open("Input Files/Hill/hill_plain_3x3.txt", "r")
            hillOut = open("Output Files/hill_cipher.txt", "w")
            vigenereIn = open("Input Files/Vigenere/vigenere_plain.txt", "r")
            vignereOut = open("Output Files/vigenere_cipher.txt", "w")
            vernamIn = open("Input Files/Vernam/vernam_plain.txt", "r")
            vernamOut = open("Output Files/vernam_cipher.txt", "w")

            printCipherCaesarPlayfair(caesarIn, caesarOut, [3,6,12], caesar)
            printCipherCaesarPlayfair(playFairIn, playFairOut, ["rats", "archangel"], playFair)
            printHill(hillIn2x2, hillOut, [5, 17, 8, 3], hillCipher)
            printHill(hillIn3x3, hillOut, [2, 4, 12, 9, 1, 6, 7, 5, 3], hillCipher)
            printVigenere(vigenereIn, vignereOut, "pie", 1, vigenere)
            printHill(vernamIn, vernamOut, "SPARTANS", vernam)

            caesarOut.close()
            playFairOut.close()
            hillOut.close()
            vignereOut.close()
            vernamOut.close()


            print("Check files created in the Output Files folder. Ciao")

        elif choice == 2:
            print("Enter plaintext and specify key for each technique")
            plaintext = input("Plaintext:").lower()
            caesarKey = int(input("Enter Caesar cipher key integer:"))
            playfairKey = input("Enter Playfair cipher key word:").lower()
            print(" 1: 2x2 Hill cipher \n 2: 3x3 Hill cipher")
            c = int(input("Choice:"))
            hillKey = []
            if c == 1:
                size = 4
                print("Enter 2x2 key:")
                while(len(hillKey)<size):
                    hillKey.append(int(input()))
            elif c == 2:
                size = 9
                print("Enter 3x3 key:")
                while(len(hillKey)<size):
                    hillKey.append(int(input()))
            vigenereKey = input("Enter Vigenere cipher key word:").lower()
            vernamKey = input("Enter Vernam cipher key word as long as the text:").upper()
            mode = int(input("Specify mode \n 1: Auto mode \n0: Repeating mode \n What have you decided: "))


            caesarCipher = caesar(caesarKey, plaintext)
            playfairCipher = playFair(playfairKey, plaintext)
            hill = hillCipher(hillKey, plaintext.upper())
            vigenereCipher = vigenere(vigenereKey, plaintext, mode)
            vernamCipher = vernam(vernamKey, plaintext.upper())
            print("Text Encrypted")
            print("Caesar Ciphertext:",caesarCipher)
            print("Playfair Ciphertext:",playfairCipher)
            print("Hill Ciphertext:",hill)
            print("vigenere Ciphertext:",vigenereCipher)
            print("vernam Ciphertext:",vernamCipher)

        if int(input("1: Start Over or press any key to EXIT")) != 1:
            break
    return



if __name__ == "__main__":
    main()

