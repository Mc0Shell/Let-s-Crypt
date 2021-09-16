import os
from cryptography.fernet import Fernet
import cryptography
import base64
from termcolor import colored

def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    
    banner()

def strToInt(string):
    tmp = []

    for x in range(len(string)):
        tmp.append(int(ord(string[x])))

    return tmp

def intToString(int):
    tmp = []

    for x in range(len(int)):
        tmp.append(str(chr(int[x])))

    return tmp

def banner():
    print(colored("""
   __        _                                     _   
  / /   ___ | |_   ___    ___  _ __  _   _  _ __  | |_ 
 / /   / _ \| __| / __|  / __|| '__|| | | || '_ \ | __|
/ /___|  __/| |_  \__ \ | (__ | |   | |_| || |_) || |_ 
\____/ \___| \__| |___/  \___||_|    \__, || .__/  \__|
                                     |___/ |_|   
                     by Mc0Shell
""", 'blue'))

key = b'Kuc11VOV_igMzl1z0bGh2NBegtBfaNPdkrKAQmQ-iUE=' #randomly generated
fernet = Fernet(key)

try:
    while True:
        screen_clear()

        print("\n Select an option: ")
        print(colored("\n   [1] > Encrypt a text", "yellow"))
        print(colored("   [2] > Decrypt a text", "yellow"))
        print(colored("\n   [3] > Exit\n", "red"))

        opt = input(colored(' > ', 'blue'))

        if opt == '1':
            screen_clear()
            print("\n Enter the text to be encrypted \n")
            text = input(colored(' > ', 'blue'))

            screen_clear()
            print("\n Enter the password for encryption \n")
            password = input(colored(' > ', 'blue'))

            screen_clear()
            print("\n Data Summary: \n")
            print(colored("     Text: ", "yellow") + text)
            print(colored("     Passowrd: ", "yellow") + password + "\n\n")

            crText = strToInt(text)
            crPassword = strToInt(password)

            crRes = []
            y = 0

            for x in range(len(text)):
                crRes.append(crText[x] + crPassword[y])

                if y == len(password)-1:
                    y = 0
                else:
                    y = y + 1

            print(" Output: \n\n    ", end="")

            st = ""
            for x in crRes:
                st += str(x) + " "
            st = st[0:-1]

            fernetConv = fernet.encrypt(st.encode())
            out = fernetConv.decode("utf-8")
            print(colored(out, "green"))

            r = input("\n\n Save text to a file? [" + colored("Y", "green") + "/" + colored("n", "red") + "] > ")
            if r == 'y' or r == 'Y':
                f = open("output.dat","w")
                f.write(str(out))
                f.close()

        elif opt == '2':
            screen_clear()
            print("\n Enter the text to be decrypted \n")
            text = input(colored(' > ', 'blue'))

            screen_clear()
            print("\n Enter the password for decryption \n")
            password = input(colored(' > ', 'blue'))

            screen_clear()
            print("\n Data Summary: \n")
            print(colored("     Text: ", "yellow") + text)
            print(colored("     Passowrd: ", "yellow") + password + "\n\n")

            dec = text.encode()
            try:
                dec = fernet.decrypt(dec)
            except (cryptography.fernet.InvalidToken, TypeError):
                print(colored(" Invalid crypted text", "red"))
                input("\n Press Enter to continue...")
                continue
            dec = dec.decode("utf-8")

            crText = dec.split(' ')
            crPassword = strToInt(password)

            y = 0
            for i in crText:
                crText[y] = int(i)
                y=y+1

            crRes = []
            y = 0

            for x in range(len(crText)):
                crRes.append(crText[x] - crPassword[y])

                if y == len(password)-1:
                    y = 0
                else:
                    y = y + 1

            crRes = intToString(crRes)

            print(" Output: \n\n    ", end="")

            for char in crRes:
                print(char, end="")

            r = input("\n\n Save text to a file? [" + colored("Y", "green") + "/" + colored("n", "red") + "] > ")
            if r == 'y' or r == 'Y':
                f = open("output.dat","w")
                for element in crRes:
                    f.write(str(element))
                f.close()

        elif opt == '3':
            exit(0)

        input("\n\n Press Enter to continue...")
except KeyboardInterrupt:
    exit(0)

input("\n\n Press Enter to continue...")
